from django.shortcuts import render, redirect
from .forms import RegisterForm, TweetForm
from django.contrib import messages
from django.contrib.auth import login, logout,  authenticate
from django.contrib.auth.decorators import login_required
from .functions import handle_upload_file
from .models import Tweets, Profile
from .backends import EmailBackend
from website.settings import MEDIA_ROOT
import os


def home(request):
    tweets = Tweets.objects.all()
    user = request.user
    context = {'tweets': tweets, 'user': user}
    return render(request, 'main/home.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile = Profile(user=user, bio='', pic=os.path.join(MEDIA_ROOT+'media'+'178348.jpg'))
            login(request, user)
            messages.success(request, "Signed up successfully")
            return redirect('/home')
        else:
            messages.error(request, "Sign up failed")
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})


def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = EmailBackend.authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "logged in successfully!")
            return redirect('/home')
        else:
            messages.error(request, "login failed!")
            return redirect('/login')

    return render(request, 'registration/login.html')


@login_required(login_url='login')
def tweet(request):
    if request.method == 'POST':
        newTweet = Tweets(author=request.user, text=request.POST['tweet-txt'], image=request.FILES['tweet-img'], likes=[], comments=[], views=[], retweets=[])
        newTweet.save()
        return redirect('home')
    return render(request, 'main/tweet.html')


@login_required(login_url='login')
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {'user': user, 'profile': profile}
    return render(request, 'main/profile.html', context)


@login_required(login_url='login')
def edit_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {'user': user, 'profile': profile}
    return render(request, 'main/edit_profile.html', context)
