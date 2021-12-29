from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
	users = User.objects.exclude(username='pi')

	for i in range(0, 10):
		profiles = []

		for j in range(0, 1000):
			users.append(User(username=f'Victor{i * 1000 + j}', email=f'jleon{i * 1000 + j}@beatles.com', password='glass onion'))

		User.objects.bulk_create(users)

		print(f'[{i+1}/10] done')

	def handle(self, *args, **options):
		return 0
