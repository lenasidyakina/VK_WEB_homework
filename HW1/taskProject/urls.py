"""
URL configuration for taskProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from task1.views import Task1BaseView, Task1IndexView, Task1AskView, Task1QuestionView, Task1LoginView, Task1SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("base/", Task1BaseView.as_view()),
    path("index/", Task1IndexView.as_view()),
    path("question/", Task1QuestionView.as_view()),
    path("ask/", Task1AskView.as_view()),
    path("login/", Task1LoginView.as_view()),
    path("signup/", Task1SignupView.as_view()),

]
