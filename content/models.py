from django.db import models


# Create your models here.
class Feed(models.Model):
    number_data = models.TextField()  # 글내용
    tag = models.TextField()  # 글내용
    image = models.TextField()  # 피드 이미지
    user_id = models.TextField()  # 글쓴이
    like_count = models.IntegerField()  # 좋아요
    upload_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)  # 생성된 날짜와 시간 자동 설정
