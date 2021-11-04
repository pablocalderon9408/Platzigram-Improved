"""Post URLs"""

from django.urls import path


from posts import views


urlpatterns = [

    path(
        route='',
        view= views.list_posts,
        name='Feed'),
        
    path(
        route='posts/new',
        view = views.create_post,
        name='create'),
]