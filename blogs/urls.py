from django.urls import path

from .views import BlogListCreate

urlpatterns =[
  path('api/blogs', BlogListCreate.as_view())
]