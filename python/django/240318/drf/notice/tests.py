from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from notice.models import Notice


class NoticeTest(TestCase):
    def setUp(self):
        print("-- main app 테스트 BEGIN --")
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="byeong",
            password="qudgjs01!@",
        )
        self.user.save()
        self.notice = Notice.objects.create(
            title="test title",
            content="test content",
            author=self.user,
        )
        self.notice.save()
        print("-- main app 테스트 END --")

    def test_notice_read(self):
        """
        회원이 아닌 사람이 notice를 읽으려 할 때
        notice Read 가능 테스트
        """
        print("-- notice read 테스트 BEGIN --")
        response = self.client.get("/notice/")
        self.assertEqual(response.status_code, 200)
        print("-- notice read 테스트 END --")