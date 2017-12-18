from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list': latest_question_list}
#     return HttpResponse(template.render(context, request))


def index(request):
    heading_0 = dict(title='Data Munging',
                     blurb="""Spend less time formatting and cleaning your data, and more time
                     building your application! We clean up messy data sets and provide you with
                     an API endpoint for easy integration into your application."""
                     )
    heading_1 = dict(title='Data Streaming',
                     blurb="""We provide up-to-date live data sources from non-traditional data
                     sources. If there is a data source you would like, let us know and we will
                     provide you with an API endpoint."""
                     )
    heading_2 = dict(title='Simple Integration',
                     blurb="""All programming languages are supported via the REST API. Built in
                     support for Python is coming soon! Documentation on how to use this is free
                     and open source."""
                     )

    company = dict(name='Data North',
                   vision='Data for Humans.  Coming soon!'
                   )

    context = dict(company=company,
                   heading=[heading_0, heading_1, heading_2])

    return render(request, 'marketing/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'marketing/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
