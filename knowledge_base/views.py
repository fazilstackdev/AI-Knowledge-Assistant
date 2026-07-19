from pyexpat.errors import messages

from django.http import HttpResponse
from django.shortcuts import render,redirect

from .embeddings import create_embeddings

from .models import Document

# Create your views here.
from.forms import DocumentUploadForm
from .pdf_utils import extract_text_from_pdf
from.vector_store import store_chunks

from .pdf_utils import extract_text_from_pdf

from .chunking import create_chunks

from .embeddings import create_embeddings

from .vector_store import store_chunks

from .models import ChatHistory



def upload_document(request):

    if request.method == 'POST':

        form = DocumentUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            document = form.save()

            text = extract_text_from_pdf(
                document.pdf_file.path
            )

            chunks = create_chunks(text)

            embeddings = create_embeddings(
                chunks
            )

            store_chunks(
                chunks,
                embeddings,
                document.id
            )

            return redirect(
                'upload_document'
            )

    else:

        form = DocumentUploadForm()

    return render(
        request,
        'knowledge_base/upload.html',
        {
            'form': form
        }
    )
    
    
    
    
from django.http import HttpResponse
from .models import Document
from .pdf_utils import extract_text_from_pdf


def show_pdf_text(request):

    doc = Document.objects.last()

    text = extract_text_from_pdf(
        doc.pdf_file.path
    )

    return HttpResponse(text[:5000])
    
    
    
    

from .chunking import create_chunks


def show_chunks(request):

    doc = Document.objects.last()

    text = extract_text_from_pdf(
        doc.pdf_file.path
    )

    chunks = create_chunks(text)

    result = ""

    for i, chunk in enumerate(chunks):

        result += f"\n\n=== Chunk {i+1} ===\n\n"

        result += chunk

    return HttpResponse(result)         
    
    
    
    
    
from django.http import HttpResponse
from.vector_store import search_chunks

def test_search(request):
    query=request.GET.get('q','')
    if not query:
        return HttpResponse('Use ?q=your question') 
    
           
    
    
    
    results=search_chunks(query)
    output=""
    for chunk in results['documents'][0]:
        output+=chunk
        output+="\n\n"
        output+="="*80
        output+="\n\n"
        
    return HttpResponse(output)
    


    
    
    
from .forms import QuestionForm
from .rag import ask_question


# knowledge_base/views.py
from django.shortcuts import render
from django.contrib import messages
from .forms import QuestionForm
# تابع هوش مصنوعی شما

def ask_ai(request):
    answer = None
    sources = []
    question = None

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            try:
                document = form.cleaned_data["document"]
                question = form.cleaned_data["question"]
                
                # دریافت پاسخ و منابع
                result = ask_question(question, document.id)
                answer = result.get("answer", "پاسخی یافت نشد.")
               
                
                sources = result.get("sources", [])
                ChatHistory.objects.create(document=document,question=question,answer=answer)
                
                if answer:
                    
                    messages.success(request, 'Your response was received successfully.')

                else:
                   
                    messages.warning(request, 'We could not find an answer to your question.')

                    
            except Exception as e:
               
                messages.error(request, f'An error occurred while processing your question: {str(e)}')

        else:
           
            messages.error(request, 'All fields must be filled out correctly.')

    else:
        form = QuestionForm()
    
    history=ChatHistory.objects.order_by("-created_at")
    return render(
        request,
        "knowledge_base/chat.html",
        {
            "form": form,
            "answer": answer,
            "sources": sources,
            "question": question,
              "history": history,
        }
    )