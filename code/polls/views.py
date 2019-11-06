from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404

def index(request):

    question_list = Question.objects.order_by('-pub_date')[:5]
    
    context = {
        'question_list': question_list,
    }

    return render(request, 'polls/index.html', context)

    

def detail(request, id):
    question = get_object_or_404(Question, pk=id)

    context = {
        'question': question,
    }

    return render(request, 'polls/detail.html', context)
    
def result(request, id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % id)

def vote(request, id):
    return HttpResponse("You're voting on question %s." % id)