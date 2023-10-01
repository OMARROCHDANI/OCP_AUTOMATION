from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import password_validation


def home(request):
    return render(request, 'authenticationindex2.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists!")
            return redirect('/authentication/')
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('/authentication/')
        if len(username) > 10:
            messages.error(request, 'Username must be under 10 characters')
            return redirect('/authentication/')
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")
            return redirect('/authentication/')
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric")
            return redirect('/authentication/')

        try:
            password_validation.validate_password(pass1, user=User(username=username))
        except password_validation.ValidationError as validation_error:
            messages.error(request, validation_error.messages[0])
            return redirect('/authentication/signup/')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect('/authentication/signin/')

    return render(request, 'signup2.html')

def authenticationindex2(request):
    if request.user.is_authenticated:
        fname = request.user.first_name
        return render(request, "authenticationindex2.html", {'fname': fname, 'user_is_authenticated': True})
    else:
        return redirect("/authentication/")    
 

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password =pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('/authentication/authenticationindex2/')
        else:
            messages.error(request, "Bad Credentials")
            return redirect("/authentication/")
    return render(request, 'signin2.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully") 
    return redirect("/authentication/") 