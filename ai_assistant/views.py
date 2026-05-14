from django.shortcuts import render
import json
import google.generativeai as genai

from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')


@login_required
@require_POST
def ai_chat(request):

    try:

        data = json.loads(request.body)

        user_message = data.get('message')

        prompt = f"""
        You are an AI career assistant for JobPortal.

        Help users with:
        - career advice
        - CV tips
        - interview preparation
        - programming learning roadmap
        - job recommendations

        Keep answers concise and professional.

        User message:
        {user_message}
        """

        response = model.generate_content(prompt)

        return JsonResponse({
            'response': response.text
        })

    except Exception as e:

        return JsonResponse({
            'error': str(e)
        }, status=500)