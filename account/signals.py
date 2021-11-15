from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.conf import settings

User = get_user_model()

@receiver(post_save, sender=User)
def token_after_create(created, instance, *args, **kwargs):
    if created:
        Token.objects.create(user=instance)

