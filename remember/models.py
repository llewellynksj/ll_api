from django.db import models
from django.contrib.auth.models import User
from leaf.models import Leaf


class Remember(models.Model):
    """
    Remember model so users can mark a leaf as remembered or acknowledged
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leaf = models.ForeignKey(
        Leaf, related_name='remember', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} {self.leaf.name}'
