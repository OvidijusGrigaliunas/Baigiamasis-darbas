from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User_Data, Record, Category
from .forms import RecordForm
from django.utils import timezone


# Create your views here.
def index(request):
    current_user = request.user
    records = Record.objects.select_related('category').filter(user=current_user.id).order_by('category')
    context = {'current_user': current_user, 'records': records}
    return render(request, 'user_data/index.html', context)


def submit_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            cur_user = User_Data.objects.get(id=request.user.id)
            selected_category = Category.objects.get(id=form.cleaned_data['category'])
            new_record = Record(user=cur_user, category=selected_category, record_value=form.cleaned_data['value'],
                                record_date=timezone.now())
            new_record.save();
            return HttpResponseRedirect('/thanks/')
    else:
        form = RecordForm()
    return render(request, 'user_data/submit_record.html', {'form': form})
