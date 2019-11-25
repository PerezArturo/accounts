from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Materia
from .forms import PostForm

class IndexView(ListView):
    template_name='materias/index.html'
    context_object_name = 'materias_rec'
    def get_queryset(self):
        return Materia.objects.all().order_by('-semestre')

def PostView(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('materias:index')
        else:
            return render(request,'materias/post.html',{'form': form})

    form = PostForm()
    return render(request,'materias/post.html',{'form': form})

def Delete(request, pk, template_name='materias/confirm_delete.html'):
    post= get_object_or_404(Materia, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('materias:index')
    return render(request, template_name, {'object':post})