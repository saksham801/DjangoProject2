from django.shortcuts import render
from topper.models import  topper

# Create your views here.
def topper1(request):
    toppers = topper.objects.all().order_by('-score')

    return render(request, 'topper.html', {'toppers':toppers})
