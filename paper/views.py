
from django.shortcuts import render,redirect

from .models import *
from  django.http import HttpResponse
from.forms import QuestionForm
from django.views import View
from django.views.generic import ListView
from django.db.models import Q 
from django.core.mail import send_mail
import mimetypes
import os
from .filters import FilterInformation
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def homepage(request):
    
    return render(request,'pages/homepage.html')
def about(request):
    return render(request,'pages/about.html')   
def user_login(request):
    error=""
    if request.method=='POST':
       u=request.POST['emailid']
       p=request.POST['pwd']
       user= authenticate(emailid=u,pwd=p)
       try:
            if user.is_staff:
               login(request,user)
               error="no"
            else:
               error="yes"
       except:
           error="yes"
    d={'error':error}
    return render(request,'login.html',d)

def signup(request):
    error=''
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        emailid=request.POST['emailid']
        pwd=request.POST['pwd']
        try:
            Signup.objects.create(firstname=firstname,lastname=lastname,emailid=emailid,pwd=pwd)
            error="no"
        except:
            error="yes"
    d={'error':error}

    return render(request,'signup.html',d)
def user_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'homepage.html')

def Logout(request):
        Logout(request)
        return redirect('homepage')
def welcome(request):
    return render(request,'welcome.html')
def index(request):
    program=Department.objects.all()
    d={'program':program}
    return render(request,'index.html',d)
def load_courses(request):
    department_id=request.GET.get('department')
    courses=Course.objects.filter(department_id=department_id).order_by('name')
    return render(request,'courses_dropdown_list_options.html',{'courses':courses})

class HomeView(View):
    def get(self,request):
        form=QuestionForm()
        return render(request,'semester.html',{'form':form})
    def post(self,request):
        form=QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return render(request,'semester.html',{'form':form})
def detail(request):
    item_list=Question.objects.all()
    
    context={
        'item_list':item_list,

    }
    return render(request,'search.html',context)
class search_data(ListView):
    model=Question
    template_name='search.html'

    def get_queryset(self):
        


        query=self.request.GET.get('q')
        return Question.objects.filter(Course__icontains=query)
      
def search_detail(request):
    item_list=Question.objects.all()
    
    context={
        'item_list':item_list,

    }
    return render(request,'search.html',context)  
def SearchInfo(request):
    item=Question.objects.all()
    filters=FilterInformation(request.GET,queryset=item)
    context={'filters':filters}
    return render(request,'pages/search_info.html',context)
def download_pdf_file(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/downloadapp/Files/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'file.html')
@csrf_exempt       
def form(request):
    if request.method=="POST":
        email=request.POST['email']
        message=request.POST['message']
        send_mail(
    '   Queries',
    'message',
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
)
    return render(request,'pages/search_info.html')

def admin_login(request):
    
    error=""
    if request.method=='POST':
       u=request.POST['username']
       p=request.POST['pwd']
       user= authenticate(username=u,password=p)
       try:
            if user.is_staff:
               login(request,user)
               error="no"
            else:
               error="yes"
       except:
           error="yes"
    d={'error':error}
    return render(request,'pages/admin_login.html',d)
def admin_home(request):
    if not request.user.is_staff:
        return redirect('pages/admin_login.html')
    
def logout_admin(request):
    if not request.user.is_staff:
        return redirect('/pages/admin_login.html')
    logout(request)
    return redirect('/admin_homepage.html')
def formdetails(request):
    if request.method=="POST":
       
        name=request.POST.get('name')
        
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        en=Contact(name=name,email=email,subject=subject)
        en.save()
    return render(request,'pages/homepage.html')
