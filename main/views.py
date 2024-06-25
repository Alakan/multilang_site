from django.shortcuts import render
from .models import BlogArticle
import openai
# Create your views here.

def article_list(request):
    articles = BlogArticle.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})



def chatbot(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return render(request, 'main/chatbot.html', {'answer': answer})
    return render(request, 'main/chatbot.html')
