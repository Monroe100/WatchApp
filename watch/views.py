from django.shortcuts import render
from django.http import HttpResponse
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# Create your views here.

def welcome(request):
    return HttpResponse('NEIGHBOURHOOD')



    # if request.method == 'POST':
    #     form = NewsLetterForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['your_name']
    #         email = form.cleaned_data['email']

    #         recipient = NewsLetterRecipients(name = name,email =email)
    #         recipient.save()
    #         send_welcome_email(name,email)

    #         HttpResponseRedirect('news_today')
    #         #.................
    # return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})
