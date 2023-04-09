from django.shortcuts import render
from polls.models import Question
from django.template import loader
# Create your views here.
from django.http import HttpResponse


def index(request):
    questions = Question.objects.order_by("-pub_date")[:5]
    page = loader.get_template("polls/index.html")
    context = {
        "questions": questions
    }
    return HttpResponse(page.render(context, request))


def details(requesr, question_id):
    questions = Question.objects.order_by("-pub_date")[:5]

    somedata = ", ".join([q.question_text for q in questions])

    return HttpResponse("You're looking at details of %s." % somedata)


def results(request, question_id):
    response = "you're looking at the result of %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
