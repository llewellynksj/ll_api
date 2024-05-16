from django.db import models
from django.contrib.auth.models import User


class Leaf(models.Model):
  """
  Leaf model
  """
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=100, blank=True)
  memory = models.TextField()
  parent1 = models.CharField(max_length=100)
  parent2 = models.CharField(max_length=100, blank=True)
  due_date = models.DateField(blank=True, null=True)
  birth_date = models.DateField(blank=True, null=True)
  weight = models.IntegerField(blank=True, null=True)
  quotation = models.CharField(max_length=100, blank=True)
  image = models.ImageField(
    upload_to='images/',
    default='../default_profile',
    blank=True,
  )

  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f'{self.user.username}: {self.name} - {self.due_date}'