from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from app.models import Profile, Question, Tag
import random

class Command(BaseCommand):
	que = Question.objects.all().order_by('-id')
	tagss = Tag.objects.all()

	for i in range(328, 850):

		for j in range(1, 100):
			try:
				que[i * 100 + j].tags.add(tagss[random.randint(5000, 9999)], tagss[random.randint(0, 4999)])
			except:
				print("failed")

		# Question.objects.bulk_create(que)

		print(f'[{i+1}/850] done')

	def handle(self, *args, **options):
		return 0
