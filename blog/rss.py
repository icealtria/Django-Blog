from django.contrib.syndication.views import Feed
from django.db.models.base import Model
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed
from .models import Post

class LatestPostsFeed(Feed):
    title = "My blog"
    link = "/blog/"
    description = "New posts of my blog"
    feed_type = Rss201rev2Feed

    def items(self):
        return Post.objects.filter(status=Post.STATUS_PUBLISHED)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.desc
    
    def item_link(self, item: Model) -> str:
        return reverse("post_detail", args=[item.pk])