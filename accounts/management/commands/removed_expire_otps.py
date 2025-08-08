from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime,timedelta


class Command(BaseCommand):
    help = "Remove All Expired Otp Code"
    
    def handle(self, *args, **kwargs):
        expired_time = datetime.now() - timedelta(minutes=2) 
        OtpCode.objects.filter(created__lt=expired_time).delete()
        self.stdout.write("All Expired Otp  Codes Remove")
        