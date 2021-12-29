from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
	def new_questions(self):
		return self.all().order_by('-id')

	def hype_questions(self):
		return self.all().order_by('-rate')

	def tag_questions(self, tag):
		try:
			return self.all().filter(tags__in=[Tag.objects.get(name=tag)]).order_by('-id')
		except:
			return []

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nickname = models.CharField(max_length=256, unique=True)
	image = models.FileField(upload_to=None, blank=True, null=True)

	def __str__(self):
		return self.nickname

class Question(models.Model):
	title = models.CharField(max_length=128)
	text = models.TextField(max_length=2048)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='questions')
	rate = models.IntegerField(default=0)
	tags = models.ManyToManyField('Tag', related_name='questions')

	objects = QuestionManager()

	def __str__(self):
		return self.title

class Tag(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
    	return self.name

class Comment(models.Model):
	text = models.TextField(max_length=2048)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
	rate = models.IntegerField(default=0)
	correct = models.BooleanField(default=False)
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments', blank=True, null=True, default='')

	def __str__(self):
		return self.text

class Like(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='rates', blank=True, null=True, default='')
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='rates', blank=True, null=True, default='')
	is_like = models.BooleanField(default=True)
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rates', blank=True, null=True, default='')

	def __str__(self):
		return "like"