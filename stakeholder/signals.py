from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from stakeholder.models import Student, Teacher, Parent, Administrator
from django.contrib.auth.models import User


@receiver(pre_save, sender=Student)
def create_user_for_student(sender, instance, *args, **kwargs):
    if instance.id is None:
        username = instance.student_id
        first_name = instance._first_name
        last_name = instance._last_name
        email = instance._email

        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(username)
        user.save()

        instance.user = user


@receiver(post_save, sender=Student)
def create_post_save_parent_for_student(sender, instance, created, *args, **kwargs):
    if created:
        father_name = instance.father_name
        mother_name = instance.mother_name
        username = father_name[0:3] + "" + mother_name[0:3] + "_" + instance.student_id
        email = instance.email

        user = User(username=username, email=email)
        user.set_password(instance.student_id)
        user.save()

        parent = Parent(user=user, children=instance)
        parent.save()


@receiver(pre_save, sender=Teacher)
def create_user_for_teacher(sender, instance, *args, **kwargs):
    if instance.id is None:
        username = instance.teacher_id
        first_name = instance._first_name
        last_name = instance._last_name
        email = instance._email

        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(username)
        user.save()

        instance.user = user


@receiver(pre_save, sender=Administrator)
def create_user_for_administrator(sender, instance, *args, **kwargs):
    if instance.id is None:

        first_name = instance._first_name
        last_name = instance._last_name
        email = instance._email
        username = first_name[0:3]

        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(username)
        user.save()

        instance.user = user