from django.shortcuts import render
import json
import google.generativeai as genai

from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")


@login_required
@require_POST
def ai_chat(request):

    try:

        data = json.loads(request.body)

        message = data.get("message")

        response = model.generate_content(message)

        return JsonResponse({
            "response": response.text
        })

    except Exception as e:

        print("GEMINI ERROR:", e)

        return JsonResponse({
            "error": str(e)
        }, status=500)