from django.db import models


class Document(models.Model):
    title=models.CharField(max_length=255)
    pdf_file=models.FileField(upload_to='documents/')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
    
    
class ChatHistory(models.Model):
    document=models.ForeignKey(Document,
        on_delete=models.CASCADE
    )
    question=models.TextField()
    answer=models.TextField()
    
    created_at=models.DateTimeField(
        auto_now_add=True
    ) 
    
    def __str__(self):
        return self.question[:50]   
    
    
    
    
    
    