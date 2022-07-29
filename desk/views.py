from django.contrib import messages
from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, ListView
from .forms import *
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import *

# Create your views here.
@login_required(login_url='login')
# ----------------------- DASHBOARD ------------------------
def Dashboard(request):
    print("You are:- ", request.session.get('email'))
    return render(request, 'dashboard.html')


# ----------------------- COMPLAIN ------------------------
def Complain_data(request):
    cm = Complain.objects.all()
    return render(request, 'complain.html', {'cm': cm})


# @login_required(login_url='login')
# class ListSecretCodes(LoginRequiredMixin, ListView):
#     model = Insert_complain

def Aboutus(request):
    return render(request, 'about.html')

class Insert_complain(LoginRequiredMixin, SuccessMessageMixin, FormView):
    model = Complain
    form_class = ComplainForm
    template_name = 'insert_complain.html'
    success_url = "insert_complain"
    success_message = "Your Complain Submitted Successfully...!!"

    def get_initial(self):
        return {'std_id': self.request.user}

    def form_invalid(self, form):
        return super().form_invalid(form)    

    def form_valid(self, form):
        form.save()
        return redirect('insert_complain')


def Delete_complain(request, id):
    complain = Complain.objects.get(id=id)
    complain.delete()
    return redirect('complain')


# ----------------------- STUDENT ------------------------

def Student_data(request):
    st = Student.objects.all()
    return render(request, 'student.html', {'st': st})


class Insert_student(SuccessMessageMixin, FormView):
    model = Student
    form_class = StudentForm
    fields = "__all__"
    template_name = 'insert_student.html'
    success_url = 'login'
    success_message = 'Account Created Successfully'

    def form_valid(self, form):
        form.save()
        return redirect('login')


# ----------------------- FEEDBACK ------------------------
class Insert_feedback(SuccessMessageMixin, FormView):
    model = Feedback
    form_class = FeedbackForm
    fields = "__all__"
    template_name = 'insert_feedback.html'
    success_url = 'insert_feedback'
    success_message = "Your Feedback Submitted..!!"

    def get_initial(self):
        return {'std_id': self.request.user}

    def form_valid(self, form):
        form.save()
        return redirect('insert_feedback')


def Feed_data(request):
    fd = Feedback.objects.all()
    return render(request, 'feedback.html', {'fd': fd})


def Delete_feedback(request, id):
    feed = Feedback.objects.get(id=id)
    feed.delete()
    return redirect('feedback')


# ----------------------- ACCOUNT ------------------------


def Signup(request):
    form = Signupform(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        join = form.cleaned_data['joindate']
        end = form.cleaned_data['enddate']
        user.set_password(password)
        user.save()
        return redirect("login")
    context = {
        'form': form
    }
    return render(request, 'signup.html',{'context':context})
    # else:
    #     return HttpResponse("404 Not Found")


def Login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':    
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('validate')
        else:
            return HttpResponse("Login Failed")
    return render(request, 'login.html')

def validate(request):
    user = User.objects.get(id = request.user.id)
    today = datetime.date.today()
    end = user.enddate
    if end == today:
        logout(request)
        return HttpResponse("Your college session has been finished. You can not log in ")
    else:
        return redirect('dashboard')


def Logout(request):
    logout(request)
    return redirect('login')


# ----------------------- ADMIN ------------------------
def AdminSide(request):
    return render(request, 'admin.html')
