import io,csv
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from tablib import Dataset

from .models import Alumno
from .forms import PostForm


# Create your views here.
class IndexView(ListView):
    template_name='alumnos/index.html'
    context_object_name = 'alumnos_rec'
    def get_queryset(self):
        return Alumno.objects.all().order_by('matricula')

def PostView(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            subject = 'Has sido dado de alta'
            message = ' Bienvenido alumno ' +str(form['nombre'].value())+ ' con numero de control ' + str(form['matricula'].value())+ ' al sistema.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = str(form['email'].value())
            send_mail( subject, message, email_from, [recipient_list] )
            return redirect('alumnos:index')
        else:
            return render(request,'alumnos/post.html',{'form': form})
    form = PostForm()
    return render(request,'alumnos/post.html',{'form': form})

def simple_upload(request):
    if request.method == "GET":
        return render(request,'alumnos/post_masivo.html')

    new_alumnos = request.FILES['myfile']

    dataset = new_alumnos.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    next(io_string)
    for column in csv.reader(io_string,delimiter=',',quotechar='|'):
        _, created = Alumno.objects.update_or_create(
            matricula=column[0],
            nombre=column[1],
            apellidop=column[2],
            apellidom=column[3],
            email=column[4],
            semestre=column[5]
        )
        
    context={}
    return redirect('alumnos:index')