from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Link(models.Model):
    Status = (
        (1, "正常"),
        (0, "删除"),
    )
    title = models.CharField(max_length=100, verbose_name="标题")
    href = models.URLField(verbose_name="链接")
    status = models.IntegerField(choices=Status, default=1)
    weight = models.PositiveIntegerField(
        default=1, choices=zip(range(1, 6), range(1, 6)), verbose_name="权重"
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name


class SideBar(models.Model):
    Status = (
        (1, "展示"),
        (0, "隐藏"),
    )

    Side_Type = (
        (1, "HTML"),
        (2, "最新文章"),
        (3, "最热文章"),
        (4, "最近评论"),
    )

    title = models.CharField(max_length=50, verbose_name="标题")
    display_type = models.IntegerField(choices=Side_Type, default=1)
    content = models.CharField(max_length=500, blank=True, verbose_name="内容")
    status = models.IntegerField(choices=Status, default=1)
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏 "
