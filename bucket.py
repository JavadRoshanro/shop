from django.conf import settings
from boto3.session import Session
import os



class Bucket:
    def __init__(self):
        session = Session(
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
        self.conn = session.client(
            service_name="s3",  # باید اینجا s3 بنویسی نه bucket name
            endpoint_url=settings.AWS_S3_ENDPOINT_URL
        )
        
        
    def get_objects(self):
        result = self.conn.list_objects_v2(Bucket=settings.AWS_STORAGES_BUCKET_NAME)
        if result['KeyCount']:
            return result['Contents']
        else:
            return None
        
    def delete_object(self, key):
        self.conn.delete_object(Bucket=settings.AWS_STORAGES_BUCKET_NAME, Key=key)
        return True
        

    def download_object(self, key):
        file_path = os.path.join(settings.AWS_LOCAL_STORAGES, key)

        # ساخت دایرکتوری مقصد اگر وجود نداشته باشه
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'wb') as f:
            self.conn.download_fileobj(settings.AWS_STORAGES_BUCKET_NAME, key, f)

       
    
bucket = Bucket()