# from django.db import models

# Create your models here.
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    # 자동 날짜 저장
    # created_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # title 수정
    def __str__(self):
        return f'[{self.pk}]{self.title}'
