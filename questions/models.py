from django.db import models
from users.models import MyUser

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length = 100 , default = "")
    text = models.TextField(max_length = 1024 , default = '')
    create_on = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(MyUser , related_name = 'question_created')
    upvoted_by = models.ManyToManyField(MyUser , related_name = 'question_upvoted' , blank = True , null = True)
    def __str__(self):
        return self.title
