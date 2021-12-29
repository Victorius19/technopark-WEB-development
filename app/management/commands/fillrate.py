from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from app.models import Profile, Question, Tag, Comment, Like
import random

class Command(BaseCommand):
	#que = Question.objects.all()
	#profiles = Profile.objects.all()
	count = 0
	for i in range(133, 1000):
		comm = []

		for j in range(0, 1000):
			count += 1
			for l in range(0, 2):
				tmp = Like(user_id=random.randint(0, 9999), comment_id=count)
				# tmp.tags.add(tagss[random.randint(3334, 6666)], tagss[random.randint(0, 3333)], tagss[random.randint(6667, 9999)])
				comm.append(tmp)
		try:
			Like.objects.bulk_create(comm)
		except:
			print("failed")

		print(f'[{i+1}/1000] done')

	def handle(self, *args, **options):
		return 0
