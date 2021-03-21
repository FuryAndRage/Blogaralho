from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('<int:pk>/', views.PostApiView.as_view(),name = 'post'),
    path('posts/', views.PostsApiView.as_view(), name='post')
]