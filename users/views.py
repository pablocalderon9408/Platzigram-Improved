# Django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic import DetailView, FormView

# Models
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from posts.models import Post

# Forms
from users.forms import ProfileForm, SignupForm
from users.models import Profile


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view"""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Profile update"""
    context_object_name = 'profile'
    fields = ['website', 'biography', 'phone_number', 'picture']
    model = Profile
    template_name = 'users/update_profile.html'

    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile"""
        import ipdb; ipdb.set_trace()
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


# @login_required
# def update_profile(request):
#     """Update a user's profile view."""
#     profile = request.user.profile

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data
#             profile.website = data['website']
#             profile.phone_number = data['phone_number']
#             profile.biography = data['biography']
#             if data['picture'] is None:
#                 profile.picture = request.user.profile.picture
#             else:
#                 profile.picture = data['picture']
#             profile.save()
#             url = reverse(
#                 'users:detail',
#                 kwargs={'username': request.user.username}
#                 )
#             return redirect(url)

#     else:
#         form = ProfileForm()

#     return render(
#         request=request,
#         template_name='users/update_profile.html',
#         context={
#             'profile': profile,
#             'user': request.user,
#             'form': form
#         }
#     )

class Signin(LoginView):
    """Login view"""

    template_name = 'users/login.html'
    success_url = reverse_lazy('posts:Feed')


# def login_view(request):
#     """Login view"""
#     if request.method == "POST":
#         print('*'*10)
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         print(username, ":", password)
#         if user:
#             login(request, user)
#             return redirect('posts:Feed')
#         else:
#             return render(request, 'users/login.html',
#                           {'error': 'Invalid username or password'})
#     return render(request, 'users/login.html')


class SignupView(FormView):
    """Sign up view"""

    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# def signup(request):

#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#     else:
#         form = SignupForm()
#     return render(
#         request=request,
#         template_name='users/signup.html',
#         context={'form': form}
#     )


class Logout(LogoutView):
    """Logout view"""

    template_name = 'users/login.html'


# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('users:login')
