from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.core.validators import RegexValidator
from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail


# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    phone_regex = RegexValidator(regex='^\??\d{9,11}$', message='Please Enter the number that starts with 9 and has 10 digits.')

    full_name = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_no = models.CharField(max_length=10, blank=True, validators=[phone_regex])

    address = models.CharField(max_length=80, blank=True)
    profile_photo = models.ImageField(blank=True, upload_to = 'images/')


    def __str__(self):
        return f'{self.username}'



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    try:
        email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

        send_mail(
            # title:
            "Password Reset for {title}".format(title="Hamro Cinema"),
            # message:
            email_plaintext_message,
            # from:
            "vinsmokedarshan@gmail.com",
            # to:
            [reset_password_token.user.email],
            fail_silently=False
        )
    except Exception as ex:
        print('Something Went Wrong')
