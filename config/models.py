from django.db import models
from django.contrib.auth.models import User

from django.template.loader import render_to_string
# Create your models here.


class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0

    Status = (
        (1, "正常"),
        (0, "删除"),
    )
    title = models.CharField(max_length=100, verbose_name="标题")
    href = models.URLField(verbose_name="链接")
    link_status = models.IntegerField(choices=Status, default=1)
    weight = models.PositiveIntegerField(
        default=1, choices=zip(range(1, 6), range(1, 6)), verbose_name="权重"
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name


class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0

    Status = (
        (STATUS_SHOW, "展示"),
        (STATUS_HIDE, "隐藏"),
    )

    DISPLAY_HTML = 1
    DISPLAY_LATEST = 2
    DISPLAY_HOT = 3
    DISPLAY_COMMENT = 4

    Side_Type = (
        (DISPLAY_HTML, "HTML"),
        (DISPLAY_LATEST, "最新文章"),
        (DISPLAY_HOT, "最热文章"),
        (DISPLAY_COMMENT, "最近评论"),
    )

    title = models.CharField(max_length=50, verbose_name="标题")
    display_type = models.IntegerField(choices=Side_Type, default=1)
    content = models.CharField(max_length=500, blank=True, verbose_name="内容")
    sidebar_status = models.IntegerField(choices=Status, default=1)
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏 "

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=cls.STATUS_SHOW)

    @property
    def content_html(self):
        from blog.models import Post
        from comment.models import Comment

        result = ""

        if self.display_type == self.DISPLAY_HTML:
            result = self.content
        elif self.display_type == self.DISPLAY_LATEST:
            context = {
                "posts": Post.latest_posts(),
            }
            result = render_to_string("config/blocks/sidebar_posts.html", context)
        elif self.display_type == self.DISPLAY_HOT:
            context = {
                "posts": Post.most_popular(),
            }
            result = render_to_string("config/blocks/sidebar_posts.html", context)
        elif self.display_type == self.DISPLAY_COMMENT:
            context = {
                "comments": Comment.objects.filter(status=Comment.STATUS_NORMAL),
            }
            result = render_to_string("config/blocks/sidebar_comments.html", context)
        return result


class Nav(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0

    Status = (
        (STATUS_SHOW, "展示"),
        (STATUS_HIDE, "隐藏"),
    )

    title = models.CharField(max_length=50, verbose_name="标题")
    link = models.URLField(verbose_name="链接")
    nav_status = models.IntegerField(choices=Status, default=1)

    class Meta:
        verbose_name = "导航"
        verbose_name_plural = verbose_name

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=cls.STATUS_SHOW)
