#for registertion templatetags

from tkinter.tix import STATUS
from turtle import pos
from django.shortcuts import get_object_or_404 , render
from blog.models import *
from blog.models import Post
from blog.models import Category
from django import template
register = template.Library()

@register.simple_tag(name="totalposts")
def function():
    posts = Post.objects.filter(status = 1).count()

    return posts


@register.simple_tag(name="posts")
def function():
    posts = Post.objects.filter(status = 1)
    return posts


@register.simple_tag(name='comments_count')
def function(pid):
    post = Post.objects.get(pk=pid)
    return Comment.objects.filter(post=post.id,approve=True).count()



@register.filter(name="snippet")
def function(value):
    return value[:100]

@register.inclusion_tag("blog/blog-category.html")

def postcategories():
    posts = Post.objects.filter(status =1)
    category = Category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name]=posts.filter(category=name).count()
    return {"categories":cat_dict}
        

@register.inclusion_tag("blog/blog-popular.html")
def latestposts(args=3):
    posts = Post.objects.filter(status=1).order_by("-published_date")[:args ]
    return {"posts":posts}
