from typing import Any
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Tag, Post, Category
from config.models import SideBar, Nav, Link

from django.views.generic import DetailView, ListView

from comment.forms import CommentForm
from comment.models import Comment

# Create your views here.
class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sidebars"] = SideBar.get_all()
        context['navs'] = Nav.get_all()
        return context
    
class PostDetailView(CommonViewMixin, DetailView):
    model = Post
    template_name = "blog/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'comment_form': CommentForm,
                'comment_list': Comment.get_by_target(self.request.path)
            }
        )
        return context
    
class IndexView(CommonViewMixin, ListView):
    queryset = Post.objects.filter(status=Post.STATUS_PUBLISHED)
    template_name = "blog/list.html"
    paginate_by = 7
    context_object_name = "post_list"

class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        Category_id = self.kwargs.get("category_id")
        category = get_object_or_404(Category, pk=Category_id)
        context["category"] = category
        return context
        
class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Tag_id = self.kwargs.get("tag_id")
        tag = get_object_or_404(Tag, pk=Tag_id)
        context["tag"] = tag
        return context

class HomeView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SearchView(IndexView):
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(status=Post.STATUS_PUBLISHED).filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )
        else:
            return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_keyword'] = self.request.GET.get('q', '')
        return context
    
class AuthorView(IndexView):
    def get_queryset(self):
        query = super().get_queryset()
        author_id = self.kwargs.get('owner_id')
        return query.filter(owner__id=author_id)
        
# def post_list(request, category_id=None, tag_id=None):
#     tag = None
#     category = None

#     if tag_id:
#         post_list, tag = Post.get_by_tag(tag_id)

#     elif category_id:
#         post_list, category = Post.get_by_category(category_id)
#     else:
#         post_list = Post.objects.filter(status=Post.STATUS_PUBLISHED)

#     context = {"post_list": post_list, "tag": tag, "category": category}

#     return render(request, "blog/list.html", context=context)


# def post_detail(request, post_id):
#     # content = "post_detail post_id=%s" % (post_id)
#     # return HttpResponse(content)
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post = None
#     return render(request, "blog/detail.html", context={"post": post})


def links(request):
    return HttpResponse("links")
