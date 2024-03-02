from email import message
from msilib.schema import ComboBox
from pyexpat.errors import messages
from sre_constants import SUCCESS
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 , redirect
from blog.models import Post , Comment
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.contrib import messages
from blog.forms import Commentform
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.

def blog_view(request,cat_name=None , username=None , tag_name=None):
    if username != None: 
        posts=Post.objects.filter(author__username=username)

    elif tag_name != None:
        posts=Post.objects.filter(tags__name = tag_name)

    elif cat_name != None : 
        posts= Post.objects.filter(category__name=cat_name)
    else: 
        posts=Post.objects.filter(status=1)
   
    #for paginator
    try:
        posts=Paginator(posts,3)
        page_number= request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)


    return render(request, "blog/blog-home.html",{"posts":posts})

def blog_single(request,pk):

    form=Commentform()
    
    if request.method == "POST":
        form = Commentform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"your comment submited ")
        else:
            messages.add_message(request,messages.ERROR,"your comment  didn't submitted ")


    post = get_object_or_404(Post,id=pk,status=1)
    
    if post.login_require == False :

        comments = Comment.objects.filter(post=post.id,approve=True)
        return render(request, "blog/blog-single.html",{"post":post,"comments":comments,"form":form})
    else:
        return HttpResponseRedirect(reverse("accounts:login"))
        
    


def blog_search(request):
        posts=Post.objects.filter(status=1)
        if request.method == "GET":
            #print(request.GET.get("s"))
            if s:= request.GET.get("s"):
                posts = posts.filter(content__contains=s)




        return render(request,"blog/blog-home.html",{{"posts":posts}})
