from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_school(request):
    form=SchoolForm()
    d={'form':form}
    if request.method=="POST":
        form_data=SchoolForm(request.POST)
        if form_data.is_valid():
            n=form_data.cleaned_data['name']            
            p=form_data.cleaned_data['principal']
            l=form_data.cleaned_data['location']
            S=School.objects.get_or_create(name=n,principal=p,location=l)[0]
            S.save()
            return HttpResponse('Data inserted successfully')


    return render(request,'insert_school.html',d)
