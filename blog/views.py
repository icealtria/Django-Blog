from django.http import HttpResponse
from django.shortcuts import render

from .models import Tag, Post, Category


# Create your views here.
def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)

    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.objects.filter(status=Post.STATUS_PUBLISHED)

    context = {"post_list": post_list, "tag": tag, "category": category}

    return render(request, "blog/list.html", context=context)


def post_detail(request, post_id):
    # content = "post_detail post_id=%s" % (post_id)
    # return HttpResponse(content)
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    return render(request, "blog/detail.html", context={"post": post})


def links(request):
    return HttpResponse("links")
