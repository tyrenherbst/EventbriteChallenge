import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('Date Published',default=timezone.now())
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1)<= self.pub_date <= timezone.now()
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean= True
    was_published_recently.short_description = 'Published recently?'

class Results(models.Model):
    category = models.CharField(max_length = 200,default='',null=True)
    name = models.CharField(max_length = 200,default='',null=True)
    eID = models.CharField(max_length = 200,default='',null=True)
    city = models.CharField(max_length = 200,default='',null=True)
    country = models.CharField(max_length = 200,default='',null=True)
    link = models.CharField(max_length = 200,default='',null=True)

    class Meta:
        db_table = 'Results'
 

class Category(models.Model):
    question = models.ForeignKey(Question)
    category_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('Date Published',default=timezone.now())
    cID = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.category_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean= True
    was_published_recently.short_description = 'Published recently?'
