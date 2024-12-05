from django.shortcuts import render

# Create your views here.
def polls_home_page(req):
    return render(req, 'polls/home.html')