from django.shortcuts import render

# Create your views here.
def test(request, value):
    context = {
        'value': value,
    }
    return render(request, 'test.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    context = {
        'something': request.GET.get('something'),
    }
    return render(request, 'catch.html', context)