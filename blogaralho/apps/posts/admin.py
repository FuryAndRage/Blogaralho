from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    
    summernote_fields = ('post_content',)

admin.site.register(Post, PostAdmin)