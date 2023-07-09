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

from blog.views import links
from blog.views import PostDetailView, CategoryView, TagView, HomeView
# from blog.views import post_list, post_detail
urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('admin/', custom_site.urls),
    # path('', post_list),
    path('', HomeView.as_view()),
    path('category/<int:category_id>/', CategoryView.as_view(), name = "category_list"),
    path('tag/<int:tag_id>/', TagView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # path('category/<int:category_id>/', post_list),
    # path('tag/<int:tag_id>/', post_list),
    # path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('links/', links),
]
