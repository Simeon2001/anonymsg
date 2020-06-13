from django.shortcuts import render,get_object_or_404
from .models import Comment,Post
from .forms import CommentForm
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User

# Create your views here.

class IndeView(ListView):
    model = Post
    template_name = 'msg/inde.html'
    context_object_name = 'ur'
    
 #view post           
def IndexView (request):
    if request.user:
        current_user = request.user
        a = current_user.id
        b = Post.objects.filter(name_id = a)
        return render (request, 'msg/index.html', {'b':b})
        
    else:
        return render (request, 'msg/post.html')
        
#comments section
def postr (request,pk):
    post = Post.objects.get(nickname=pk)
    comm = None
    if request.method == 'POST':
        cform = CommentForm(request.POST)
        if cform.is_valid():
            comm = cform.save(commit=False)
            comm.post = post
            comm.save()
    
    else:
	    cform = CommentForm()
    
    return render(request,'msg/post.html',{'post':post,'comm':comm,'cform':cform})
#view comments
@login_required(login_url='login')    
def comment_lock (request,pi):
    current_user = request.user
    ad = current_user.id
    post = get_object_or_404(Post,pk=pi)
    comments = post.comments.filter(active=True)
    
    return render(request,'msg/detail.html',{'post':post,'comments':comments,'ad':ad})
#logout    
def logout (request):
    return render (request,'registration/logout.html')
#signup 
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register/register.html'
    
#create post    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'msg/create.html'
    fields = ['nickname', 'text']
    login_url = 'login' 
    def form_valid(self, form): # new
        form.instance.name = self.request.user
        return super().form_valid(form)

#delete post    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): # new
    model = Post
    template_name = 'msg/delete.html'
    success_url = reverse_lazy('Home/')
    login_url = 'login' 
    def test_func(self): # new
        obj = self.get_object()
        return obj.name == self.request.user
    
    
    
    
    
    
    
    
    
    
    
    
    