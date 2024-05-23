from django.db import models
from django.contrib.auth.models import User


class Leaf(models.Model):
  """
  Leaf model
  """

  TYPE_CHOICES = [
    ('during_pregnancy', 'During Pregnancy'),
    ('at_birth_or_shortly_after', 'At Birth or Shortly After'),
  ]

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  type_of_loss = models.CharField(max_length=100, choices=TYPE_CHOICES)
  name = models.CharField(max_length=100, blank=True)
  memory = models.TextField(blank=True)
  parent1 = models.CharField(max_length=100, blank=True)
  parent2 = models.CharField(max_length=100, blank=True)
  due_date = models.DateField(blank=True, null=True)
  birth_date = models.DateField(blank=True, null=True)
  weight = models.IntegerField(blank=True, null=True)
  image = models.ImageField(
    upload_to='images/',
    default='../default_profile',
    blank=True,
  )

  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f'{self.user.username}: {self.name} - {self.due_date}'