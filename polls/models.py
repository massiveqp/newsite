from django.db import models

# Create your models here.
class Question(models.Model):
	#...
	def __unicode__(self):
		return self.question_text
 	question_text = models.CharField(max_length=200)
 	pub_date = models.DateTimeField('datepublished')

class Choice(models.Model):
	#...
	def __unicode__(self):
		return self.choice_text
 	question = models.ForeignKey(Question)
 	choice_text = models.CharField(max_length=200)
 	votes = models.IntegerField(default=0)
