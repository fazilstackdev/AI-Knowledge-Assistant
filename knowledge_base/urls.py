from django.urls import path
from.import views

urlpatterns = [
    path('',views.upload_document,name='upload_document'),
    path('test-text/',views.show_pdf_text,name="show_pdf_text"),
    path('chunks/',views.show_chunks,name='show_chunks'),
    path('search/',views.test_search,name='test_search'),
    
    path("chat/",views.ask_ai,name="ask_ai"),
    
       
]
