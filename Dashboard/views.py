from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "home.html")





# Signup view
def signup_view(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password1")

            if password1 == password2:
                u = User.objects.create_user(username = username, password=password1)
                login(request, u)  # Automatically log the user in after signup
                messages.success(request, "Signup successful! Welcome to Sustainify!")
                return redirect("dashboard")  # Redirect to the dashboard after signup
            
            else:
                messages.error(request, "Signup failed. Passwords did not match")    
                return redirect("home")
        
        except:
            messages.error(request, "Signup failed. username already taken.")
            return redirect("home")
        
    return redirect("home")


def dashboard(request):
    return render(request, "dashboard.html")


# Login view
def login_view(request):
    if request.method == "POST":
        u_name = request.POST['username']
        password = request.POST['password']

        print(u_name, password)  # Just for debugging, can remove in production

        # Authenticate the user
        user = authenticate(request, username=u_name, password=password)
        
        # Check if user is authenticated
        if user is not None:
            login(request, user)  # Log the user in
            return redirect("dashboard")  # Redirect to the dashboard after login
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect("home")  # Redirect back to login page

    return redirect("home") # Render the login page if the request is not POST



    






# Logout view
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")  # Redirect to homepage after logout
