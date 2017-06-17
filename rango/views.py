from django.shortcuts import render

from django.http import HttpResponse

def index(request):
        context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}
        return render(request,'index.html', context=context_dict)
def home(home):
        return HttpResponse("Home...!")
def about(about):
        return HttpResponse("About!<p> <a href='../rango/'>index</a>")