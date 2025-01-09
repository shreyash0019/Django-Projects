from django.shortcuts import render
from testapp.forms import FeedbackForm
# Create your views here.
def feedback_view(request):
    form = FeedbackForm()
    return render (request, "testapp/feed.html", {'form': form })