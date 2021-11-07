"""Users URLs"""

from django.urls import path
from users.views import UserDetailView


from users import views


urlpatterns = [
    # Posts
    # Management
    path(
        route='login/',
        view=views.login_view,
        name='login'),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name="signup"),
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'),

    path(
        route='<str:username>/',
        view=UserDetailView.as_view(),
        name='detail'
    ),
]
