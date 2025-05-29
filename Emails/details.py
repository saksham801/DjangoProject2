import pymongo
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string
import os
import requests
from datetime import datetime


def ip():
    # Get public IP address and location info
    response = requests.get("https://ipinfo.io/json")

    if response.status_code == 200:
        data = response.json()
        ip_address = data.get("ip")
        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        location = f"{city}, {region}, {country}"

        return ip_address, location
    else:
        print("Failed to retrieve IP information.")


def generate_otp(length=6):
    """Generate an alphanumeric OTP with uppercase letters and digits."""
    characters = string.ascii_uppercase + string.digits
    otp = ''.join(random.choices(characters, k=length))
    return otp


def sending_otp(otp=generate_otp(6), email=''):
    # Email details
    sender_email = "dubeysaksham796@gmail.com"
    receiver_email = email
    password = "dfnfoasnifvnhzwt"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the Emails message
    message = MIMEMultipart("alternative")
    message["Subject"] = "OTP FROM Adhyayan Coaching Institute [ACI]"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Your OTP HTML Content
    html = f"""<!DOCTYPE html>
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

    # Attach HTML content
    part = MIMEText(html, "html")
    message.attach(part)

    # Send the Emails
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print(f'''OTP Send successfully to {email} If You don't recive it check your spam folder''')
        return otp




    except Exception as e:
        print(f"Error sending email: {e}")
        return otp


def sending_username(email="", username=""):
    # Email details
    sender_email = "dubeysaksham796@gmail.com"
    receiver_email = email
    password = "dfnfoasnifvnhzwt"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the Emails message
    message = MIMEMultipart("alternative")
    message["Subject"] = "USERNAME FROM LIBRARY MANAGEMENT SYSTEM [LMS]"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Your Username HTML Content
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Your Username - Adhyayan Coaching Institute</title>
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
      </style>
    </head>
    <body style="margin:0; padding:0; font-family:'Roboto', sans-serif; background-color:#000000;">
      <table width="100%" cellpadding="0" cellspacing="0" style="padding: 30px 0;">
        <tr>
          <td align="center">
            <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 0 15px rgba(255,255,255,0.1);">

              <!-- Header -->
              <tr>
                <td style="background-color:#000000; padding: 20px; color:#ffffff; text-align:center;">
                  <h1 style="margin:0; font-size:24px;">Adhyayan Coaching Institute</h1>
                  <p style="margin:0; font-size:14px;">Your Login Information</p>
                </td>
              </tr>

              <!-- Body Content -->
              <tr>
                <td style="padding: 30px; color:#111111;">
                  <h2 style="color:#000000;">Dear Student,</h2>
                  <p style="font-size:16px;">Thank you for registering with <strong>Adhyayan Coaching Institute</strong>.</p>
                  <p style="font-size:16px;">Here is your username:</p>

                  <div style="margin: 30px 0; text-align: center;">
                    <span style="display:inline-block; background-color:#000000; color:#ffffff; padding:15px 30px; font-size:24px; font-weight:bold; border-radius:8px;">
                      {username}
                    </span>
                  </div>

                  <p style="font-size:14px; color:#444444;">Please keep this username safe. You will need it to log in to your account.</p>
                  <p style="font-size:14px; color:#888888;">If you did not create this account, you may ignore this email.</p>
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

    # Attach HTML content
    part = MIMEText(html, "html")
    message.attach(part)

    # Send the Emails
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print(f'''Username Send successfully to {email} If You don't recive it check your spam folder''')



    except Exception as e:
        print(f"Error sending email: {e}")


def sending_password(email="", password1=""):
    # Email details
    sender_email = "dubeysaksham796@gmail.com"
    receiver_email = email
    password = "dfnfoasnifvnhzwt"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the Emails message
    message = MIMEMultipart("alternative")
    message["Subject"] = " PASSWORD FROM LIBRARY MANAGEMENT SYSTEM [LMS]"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Your Username HTML Content
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Your Login Info - Adhyayan Coaching Institute</title>
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
      </style>
    </head>
    <body style="margin:0; padding:0; font-family:'Roboto', sans-serif; background-color:#000000;">
      <table width="100%" cellpadding="0" cellspacing="0" style="padding: 30px 0;">
        <tr>
          <td align="center">
            <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 0 15px rgba(255,255,255,0.1);">

              <!-- Header -->
              <tr>
                <td style="background-color:#000000; padding: 20px; color:#ffffff; text-align:center;">
                  <h1 style="margin:0; font-size:24px;">Adhyayan Coaching Institute</h1>
                  <p style="margin:0; font-size:14px;">Your Login Information</p>
                </td>
              </tr>

              <!-- Body Content -->
              <tr>
                <td style="padding: 30px; color:#111111;">
                  <h2 style="color:#000000;">Dear Student,</h2>
                  <p style="font-size:16px;">Thank you for registering with <strong>Adhyayan Coaching Institute</strong>.</p>
                  <p style="font-size:16px;">Here is your password:</p>

                  <div style="margin: 30px 0; text-align: center;">
                    <span style="display:inline-block; background-color:#000000; color:#ffffff; padding:15px 30px; font-size:24px; font-weight:bold; border-radius:8px;">
                      {password1}
                    </span>
                  </div>

                  <p style="font-size:14px; color:#444444;">Please keep this password safe. You will need it to log in to your account.</p>
                  <p style="font-size:14px; color:#888888;">If you did not create this account, you may ignore this email.</p>
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

    # Attach HTML content
    part = MIMEText(html, "html")
    message.attach(part)

    # Send the Emails
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print(f'''Password Send successfully to {email} If You don't recive it check your spam folder''')

    except Exception as e:
        print(f"Error sending email: {e}")


def sending_greeting(email=""):
    # Email details
    sender_email = "dubeysaksham796@gmail.com"
    receiver_email = email
    password = "dfnfoasnifvnhzwt"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the Emails message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Greeting From Adhyayan Coaching Institute [ACI] "
    message["From"] = sender_email
    message["To"] = receiver_email

    # Your Username HTML Content
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Welcome to Adhyayan Coaching Institute</title>
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
      </style>
    </head>
    <body style="margin:0; padding:0; font-family:'Roboto', sans-serif; background-color:#000000;">
      <table width="100%" cellpadding="0" cellspacing="0" style="padding:30px 0;">
        <tr>
          <td align="center">
            <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:12px; overflow:hidden; box-shadow:0 0 15px rgba(255,255,255,0.1);">
              <tr>
                <td style="background-color:#000000; padding: 25px; text-align:center;">
                  <h1 style="margin:0; font-size:26px; color:#ffffff;">Adhyayan Coaching Institute</h1>
                  <p style="margin:5px 0 0; font-size:15px; color:#bbbbbb;">Welcome Aboard!</p>
                </td>
              </tr>
              <tr>
                <td style="padding:30px; color:#111111;">
                  <h2 style="color:#000000; margin-top:0;">Dear Student,</h2>
                  <p style="font-size:16px;">Thank you for registering with <strong>Adhyayan Coaching Institute</strong>!</p>
                  <p style="font-size:16px;">You now have access to top-tier learning resources, expert guidance, and a supportive academic environment designed to help you succeed.</p>
                  <div style="margin:30px 0; text-align:center;">
                    <span style="display:inline-block; background-color:#000000; color:#ffffff; padding:15px 25px; font-size:18px; font-weight:bold; border-radius:10px;">
                      Let's Begin the Journey!
                    </span>
                  </div>
                  <p style="font-size:14px; color:#444444;">If you have any questions, our support team is always ready to help you.</p>
                  <br>
                  <p style="font-size:14px; color:#000000;">– The Adhyayan Team</p>
                </td>
              </tr>
              <tr>
                <td style="background-color:#f2f2f2; text-align:center; padding:15px; font-size:12px; color:#555;">
                  © 2025 Adhyayan Coaching Institute. All rights reserved.
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </body>
    </html>
    """

    # Attach HTML content
    part = MIMEText(html, "html")
    message.attach(part)

    # Send the Emails
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print(f'''Greeting Send successfully to {email} If You don't recive it check your spam folder''')

    except Exception as e:
        print(f"Error sending email: {e}")


