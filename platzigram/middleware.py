# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:

    """Ensure every user that is interacting with the
    platform have their profile picture and biography"""
    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'),
                                            reverse('users:logout')]:
                        return redirect('users:update_profile')

        response = self.get_response(request)
        return response
