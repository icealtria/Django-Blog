"""
URL configuration for blog_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .custom_site import custom_site

from config.views import LinkListView
from blog.views import PostDetailView, CategoryView, TagView, HomeView, SearchView, AuthorView
from comment.views import CommentView
from blog.rss import LatestPostsFeed

from rest_framework.routers import SimpleRouter
from blog.apis import CategoryViewSet, PostViewSet
router = SimpleRouter()
router.register(r'posts', PostViewSet, basename="api-post")
router.register(r'categories', CategoryViewSet, basename="api-category")

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('admin/', custom_site.urls),
    path('', HomeView.as_view()),
    path('category/<int:category_id>/', CategoryView.as_view(), name = "category_list"),
    path('tag/<int:tag_id>/', TagView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('author/<int:owner_id>/', AuthorView.as_view(), name='author'),
    path('links/', LinkListView.as_view(), name='links'),
    path('comment/', CommentView.as_view(), name='comment'),
    path("feed/", LatestPostsFeed(), name="rss"),
    path("api/", include(router.urls)),
    path("api/doc/", include_docs_urls(title="Blog API")),
]
