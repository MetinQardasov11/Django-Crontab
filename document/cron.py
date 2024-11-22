from .models import Test, Document
from datetime import datetime

def my_scheduled_job():
    Test.objects.create(name='Test')
    
    
def document_expired_check():
    today = datetime.today().date().strftime('%Y-%m-%d')
    qs = Document.objects.filter(expired=False)
    
    for doc in qs:
        exp = doc.expiration_date.strftime('%Y-%m-%d')
        if exp < today:
            doc.expired = True
            doc.save()