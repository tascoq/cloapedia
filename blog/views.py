from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import PostCreateForm
from .models import Post


def main_page(request):
    return render(request, 'blog/index.html')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    form = PostCreateForm()
    return render(request, 'blog/post_create.html',
                  context={'form': form})


@login_required
def user_posts(request):
    posts = Post.objects.filter(author=request.user)
    context = {
        'posts': posts
    }
    return render(request, 'blog/user_posts.html', context)
