from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
	templates = 'posts/index.html'
	posts = Post.objects.order_by('-pub_date')[:10]
	context = {
		'posts': posts
	}
	return render(request, templates, context)

def group_posts(request, slug):
	templates = 'posts/group_list.html'
	group = get_object_or_404(Group, slug = slug)
	posts = Post.objects.filter(group = group).order_by('-pub_date')[:10]
	context = {
		'groups': group,
		'posts': posts
	}
	return render(request, templates)
