import time

from django.shortcuts import render, redirect

from contact.models import Contact


# Create your views here.
def contact1(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['Emails']
        message = request.POST['message']
        no = request.POST['phone']
        contact = Contact(name=name, email=email, message=message,no = no)
        contact.save()

        time.sleep(2)
        return redirect('suc')


    return render(request,'cont.html')


