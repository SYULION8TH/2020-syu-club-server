from django.db import models

class Qna(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

class Qna_Comment(models.Model):
    body = models.TextField()
    qna = models.ForeignKey('Qna', on_delete=models.CASCADE, related_name="QnaComments")
