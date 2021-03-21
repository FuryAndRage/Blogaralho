from django.urls import path
from . import views

app_name = 'categories'
urlpatterns = [
    path('<int:pk>/', views.CategoryAPIView.as_view(), name = 'category' ),
    path('categories/', views.CategoriesApiView.as_view(), name = 'categories')
]