from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("user", kwargs={"pk": self.pk})
    

class Message(models.Model):
    message_text = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        dots = ''
        text_crop_length = 20
        if len(self.message_text) > text_crop_length:
            dots = '...'
        return self.message_text[:text_crop_length] + dots

    def get_absolute_url(self):
        return reverse("messenger:message_details", kwargs={"pk": self.pk})

    def message_preview(self):
        N = 20
        dots = ''
        if len(self.message_text) > N: 
            dots = '...'
        return self.message_text[:50] + dots
    