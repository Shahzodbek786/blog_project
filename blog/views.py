from django.http import Http404
from django.shortcuts import render, get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Blog


# def blogListview(request):
#     blogs = Blog.objects.all()
#
#     context = {
#         'blogs': blogs,
#     }
#     return render(request, "home.html", context=context)
#
#
# def blogdetailview(request, id):
#     blog = get_object_or_404(Blog, id=id)
#     context = {
#         'blog': blog,
#     }
#
#     return render(request, 'blog_detail.html', context=context)

class BlogListView(ListView):
    model = Blog
    template_name = "home.html"
    context_object_name = "blogs"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"