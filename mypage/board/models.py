from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('free', '자유'),
        ('diary', '일기'),
        ('activity', '활동'),
    ]
    
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='free'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_date = models.DateTimeField("date posted")
    update_date = models.DateTimeField("date updated", auto_now=True) # 저장될 때마다 매번 갱신
    
    def __str__(self):
        return self.title