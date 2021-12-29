from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from app.models import Profile, Question

# Create your views here.

def Pagination(request, data):
	paginator = Paginator(data, 5)
	page = request.GET.get('page')
	return paginator.get_page(page)

def index(request):
	return render(request, "index.html", {'questions': Pagination(request, Question.objects.new_questions())})

def hot(request):
	return render(request, "hot.html", {'title': 'Hot questions', 'questions': Pagination(request, Question.objects.hype_questions())})

def tag(request, tag):
	return render(request, "hot.html", {'title': f'Questions by tag {tag}', 'questions': Pagination(request, Question.objects.tag_questions(tag))})

def ask(request):
	return render(request, "ask.html", {})

def question(request, id):
	question = Question.objects.get(id=id)

	return render(request, "question.html", {'content': question, 'questions': Pagination(request, question.comments.all().order_by('id'))})

def settings(request):
	return render(request, "settings.html", {})

def signup(request):
	return render(request, "signup.html", {})

def login(request):
	return render(request, "login.html", {})