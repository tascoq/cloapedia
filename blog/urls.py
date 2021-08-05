from django.urls import path

from .views import main_page, create_post, user_posts

urlpatterns = [
    path('my-posts/', user_posts, name='my_posts'),
    path('create-post/', create_post, name='create_post'),
    path('', main_page, name='main_page'),
]
