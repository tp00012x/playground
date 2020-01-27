from core.models import User
from django.db import models
from django.db.models import Q, F


class Post(models.Model):

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user'],
                condition=Q(is_featured=True),
                name='unique featured post per user'
            ),
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    post = models.TextField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Like(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'comment'],
                name='unique like per comment'
            ),
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    is_positive = models.BooleanField(blank=True, null=True)

    def __str__(self):
        positive_or_negative = 'Positive' if self.is_positive else 'Negative'
        return (
            f"{self.user.name} - {self.comment.title} - {positive_or_negative}"
        )
