from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from app.models import Profile, Question, Tag
import random

class Command(BaseCommand):
	# tagss = Tag.objects.all()
	profiles = Profile.objects.all()

	for i in range(0, 100):
		que = []
    
		for j in range(0, 1000):
			user = profiles[random.randint(0, 9999)]
			tmp = Question(author=user, title=f'{user.nickname} ask you', text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
			# tmp.tags.add(tagss[random.randint(3334, 6666)], tagss[random.randint(0, 3333)], tagss[random.randint(6667, 9999)])
			que.append(tmp)

		Question.objects.bulk_create(que)

		print(f'[{i+1}/10] done')

	def handle(self, *args, **options):
		return 0
