from django.db import models
from blogaralho.apps.categories.models import Category


class Post(models.Model):
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    post_image = models.ImageField(upload_to = 'post/%Y/%m', null = True, blank = True)
    post_date = models.DateTimeField(auto_now=True)
    post_location = models.TextField()
    post_is_public = models.BooleanField(default=False, null=True, blank = True)

    def __str__(self):
        return self.post_title
