from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from blog.models import Post


class BlogTest(TestCase):
    def setUp(self):
        print("-- main app 테스트 BEGIN --")
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="byeong",
            password="qudgjs01!@",
        )
        self.user.save()
        self.blog = Post.objects.create(
            title="test blog title",
            content="test blog content",
            author=self.user,
        )
        self.blog.save()
        print("-- main app 테스트 END --")

    def test_blog_read(self):
        """
        회원이 아닌 사람이 blog를 읽으려 할 때
        blog Read 가능 테스트
        """
        print("-- blog read 테스트 BEGIN --")
        response = self.client.get("/blog/post/")
        self.assertEqual(response.status_code, 403)
        print("-- blog read 테스트 END --")