from django.test import TestCase

# Create your tests here.
 import User

# Create your models here.

class ProfileManager(models.Manager):
	def create_user(self):
		user = User.objects.create_user(username='john', email='jlennon@beatles.com', password='glass onion')

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
	answers_count = models.IntegerField(default=0)
	tags = models.ManyToManyField('Tag', related_name='questions')

	def __str__(self):
		return self.title

class Tag(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
    	return self.name

class Comment(models.Model):
    text = models.TextField(max_length=2048)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
    	return self.name

class Like(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='rates', blank=True, null=True, default='null')
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='rates', blank=True, null=True, default='null')

	user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rates', blank=True, null=True, default='null')