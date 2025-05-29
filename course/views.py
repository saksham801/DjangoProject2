from django.shortcuts import render
from home.models import Course
from database.course import course_name
import pymongo


client = pymongo.MongoClient('mongodb+srv://dubeysaksham796:Iron_Man@adhyayancoachinginstitu.hqcuhrf.mongodb.net/?retryWrites=true&w=majority&appName=AdhyayanCoachingInstitute')
db = client['Adhyayan_Coaching_Institute']
collection = db['course']



# Create your views here.
def index(request):
    courses = Course.objects.all()
    user =list( collection.find())
    return render(request,'courses.html',{'user':user})
