from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Grupo
from .forms import PostForm

class IndexView(ListView):
    template_name='grupos/index.html'
    context_object_name = 'grupos_rec'
    def get_queryset(self):
        return Grupo.objects.all()

class PostDetailView(DetailView):
    model=Grupo
    
    template_name = 'grupos/post-detail.html'

def PostView(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form_list = form.save(commit=False)
            form_list.save()
            form.save_m2m()
        return redirect('grupos:index')
    form = PostForm()
    return render(request,'grupos/post.html',{'form': form})

def edit(request, pk, template_name='grupos/edit.html'):
    post= get_object_or_404(Grupo, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form_list = form.save(commit=False)
        form_list.save()
        form.save_m2m()
        return redirect('grupos:index')
    return render(request, template_name, {'form':form})

def Delete(request, pk, template_name='grupos/confirm_delete.html'):
    post= get_object_or_404(Grupo, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('grupos:index')
    return render(request, template_name, {'object':post})