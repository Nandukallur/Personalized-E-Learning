from django.shortcuts import render

# Create your views here.
# views.py
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate
from django.views.generic import TemplateView
from langchain.prompts import PromptTemplate


@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        openai_api_key = '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'
        llm = OpenAI(openai_api_key=openai_api_key, temperature=0.8)

        input_text = request.POST.get('input_text', '')

        if input_text.lower() == 'exit':
            return JsonResponse({'response': 'Thank you for using Chatbot. Have a great day ahead'})

        if input_text.lower() in ['hi', 'hai', 'hello', 'hy']:
            return JsonResponse({'response': 'Hai, Welcome to Chatbot'})

        if input_text.lower() in ['bye', 'by', 'goodbye', 'thank you', 'thanks']:
            return JsonResponse({'response': 'Thank you for using Chatbot. Have a great day ahead.'})

        input_prompt = PromptTemplate(input_variables=['query'], template='IT related {query}')
        chain = LLMChain(llm=llm, prompt=input_prompt, verbose=True)

        return JsonResponse({'response': chain.run(input_text)})
    else:
        return JsonResponse({'response': 'Invalid request'}, status=400)


class ChatBotView(TemplateView):
    template_name = "chatbot.html"
