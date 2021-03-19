from django.db import models

class Category(models.Model):
    category_name = models.Model(max_length=255)

    def __str__(self):
        return self.category_name
