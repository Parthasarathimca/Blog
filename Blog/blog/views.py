from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from blog.models import BLOG,LIKE
import json

def user_login(request):
    data={}
    if request.method == 'GET':
        return render(request, "login.html",data)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/blogs/")
    else:
        data={"error":"Invalid Login"}
        template="login.html"
    return render(request, template,data)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")

    

@login_required()
def blogs(request):
    data={}
    blogs=BLOG.objects.all().order_by("-create_datetime")
    #blogs_likes=LIKE.objects.prefetch_related('blog')
    #print("=============",blogs_likes)
    data.update({"blogs":blogs})
    return render(request, "blogs.html",data)

@login_required()
def likes(request):
    data={}
    #try:
    blog_id=request.POST['blog_id']
    blog= BLOG.objects.get(id=blog_id) if blog_id else None
    if blog:
        instance=LIKE.objects.create(blog=blog,created_by=request.user)
        instance.save()
    total_likes=LIKE.objects.filter(blog=blog_id).count()
    data={'total_likes':total_likes}
    #except Exception as identifier:
    #    pass
    return HttpResponse(json.dumps(data), status=200)
