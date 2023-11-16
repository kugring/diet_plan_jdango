from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.
class User(AbstractBaseUser):
    """
        유저 프러파일 사진
        유저 닉네임  -> 화면에 표기되는 이름
        유저 이름      -> 실제 사용자 이름
        유저 이메일주소 -> 회원가입할때 사용하는 아이디
        유저 비밀번호 ->
    """

    profile_image = models.TextField()  # 프로필 이미지
    nickname = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    # 실제로 사용할 진짜 아이디같은 닉네임을 넣는다.
    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = "User"
