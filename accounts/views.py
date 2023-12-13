from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login , logout , get_user_model
from . form import RegisterCustomerForm
from django.contrib.auth.views import PasswordChangeView , PasswordChangeDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

User = get_user_model()

def register_customer(request):
    if request.method=='POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.is_customer = True
            var.username = var.email
            var.save()
            messages.success(request, ' Your account have been succesfully registered . Please login to continue')
            return redirect('login')
        else:
            messages.warning(request , 'Something went wrong . Please check form inputs')
            return redirect('register-customer')
    else:
        form = RegisterCustomerForm()
        context = {'form' : form}
        return render(request, 'accounts/register_customer.html' , context)

#login a user

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, 'Login Successful')
            return redirect('dashboard')
        else:
            # Check specifically for incorrect username or password
            if user is None:
                messages.warning(request, 'Incorrect username. Please check your username and try again.')
            else:
                messages.warning(request, 'Incorrect password. Please check your password and try again.')

            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


#logout a user
def logout_user(request):
    logout(request)
    messages.success(request , 'Your session has ended please login again')
    return redirect('login')

class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('dashboard')
    success_message = _("Your password was changed successfully.")

class YourCustomPasswordChangeDoneView(SuccessMessageMixin, PasswordChangeDoneView):
    success_message = _("Your password was changed successfully.")
    success_url = reverse_lazy('dashboard')
    

