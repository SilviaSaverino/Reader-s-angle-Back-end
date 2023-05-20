from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class PostFollower(models.Model):
    """
    Model to represent the followers of posts.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner.username} follows post {self.post.id}'