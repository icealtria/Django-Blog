from django.test import TestCase

from .models import Category, Post, Tag
from django.contrib.auth.models import User


# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self) -> None:
        owner = User.objects.create_user(
            username="test", password="123456", email="test@qq.com"
        )
        tag = Tag.objects.create(name="Test Tag", owner=owner)
        category = Category.objects.create(name="Test Category", owner=owner)
        self.post = Post.objects.create(
            title="Test Post",
            desc="This is a test post.",
            body="This is the body of the test post.",
            category=category,
            owner=owner,
        )
        self.post.tags.set([tag])

    def test_post(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.desc, "This is a test post.")
        self.assertEqual(self.post.body, "This is the body of the test post.")
