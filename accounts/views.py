from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def user_login(request):
    """
    Handle user login.

    - On GET: Render the login form.
    - On POST: Authenticate user with username and password.
      If valid, log the user in and redirect to the task list.
      If invalid, show an error message.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("task_list")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "accounts/login.html")


def user_logout(request):
    """
    Handle user logout.

    - Only accepts POST requests (for safety).
    - Logs out the current user and redirects to the login page.
    - If accessed with GET, redirect to the task list instead.
    """
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return redirect("task_list")


def signup(request):
    """
    Handle new user registration.

    - On GET: Render the signup form.
    - On POST:
        * Validate password confirmation.
        * Check if the username is already taken.
        * If valid, create a new user, log them in, and redirect to task list.
        * If invalid, show error messages.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect("task_list")
    return render(request, "accounts/signup.html")
