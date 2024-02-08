from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings                                                                                                                                                      
from django.http import HttpResponse
# Create your views here.


def index(request):
    account_sid = 'your_twilio_account_sid'
    auth_token = 'your_twilio_auth_token'
    twilio_phone_number = 'your_twilio_phone_number'

    if request.method == "POST":
        s_name = request.POST['f_name']       
        r_name = request.POST['l_name']       
        age = request.POST['age']       
        phone = request.POST['phone']       
        msg = request.POST['message']       
        message_to_broadcast = f'Hello {r_name}!, I am {s_name}. I am {age} years old. {msg}'
        print(message_to_broadcast)
        
        # client = Client(account_sid, auth_token)
        
        # client.messages.create(to=phone,
        #                     from_=twilio_phone_number,
        #                     body=message_to_broadcast)

    
    return render(request, 'bulk_sms/index.html')