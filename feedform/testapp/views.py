from django.shortcuts import render
from testapp.forms import FeedBackForm
# Create your views here.
def feedbackform_view(request):
    submitted = False
    sname = ""
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print("Validation Success")
            print("*"*50)
            print("Name:",form.cleaned_data['name'])
            print("Rollno:",form.cleaned_data['rollno'])
            print("Email:",form.cleaned_data['email'])
            print("Feedback:",form.cleaned_data['feedback'])
            sname = form.cleaned_data['name']
            form = FeedBackForm()
            submitted = True
            #sname = form.cleaned_data['name']
    form = FeedBackForm()
    return render(request, 'testapp/feed.html',{'form':form , 'submitted':submitted, 'sname':sname})