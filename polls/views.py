from django.shortcuts import render, get_object_or_404
from polls.models import Question
from django.template import loader
# Create your views here.
from django.http import HttpResponse, Http404

def index(request):
    questions = Question.objects.order_by("-pub_date")[:5]
    context = {
        "questions": questions
    }
    return render(request, "polls/index.html", context)


def details(request, question_id):
    detail = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"detail": detail})


def results(request, question_id):
    response = "you're looking at the result of %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
