from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse
import sesame.utils

from .forms import EmailLoginForm  # Make sure this is correctly imported

def email_login_view(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            User = get_user_model()
            try:
                user = User.objects.get(email=email)
                __send_login_email(user, request)
            except User.DoesNotExist:
                # Ignore if no user found. Alternatively, show an error or a message.
                print("user not found:", email)
            
            # Redirect to a success page
            return render(request, "email_login_success.html")
    else:
        form = EmailLoginForm()
    
    return render(request, "email_login.html", {'form': form})

def __send_login_email(user, request):
    # Create a login link
    link = reverse("login")  # Ensure this is the correct view name for your login view
    link = request.build_absolute_uri(link)
    link += sesame.utils.get_query_string(user)

    # Send email
    subject = "Log in to autogenius"
    message = f"""\
Hello,

You requested that we send you a link to log in to our app:

    {link}

Thank you for joining the beta!
"""
    user.email_user(subject, message)
