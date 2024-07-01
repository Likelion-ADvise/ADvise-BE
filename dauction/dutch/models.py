from django.db import models

#게시물 model
class Ad(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    minimum_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

#댓글 model
class Proposal(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='proposals')
    identifier = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.URLField()
    info = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)