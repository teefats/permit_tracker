from datetime import date, timedelta
from django.shortcuts import render
from .models import Permit
# from .send_email import send_mail
from django.core.mail import send_mail
# Create your views here.
def index(request):
    permit =  Permit.objects.all()
    # for permit in permit:
    #     print(permit.site)
      
    print(type(permit))
    print(permit[1].expiration_date)
    from datetime import date

    date1 = date(2021, 5, 19)
    print(date1)
    print(type(date1))
    
    date2 = permit[1].expiration_date
    timechange = date2 - date1
    print(timechange.days)
    print(type(timechange))
    

    if timechange.days == 1:
        print(timechange)
        send_mail('Permit Reminder', f' Hello your {permit[1]} permit is about to expire', '', [''], html_message='<img src="https://images.unsplash.com/photo-1598281059600-6922066ce5db?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80"><p>Hello</p>')
    
    return render(request, 'permit_tracker/index.html', {'permit':  permit})



