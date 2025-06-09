from django.db.models.signals import post_save
from django.dispatch import receiver
from borrow.models import Borrow, Member

@receiver(post_save, sender=Borrow)
def create_member_on_first_borrow(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        if not Member.objects.filter(user=user).exists():
            Member.objects.create(user=user)
