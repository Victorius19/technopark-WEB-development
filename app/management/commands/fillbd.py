from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from app.models import Profile

class Command(BaseCommand):
	users = User.objects.exclude(username='pi')

	for i in range(0, 10):
		profiles = []

		#for j in range(0, 1000):
		#	users.append(User(username=f'Victor{i * 1000 + j}', email=f'jleon{i * 1000 + j}@beatles.com', password='glass onion'))

		#User.objects.bulk_create(users)

		for j in range(0, 1000):
			profiles.append(Profile(user=users[i * 1000 + j], nickname=f'Victorius{i * 1000 + j}'))

		Profile.objects.bulk_create(profiles)

		print(f'[{i+1}/10] done')

	def handle(self, *args, **options):
		return 0
