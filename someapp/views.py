from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from someapp import models
from someapp import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import TemplateView


# Create your views here.

def index(req):
    if(req.method=="GET"):
        f=UserCreationForm()
        d={
            "form":f
        }
        return render(req,'someapp/login.html',d)
    else:
        f=UserCreationForm(req.POST)
        if(f.is_valid()):
            f.save()
            username=f.cleaned_data.get("username")
            password=f.cleaned_data.get("password")
            user=authenticate(username,password)
            if(user):
                login(req,user)


def add(request):
    print(request.POST)
    print(type(request.POST))
    a=request.POST.get("a")
    b=request.POST.get("b")
    return HttpResponse(int(a)+int(b))


@login_required(login_url="auth/login")
def profile(request,name):
    #name=request.GET.get("name")
    skills=["Java","python","golang","javascript"]
    d={"name":name,"skills":skills}
    return render(request,'someapp/index.html',d)


def submit(request):
    username=request.POST.get("username")
    comment=request.POST.get("comment")

    commentModel=models.Comments(username=username,content=comment)
    commentModel.save()

    commentList=models.Comments.objects.all()

    for i in commentList:
        print(i)
    skills = ["Java", "python", "golang", "javascript"]
    d = {"name": username, "skills": skills,"comment":comment}
    return render(request, 'someapp/index.html', d)


def addComment(request):
    has_commented=request.session.get("has_commented")
    if(not has_commented):
        request.session["has_commented"]=True
        f=forms.CommentForm(request.POST)
        f.save()
        return HttpResponse("success")
    else:
        return HttpResponse("You have already commented")

@login_required(login_url='/auth/login')
def showComments(request):

    comments=models.Comments.objects.all()
    user=request.user

    d={
        "comments":comments,
        "user":user
    }
    return render(request,'someapp/comments.html',d)

def delComment(request):
    comment_id=request.POST.get("comment_id")
    models.Comments.objects.filter(pk=comment_id).delete()
    return HttpResponse("comment deleted")




def login(request):
    if(request.method=="GET"):
        f=forms.LoginForm()
        return render(request,'someapp/login.html',{"form":f})
    else:
        f=forms.LoginForm(request.POST)
        if(f.is_valid()):

            user=authenticate(request,username,password)
            if  user:
                login(request)

            pass
        return


def someform(req):
    if(req.method=="GET"):
        f=forms.CommentForm()
        d={
            "form":f
        }
        return render(req,'someapp/some_form.html',d)
    elif(req.method=="POST"):
        f=forms.CommentForm(req.POST)
        if(f.is_valid()):
            f.save()
            return HttpResponse("success "+str(req.user))
        else:
            return HttpResponse("Failed "+str(f.errors))




