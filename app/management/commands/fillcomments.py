from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from app.models import Profile, Question, QuestionManager, Tag, Comment
import random

class Command(BaseCommand):
	#que = Question.objects.all()
	#profiles = Profile.objects.all()
	que = Question.objects.all().order_by('-id')
	count = 0
	for i in range(0, 1000):
		comm = []

		for j in range(0, 2):
			count += 1
			for l in range(0, 10):
				tmp = Comment(user_id=random.randint(0, 9999), question=que[count], text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since ,.")
				# tmp.tags.add(tagss[random.randint(3334, 6666)], tagss[random.randint(0, 3333)], tagss[random.randint(6667, 9999)])
				comm.append(tmp)
		try:
			Comment.objects.bulk_create(comm)
		except:
			print("failed")

		print(f'[{i+1}/10000] done')

	def handle(self, *args, **options):
		return 0