def sending_login(email=""):
    sender_email = "dubeysaksham796@gmail.com"
    receiver_email = email
    password = "dfnfoasnifvnhzwt"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the Emails message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Greeting From Adhyayan Coaching Institute [ACI] "
    message["From"] = sender_email
    message["To"] = receiver_email

    now = datetime.now()
    date = now.strftime("%B %d, %Y")
    time1 = now.strftime("%I:%M %p")

    ip_add, location = ip()

    # Your Username HTML Content
    html =  f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Login Notification</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
  </style>
</head>
<body style="margin:0; padding:0; background-color:#000000; font-family:'Roboto', sans-serif; color:#ffffff;">
  <table width="100%" cellpadding="0" cellspacing="0" style="padding: 40px 0;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color:#1a1a1a; border-radius:10px; overflow:hidden; box-shadow:0 0 20px rgba(255,255,255,0.1);">
          <!-- Header -->
          <tr>
            <td style="background-color:#111; padding: 30px; text-align:center; border-bottom:1px solid #333;">
              <h1 style="margin:0; font-size:24px; color:#ffffff;">Adhyayan Coaching Institute</h1>
              <p style="margin:8px 0 0; font-size:14px; color:#aaaaaa;">Login Alert</p>
            </td>
          </tr>

          <!-- Content -->
          <tr>
            <td style="padding: 30px;">
              <h2 style="color:#ffffff; margin-top:0;">Hello Reader,</h2>
              <p style="font-size:16px; color:#cccccc; line-height:1.6;">
                We detected a new login to your account on <strong style="color:#ffffff;">Adhyayan Coaching Institute</strong>.
              </p>

              <table width="100%" cellpadding="0" cellspacing="0" style="margin: 25px 0; font-size:15px; color:#dddddd;">
                <tr>
                  <td style="padding: 8px 0;"><strong>Date:</strong></td>
                  <td style="padding: 8px 0;">{date}</td>
                </tr>
                <tr>
                  <td style="padding: 8px 0;"><strong>Time:</strong></td>
                  <td style="padding: 8px 0;">{time1} (IST)</td>
                </tr>
                <tr>
                  <td style="padding: 8px 0;"><strong>IP Address:</strong></td>
                  <td style="padding: 8px 0;">{ip_add}</td>
                </tr>
                <tr>
                  <td style="padding: 8px 0;"><strong>Location:</strong></td>
                  <td style="padding: 8px 0;">{location}</td>
                </tr>
              </table>

              <p style="font-size:14px; color:#aaaaaa;">If this login was you, no further action is needed.</p>
              <p style="font-size:14px; color:#ff4c4c;">If you did not perform this login, please <strong>reset your password</strong> and contact our support team immediately.</p>

              <br>
              <p style="font-size:14px; color:#ffffff;">– Adhyayan Coaching Institute Team</p>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background-color:#111; text-align:center; padding: 20px; font-size:12px; color:#777777; border-top:1px solid #333;">
              © 2025 Adhyayan Coaching Institute. All rights reserved.
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""


    # Attach HTML content
    part = MIMEText(html, "html")
    message.attach(part)

    # Send the Emails
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print(f'''Login Details Send successfully to {email} If You don't recive it check your spam folder''')

    except Exception as e:
        print(f"Error sending email: {e}")

