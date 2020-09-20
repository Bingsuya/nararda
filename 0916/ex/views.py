from django.shortcuts import render,redirect, get_object_or_404 
from .models import employee, Nara
# Create your views here.
def refresh(request):
    mem = Nara.objects.all()
    return render(request, 'refresh.html', {'mem':mem})

def profile_detail(request, pk):
    mem = get_object_or_404(Nara, pk = pk)
    mem.today = mem.today +1
    mem.total = mem.total +1
    mem.save()
    
    return render(request, 'profile_detail.html',{'mem':mem})

