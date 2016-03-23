from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST,require_http_methods
from .models import Question

# Create your views here.
@require_GET
def display_ques(request):
    context = { "questions" : Question.objects.all()}
    return render(request , "questions/display_questions.html" , context);
