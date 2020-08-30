from django.shortcuts import render
from .forms import NewUserForm
from firsthello import views


# Create your views here.

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return views.index(request)
        else:
            print('error form invalid')

    return render(request, 'users.html', {'form': form})
