from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def index(request):
    context_dict = {"text":"hello world","number":100}
    return render(request,'basic_app/index.html',context=context_dict)

def other(request):
    content1 = {"hello":"world"}
    return render(request,'basic_app/other.html',context=content1)

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
