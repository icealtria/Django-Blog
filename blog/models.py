from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "分类"


class Tag(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "标签"


class Post(models.Model):
    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 1
    Status = (
        (0, "Draft"),
        (1, "Published"),
    )
    status = models.SmallIntegerField(choices=Status, default=0)

    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    body = models.TextField(blank=True)
    body_html = models.TextField(blank=True,verbose_name="正文html", editable=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    pv = models.PositiveIntegerField(default=1)
    uv = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ["-id"]  # 根據id进行降序排列

    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            post_list = []
        else:
            post_list = tag.post_set.all()
        return post_list, tag

    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            post_list = []
        else:
            post_list = category.post_set.all()
        return post_list, category

    @classmethod
    def most_popular(cls):
        return cls.objects.filter(status=cls.STATUS_PUBLISHED).order_by("-pv")
