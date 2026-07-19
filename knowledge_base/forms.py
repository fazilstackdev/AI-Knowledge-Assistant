import attrs
from django import forms
from.models import Document

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=['title','pdf_file']
        widgets={
            "title": forms.TextInput(attrs={"placeholder":'Enter document title'}),
        }
        
        
        
        
        
        
        
class QuestionForm(forms.Form):

    document = forms.ModelChoiceField(
        queryset=Document.objects.all()
    )

    question = forms.CharField(
        widget=forms.Textarea()
    )
            