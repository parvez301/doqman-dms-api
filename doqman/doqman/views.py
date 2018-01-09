# django libraries
from django.http import HttpResponse

def welcome(request):
  return HttpResponse("Welcome to Doqman Document Management System")
