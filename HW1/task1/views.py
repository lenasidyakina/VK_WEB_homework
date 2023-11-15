from django.views.generic import TemplateView

class Task1BaseView(TemplateView):
    template_name = "task1/base.html"

class Task1IndexView(TemplateView):
    template_name = "task1/index.html"

class Task1AskView(TemplateView):
    template_name = "task1/ask.html"

class Task1QuestionView(TemplateView):
    template_name = "task1/question.html"

class Task1LoginView(TemplateView):
    template_name = "task1/login.html"

class Task1SignupView(TemplateView):
    template_name = "task1/signup.html"