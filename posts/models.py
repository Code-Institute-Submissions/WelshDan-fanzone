from django.db import models
from django.contrib.auth.models import User
from supported.models import TeamsList
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = ProcessedImageField(
        upload_to='images/',
        default='../default_post_uxb6vu',
        blank=True,
        processors=[ResizeToFit(width=640, height=480)],
        format='JPEG',
        options={'quality': 90},
    )
    supported_team = models.ForeignKey(
        TeamsList, on_delete=models.CASCADE, null=True,
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
