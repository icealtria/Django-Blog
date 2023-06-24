from django.db import models

from blog.models import Post
# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
