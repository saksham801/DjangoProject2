from django.shortcuts import render,redirect

import home,time
from home.models import PopularCourse,Toppers,Newsettleer



# Create your views here.
def Home(request):
    courses = PopularCourse.objects.all()
    toppers = Toppers.objects.all()

    if request.method == "POST":
        name = request.POST['names']
        email = request.POST['emails']
        message = request.POST['message1']
        data = Newsettleer(name = name, email = email, message = message)
        data.save()
        time.sleep(3)
        return redirect(success)












    return render(request,'index.html',{'courses':courses,'toppers':toppers})

def success(request):
    return render(request,'success.html')