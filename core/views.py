from django.shortcuts import render
import meetup.api

# Create your views here.

# Index view
def index(request):
    return render(request, 'core/index.html')