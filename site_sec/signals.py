from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

@receiver(user_logged_in)
def set_email_cookie_on_login(sender, request, user, **kwargs):
    response = request  
    response.set_cookie('email', user.email, max_age=None)  