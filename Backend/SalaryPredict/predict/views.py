from django.shortcuts import render

# Create your views here.

def predict(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'gs.html')
