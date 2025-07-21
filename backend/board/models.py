from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('free', '자유'),
        ('diary', '일기'),
        ('activity', '활동'),
        ('2d', '2D'),
        ('3d', '3D'),
        ('android-permission', '앱 권한'),
        ('chatbot', '챗봇'),
        ('classification', '분류'),
        ('flea-market', 'Flea Market'),
        ('green-code', 'Green Code'),
    ]
    
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='free'
    )
    tag = models.CharField(
        max_length=20,
        default='tag1'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_date = models.DateTimeField("date posted")
    update_date = models.DateTimeField("date updated", auto_now=True) # 저장될 때마다 매번 갱신
    
    def __str__(self):
        return self.title