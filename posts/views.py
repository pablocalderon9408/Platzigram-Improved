from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
import posts

from posts.forms import PostForm
from posts.models import Post

# Create your views here.

from datetime import datetime


# posts = [
#     {
#         'title': 'Mont Blanc',
#         'user': {
#             'name': 'Yésica Cortés',
#             'picture': 'https://picsum.photos/60/60/?image=1027'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/800/600?image=1036',
#     },
#     {
#         'title': 'Via Láctea',
#         'user': {
#             'name': 'Christian Van der Henst',
#             'picture': 'https://picsum.photos/60/60/?image=1005'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/800/800/?image=903',
#     },
#     {
#         'title': 'Nuevo auditorio',
#         'user': {
#             'name': 'Uriel (thespianartist)',
#             'picture': 'https://picsum.photos/60/60/?image=883'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/500/700/?image=1076',
#     }
# ]


class PostFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""

    template_name = 'posts/feed.html'
    queryset = Post.objects.all().order_by('-created')
    paginate_by = 1
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """Shows detail's post"""

    context_object_name = 'post'
    model = Post
    queryset = Post.objects.all()
    slug_field = posts
    slug_url_kwarg = posts
    template_name = 'posts/detail.html'


# @login_required
# def list_posts(request):
#     posts = Post.objects.all().order_by('-created')
#     return render(request, 'posts/feed.html', {'posts': posts})


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a post."""
    context_object_name = 'post'
    form_class = PostForm
    template_name = 'posts/new.html'
    success_url = reverse_lazy('posts:Feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["profile"] = self.request.user.profile
        return context


# @login_required
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:Feed')

#     else:
#         form = PostForm()

#     return render(
#         request=request,
#         template_name='posts/new.html',
#         context={
#             'form': form,
#             'user': request.user,
#             'profile': request.user.profile
#         }
#     )
