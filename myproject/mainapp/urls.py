from django.urls import path
from . import views
from .views import category, category_filter

urlpatterns = [
    path('', category),
    path('category/', views.category, name="category"),
    path('<int:pk>', views.category_filter, name="category"),
]
