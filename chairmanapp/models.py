from django.db import models
from django.utils import timezone
import math
from django.templatetags.static import static


# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True, max_length=30, blank=True)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)
    otp = models.IntegerField(default=7250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + '----->' + self.role


class Chairman(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    pic = models.FileField(upload_to="media/upload",
                           default="media/chairman.jpg")

    def __str__(self):
        return self.firstname


class Societymember(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    block_no = models.IntegerField()
    email = models.EmailField()

    occupation = models.CharField(max_length=30, blank=True, null=True)
    dob = models.DateField(max_length=30, blank=True, null=True)
    no_of_familymembers = models.CharField(
        max_length=30, blank=True, null=True)
    vehicle_deatils = models.CharField(max_length=30, blank=True, null=True)
    blood_group = models.CharField(max_length=30, blank=True, null=True)
    house_ownership = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)

    Gender_Choices = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(choices=Gender_Choices, max_length=1)
    pro_pic = models.ImageField(
        upload_to="media/upload", default='media/male-icon.png')

    default_pic_mapping = {'others': 'default.png',
                           'M': 'male-icon.png', 'F': 'female-icon.png'}

    def __str__(self):
        return self.firstname


class Notice(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    discription = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"

            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"


class Complaint(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint_title = models.CharField(max_length=50)
    complaint_discription = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"

            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"


class Event(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    events_title = models.CharField(max_length=50)
    events_discription = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"

            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"


class Maintenance(models.Model):

    # chairman add maintenance
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # societymember view maintenance
    member_id = models.ForeignKey(Societymember, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    amount = models.CharField(max_length=40)
    duedate = models.DateField(auto_now_add=True)
    status = models.CharField(default='PENDING', max_length=40)

    def __str__(self) -> str:
        return self.member_id.firstname


class Transaction(models.Model):
    made_by = models.ForeignKey(Societymember, related_name='transactions',on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime(
                'PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
