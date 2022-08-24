from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Core(models.Model):

   title= models.CharField(max_length=50)
   excerpt=models.TextField(null=True)
   author=models.ForeignKey(User,  on_delete=models.CASCADE)
   slug=models.SlugField(max_length=100,unique=True)
   update=models.DateField(auto_now=True, )
   published=models.DateField(default=timezone.now)

   def get_absolute_url(self):
       return reverse("single_post", args=[self.slug])

   class Meta:
    ordering=['-published']

   def __str__(self):
      return self.title
   