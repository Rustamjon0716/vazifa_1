# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def all_questions(request):
    return HttpResponse("all questions")

def detail(request,question_id):
    try:
        question  = Question.objects.get(id=question_id)

        return HttpResponse(f"id:{question.id}, question_text:{question.question_text},pub_date:{question.pub_date} ")
    except Question.DoesNotExist:
        return  HttpResponse(f"{question_id} not found")