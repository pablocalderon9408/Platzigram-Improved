# Django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import DetailView

# Models
from django.contrib.auth.models import User

# Forms
from users.forms import ProfileForm, SignupForm


class UserDetailView(DetailView):
    """User detail view"""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()


@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            import ipdb; ipdb.set_trace()
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            url = reverse(
                'users:detail',
                kwargs={'username': request.user.username}
                )

            return redirect(url)

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )


def login_view(request):
    """Login view"""
    if request.method == "POST":
        print('*'*10)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(username, ":", password)
        if user:
            login(request, user)
            return redirect('posts:Feed')
        else:
            return render(request, 'users/login.html',
                          {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')


def signup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()
    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')
