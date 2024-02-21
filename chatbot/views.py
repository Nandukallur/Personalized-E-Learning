from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from PyPDF2 import PdfReader
import os

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = "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"

# PDF Paths
pdf_paths = [
    r"C:\Users\shilp\OneDrive\Documents\Luminar\Internship\Personalized_E-Learning\Personalized-E-Learning\HTML.pdf",
    r"C:\Users\shilp\OneDrive\Documents\Luminar\Internship\Personalized_E-Learning\Personalized-E-Learning\PHP.pdf",
    r"C:\Users\shilp\OneDrive\Documents\Luminar\Internship\Personalized_E-Learning\Personalized-E-Learning\python.pdf"
]

# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings()

# Initialize CharacterTextSplitter
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=800, chunk_overlap=200, length_function=len)

# Read PDFs and split text
raw_texts = []
for path in pdf_paths:
    pdf_reader = PdfReader(path)
    raw_text = ''
    for page in pdf_reader.pages:
        content = page.extract_text()
        if content:
            raw_text += content
    raw_texts.append(raw_text)

# Split text
texts = [text_splitter.split_text(raw_text) for raw_text in raw_texts]
flattened_texts = [item for sublist in texts for item in sublist]

# Create FAISS index
document_search = FAISS.from_texts(flattened_texts, embeddings)

# Load Question Answering chain
chain = load_qa_chain(OpenAI(), chain_type="stuff")

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('input_text', '')

        if user_input.lower() == 'exit':
            return JsonResponse({'response': 'Thank you for using Chatbot. Have a great day ahead'})

        if user_input.lower() in ['hi', 'hello', 'hey', 'hy']:
            return JsonResponse({'response': 'Hello, welcome to E-Learning Chatbot. How can I assist you today!'})

        if user_input.lower() in ['bye', 'by', 'thank you', 'thanks']:
            return JsonResponse({'response': 'Bye, and have a good day'})

        question = user_input.strip()
        if len(question) < 4:
            return JsonResponse({'response': 'Please enter a valid question!'})
        
        docs = document_search.similarity_search(user_input)
        bot_response = chain.run(input_documents=docs, question=question)

        return JsonResponse({'response': bot_response})
    else:
        return JsonResponse({'response': 'Invalid request'}, status=400)
    
class ChatBotView(TemplateView):
    template_name = "chatbot.html"
