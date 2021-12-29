from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import auth
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from app.models import Question, Tag, Profile, Comment
from app.forms import LoginForm, QuestionForm, SignupForm, CommentForm

# Create your views here.

def Pagination(request, data):
	paginator = Paginator(data, 5)
	page = request.GET.get('page')
	return paginator.get_page(page)

def index(request):
	if request.method == 'POST':
		auth.logout(request)

	return render(request, "index.html", {'questions': Pagination(request, Question.objects.new_questions())})

def hot(request):
	return render(request, "hot.html", {'title': 'Hot questions', 'questions': Pagination(request, Question.objects.hype_questions())})

def tag(request, tag):
	return render(request, "hot.html", {'title': f'Questions by tag {tag}', 'questions': Pagination(request, Question.objects.tag_questions(tag))})

@login_required(redirect_field_name='login')
def ask(request):
	if request.method == 'GET':
		q_form = QuestionForm()
	elif request.method == 'POST':
		q_form = QuestionForm(data=request.POST)

		if q_form.is_valid():
			q = Question(title=q_form.cleaned_data['title'], text=q_form.cleaned_data['text'], author_id=request.user.profile.id)
			q.save()

			tags = q_form.cleaned_data['tags'].split(', ')

			for tag in tags:
				tag = tag.lower()

				t = Tag.objects.filter(name=tag)
				if (t.exists()):
					q.tags.add(Tag.objects.get(name=tag))
				else:
					new_tag = Tag(name=tag)
					new_tag.save()

					q.tags.add(new_tag)
			
			return redirect(reverse('question', kwargs={'id': q.id}))

	return render(request, "ask.html", {'form': q_form})

def question(request, id):
	question = Question.objects.get(id=id)

	if request.method == 'GET':
		form = CommentForm()
	elif request.method == 'POST':
		form = CommentForm(data=request.POST)

		if form.is_valid():
			comment = Comment(text=form.cleaned_data['text'], user_id=request.user.profile.id, question_id=form.cleaned_data['question_id'])
			comment.save()

			return redirect(reverse('question', kwargs={'id': form.cleaned_data['question_id']}))
			
	return render(request, "question.html", {'form': form, 'content': question, 'questions': Pagination(request, question.comments.all().order_by('id'))})

def settings(request):
	return render(request, "settings.html")

def signup(request):
	if request.method == 'GET':
		form = SignupForm()
	elif request.method == 'POST':
		form = SignupForm(data=request.POST)

		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
			
			profile = Profile(nickname=form.cleaned_data['nickname'], user=user)
			profile.save()

			log_user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			auth.login(request, log_user)

			return redirect(reverse('index'))

	return render(request, "signup.html", {'form': form})

def login(request):
	if request.method == 'GET':
		form = LoginForm()
	elif request.method == 'POST':
		form = LoginForm(data=request.POST)

		if form.is_valid():
			user = auth.authenticate(**form.cleaned_data)

			if not user:
				form.add_error(None, "User not found")
			else:
				auth.login(request, user)
				return redirect(reverse('index'))

	return render(request, "login.html", {'form': form})