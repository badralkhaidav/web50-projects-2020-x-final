from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from bs4 import BeautifulSoup
import requests
from ipware import get_client_ip

from .models import Order, Transfer_Order

# Create your views here.
def index(request):
    return render(request, "index.html")

def order(request):

    return render(request, "order.html")

def result(request):
    product_link=request.POST["product_link1"]
    price = request.POST["price1"]
    type= request.POST["type1"]
    amount= int(request.POST["amount1"])
    colour = request.POST["colour1"]
    size_description = request.POST["size_description1"]

    order = Order(product_link=product_link, price =price, type=type, colour=colour, size_description=size_description )

    order.save()


    return render(request,"about.html")

def check(request):

     return render(request, "check.html")

def order_result(request):
    order_id = request.POST["order_id"]
    context = {
        "order": Order.objects.get(id=order_id)
    }


    return render(request, "order_result.html", context)


def transfer_index(request):

    return render(request, "transfer_index.html")


rate = "GBP"
rate1 = "GBP"
i= 0

def transfer_order(request):
    #TDB Bank rate getting part
    html_content = requests.get("https://www.tdbm.mn/script.php?mod=rate&ln=mn").text
    soup = BeautifulSoup(html_content, "lxml")

    for tag in soup.find_all("td"):

        global i
        i+=1
        if i == 26:
            global rate
            rate = tag.text
        if i == 27:
            global rate1
            rate1 = tag.text

    # end TDB Bank rate getting part


    context = {
        "rate1" : rate1,
        "rate" : rate
    }
    return render(request, "transfer_order.html", context)

gbp_amount = "0"
mnt_amount = "0"
directionName = "0"
def transfer_result(request):
    # insert into database bill of order
    direction = request.POST.get("direction")
    global gbp_amount
    global mnt_amount
    global directionName

    gbpToMntDailyRate = request.POST["rate"]
    fee = request.POST.get("fee")

    reciever_name = request.POST.get("reciever_name")
    reciever_telephone = request.POST.get("reciever_telephone")
    reciever_email = request.POST.get("reciever_email")
    reciever_register = request.POST.get("reciever_register")
    reciever_bank = request.POST.get("reciever_bank")
    reciever_account=request.POST.get("reciever_account")

    sender_name = request.POST.get("sender_name")
    sender_telephone= request.POST.get("sender_telephone")
    sender_email=request.POST.get("sender_email")
    sender_postcode=request.POST.get("sender_postcode")
    ip = get_client_ip(request)

    #direction = '1'
    if direction == '1':
        directionName = "UKtoMGL"
        gbp_amount = request.POST["sending_amount"]

        mnt_amount = request.POST["receiving_amount"]


    elif direction == '2':
        directionName = "MGLtoUK"
        gbp_amount = request.POST.get("receiving_amount")

        mnt_amount = request.POST["sending_amount"]


    transfer_order=Transfer_Order(ip=ip,fee=fee,sender_postcode=sender_postcode,sender_email=sender_email,sender_telephone=sender_telephone,sender_name=sender_name,reciever_account=reciever_account,reciever_bank=reciever_bank,reciever_register=reciever_register,reciever_telephone=reciever_telephone,reciever_email=reciever_email,reciever_name=reciever_name,direction=direction,directionName=directionName,gbp_amount=gbp_amount ,gbpToMntDailyRate=gbpToMntDailyRate,mnt_amount=mnt_amount)
    transfer_order.save()
    #insert into GBP account

    # insert into GBP Fee account

    # insert into MNT account

    # insert into MNT fee account



    return render(request,"about.html")

def transfer_check(request):

     return render(request, "transfer_check.html")

def transfer_result_result(request):
    id = request.POST["id"]
    context = {
        "order": Transfer_Order.objects.get(id=id)
    }
    return render(request, "transfer_result.html", context)
