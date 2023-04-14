from django.shortcuts import redirect, render
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'Login/index.html')

def signup(request):
    if request.method == 'POST':
        # username = request.POST['username']
        username = request.POST.get('username', False);
        lname = request.POST.get('lastname', False);
        fname = request.POST.get('firstname', False);
        email = request.POST.get('email', False);
        pass1 = request.POST.get('password', False);
        pass2 = request.POST.get('confirmpassword', False);

        myUser = User.objects.create_user(username, email , pass1)
        myUser.first_name = fname
        myUser.last_name = lname

        myUser.save()

        messages.success(request , "Your Account has been successfully created.")

        return redirect('signin')

    return render(request, 'Login/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username', False);
        pass1 = request.POST.get('password', False);


        if username == None or pass1 == None:
            return redirect("home")
        
        user = authenticate(username = username , password = pass1)

        if user is not None:
            login(request, user)
            return render(request , "authentication/index.html", {'fname' : fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect("home")
    return render(request, 'Login/signin.html')

def signout(request):
    logout(request)
    redirect('home')