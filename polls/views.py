from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice.",

        })
    else:
        choice.vote += 1
        choice.save()

        # return render(request, "polls/results.html", {"question" : question})
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
