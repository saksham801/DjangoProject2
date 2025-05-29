from django.http import HttpResponse
from django.shortcuts import render,redirect
import random
import string
from django.core.mail import send_mail
from login.models import login as login_model
from django.contrib import messages
from database.login import login_data
import pymongo
from django.contrib.auth.hashers import check_password
import time
from Emails import details



client = pymongo.MongoClient("mongodb+srv://dubeysaksham796:Iron_Man@adhyayancoachinginstitu.hqcuhrf.mongodb.net/?retryWrites=true&w=majority&appName=AdhyayanCoachingInstitute")
db = client['Adhyayan_Coaching_Institute']
collection = db['login_user']


# Create your views here.
def login(request):
    if request.method == "POST":
        form_type = request.POST.get('form_type')

        # --- Login ---
        if form_type == 'login':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_details = collection.find_one({'$or': [{'Emails': email}, {'user_name': email}]})


            if user_details:
                from django.contrib.auth.hashers import check_password
                if check_password(password, user_details.get('password')):
                    messages.success(request, 'You are logged in')
                    email1 = user_details.get('Emails')
                    details.sending_login(email=email1)
                    return redirect('home')
                else:
                    return render(request, 'incorrect.html')
            else:
                return render(request, 'incorrect_user.html')

        # --- Signup Step 1: Send OTP ---
        elif form_type == 'signup':
            email = request.POST.get('email', '').strip().lower()

            if not send_and_store_otp(request, email):
                messages.error(request, 'Email already registered or failed to send OTP.')
                return render(request, 'already.html')

            return render(request, 'singup.html', {'show_otp': True, 'email': email})


        # --- Signup Step 2: Verify OTP ---
        elif form_type == 'otp':
            user_otp = request.POST.get('otp')
            session_otp = request.session.get('otp')
            data = request.session.get('signup_data')
            email = request.POST.get('email', '').strip().lower()

            # ✅ Recheck email existence to avoid duplicates
            if collection.find_one({'email': email}):
                messages.error(request, 'This email is already registered.')
                return render(request, 'already.html')

            # ✅ Verify OTP and store only if it's correct and email not yet registered
            if user_otp == session_otp and data:
                login_data(**data)  # Safely stores in MongoDB
                messages.success(request, 'Signup successful!')
                request.session.flush()  # Clear all session data
                return redirect('login')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')
                return render(request, 'singup.html', {'show_otp': True, 'email': email})

    # For GET requests or fallback
    return render(request, 'singup.html')



from django.contrib.auth.hashers import make_password, check_password


def send_and_store_otp(request, email):
    # 🚫 If email already exists, return early and don't store anything
    if collection.find_one({'Emails': email}):
        return False

    otp = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    request.session['otp'] = otp
    request.session['signup_data'] = {
        'name': request.POST.get('name'),
        'email': email,
        'age': request.POST.get('age'),
        'phone_no': make_password(request.POST.get('phone_no')),
        'password': make_password(request.POST.get('password')),
        'user_name': request.POST.get('user_name'),
    }

    subject = 'Your OTP for Adhyayan Coaching Institute'
    message = f'Your OTP is: {otp}'
    html_message = f"""<!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Your OTP Code - Adhyayan Coaching Institute</title>
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
      </style>
    </head>
    <body style="margin:0; padding:0; font-family: 'Roboto', sans-serif; background-color:#000000;">
      <table width="100%" cellpadding="0" cellspacing="0" style="padding: 30px 0;">
        <tr>
          <td align="center">
            <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 0 15px rgba(255,255,255,0.1);">

              <!-- Header -->
              <tr>
                <td style="background-color:#000000; padding: 20px; color:#ffffff; text-align:center;">
                  <h1 style="margin:0; font-size:24px;">Adhyayan Coaching Institute</h1>
                  <p style="margin:0; font-size:14px;">Secure OTP Verification</p>
                </td>
              </tr>

              <!-- Body Content -->
              <tr>
                <td style="padding: 30px; color:#111111;">
                  <h2 style="color:#000000;">Hello Student,</h2>
                  <p style="font-size:16px;">You're trying to access your account at <strong>Adhyayan Coaching Institute</strong>.</p>
                  <p style="font-size:16px;">Use the following OTP to verify your identity:</p>

                  <div style="margin: 30px 0; text-align: center;">
                    <span style="display:inline-block; background-color:#000000; color:#ffffff; padding:15px 30px; font-size:24px; font-weight:bold; letter-spacing:5px; border-radius:8px;">
                      {otp}
                    </span>
                  </div>

                  <p style="font-size:14px; color:#444444;">This OTP is valid for only 10 minutes. Please do not share it with anyone.</p>
                  <p style="font-size:14px; color:#888888;">If you did not request this OTP, you may safely ignore this message.</p>
                  <br>
                  <p style="font-size:14px; color:#000000;">– The Adhyayan Team</p>
                </td>
              </tr>

              <!-- Footer -->
              <tr>
                <td style="background-color:#f2f2f2; padding: 15px; text-align:center; font-size:12px; color:#666;">
                  &copy; 2025 Adhyayan Coaching Institute. All rights reserved.
                </td>
              </tr>

            </table>
          </td>
        </tr>
      </table>
    </body>
    </html>
    """

    try:
        send_mail(
            subject,
            message,
            'dubeysaksham796@gmail.com',
            [email],
            fail_silently=False,
            html_message=html_message
        )
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

    return True

