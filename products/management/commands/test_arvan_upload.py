from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

class Command(BaseCommand):
    help = 'Test Upload to Arvan Cloud'

    def handle(self, *args, **kwargs):
        file_content = ContentFile(b'This is a test file for Arvan Cloud.')
        file_name = 'test-folder/arvan_test_file.txt'

        saved_path = default_storage.save(file_name, file_content)
        file_url = default_storage.url(saved_path)

        self.stdout.write(self.style.SUCCESS(f'File uploaded successfully: {file_url}'))
