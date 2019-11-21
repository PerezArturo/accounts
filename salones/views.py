from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Salon
from .forms import PostForm

class IndexView(ListView):
    template_name='salones/index.html'
    context_object_name = 'salones_rec'
    def get_queryset(self):
        return Salon.objects.all()

def PostView(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('salones:index')
    form = PostForm()
    return render(request,'salones/post.html',{'form': form})

def Delete(request, pk, template_name='salones/confirm_delete.html'):
    post= get_object_or_404(Salon, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('salones:index')
    return render(request, template_name, {'object':post})

""" def index(request):
    salones_rec = Salon.objects.all
    context = {'salones_rec': salones_rec}
    return render(request, 'salones/index.html', context) """
