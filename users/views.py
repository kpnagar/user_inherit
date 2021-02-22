from django.shortcuts import render, redirect

from django.urls import reverse_lazy
# from django.views.generic import CreateView
from .forms import CustomUserCreateForm

# class SignUpView(CreateView):
#     form_class = CustomUserCreateForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

def SignUpView(request):
    if request.method == 'POST':
        form_class = CustomUserCreateForm(request.POST)
        if form_class.is_valid():
            form_class.save()
        return redirect('login')
    else:
        form_class = CustomUserCreateForm()
        return render(request, 'signup.html',{'form':form_class})