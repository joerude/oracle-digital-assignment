from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from class_management.models import Student
from config.settings import EMAIL_HOST_USER


@receiver(post_save, sender=Student)
def send_mail_student_after_successful_creation(sender, instance, **kwargs):
    subject = 'Вас добавили в систему школы'
    message = f'{instance.full_name}, вы были добавлены в систему от Oracle Digital'

    send_mail(subject,
              message,
              from_email=EMAIL_HOST_USER,
              recipient_list=[instance.email],
              fail_silently=False)
