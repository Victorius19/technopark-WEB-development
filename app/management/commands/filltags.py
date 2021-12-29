from django.core.management.base import BaseCommand, CommandError
from app.models import Tag

class Command(BaseCommand):

	for i in range(0, 10):
		tags = []

		for j in range(0, 1000):
			tags.append(Tag(name=f'Python{i * 1000 + j}'))

		Tag.objects.bulk_create(tags)

		print(f'[{i+1}/10] done')

	def handle(self, *args, **options):
		return 0
