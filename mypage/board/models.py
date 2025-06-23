from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_date = models.DateTimeField("date posted", auto_now_add=True) # 객체 생성 시간 자동 저장
    update_date = models.DateTimeField("date updated", auto_now=True) # 저장될 때마다 매번 갱신
    
    def __str__(self):
        return self.title