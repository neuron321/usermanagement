from django.shortcuts import redirect, render
from .forms import SignupForm
# Create your views here.
def signup(request):
    print("caught ....")
    if request.method != 'POST':
        form = SignupForm()
    else:
        form = SignupForm(request.POST)
        print(request.POST.values)
        #print(" form is ",form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

def loginUser(request):
    pass
def logoutUser(request):
    pass
