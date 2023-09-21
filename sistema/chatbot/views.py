from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
import openai
from .forms import chatbot

# Create your views here.

# Configura la API de OpenAI con tu clave de API
openai.api_key = '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'

def chat(request):
    return render(request, 'chat.html')

@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')

        # Llama a la API de OpenAI para obtener una respuesta
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=input_text,
            max_tokens=50  # Ajusta esto según tus necesidades
        )

        return JsonResponse({'User': input_text},{'response': response.choices[0].text})
    else:
        return JsonResponse({'response': 'Método no permitido'})
