from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Wallet
from .serializers import WalletSerializer
from rest_framework.decorators import api_view 
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
import json

from rest_framework.parsers import JSONParser
import requests


from .forms import WalletForm

# Create Api
@api_view(['POST'])
def create_wallet_api(request):

    try:
        if request.method == 'POST':
            v = dict(request.data)
            v['user'] = int(v['user'][0])  # user id was getting converted to list of string
            api_serializer = WalletSerializer(data=request.data)
            if api_serializer.is_valid():
                if Wallet.objects.filter(user=v["user"]).exists():
                    return JsonResponse({"Mmessage":"User Already Exists"})
                else:
                    api_serializer.save()
                    return Response(api_serializer.data, status=status.HTTP_201_CREATED)
            else:
                print("Not Valid")
            return Response(api_serializer.errors)
    except Exception as e:
        return e

# Create Form 
def create_wallet(request):

    try:
        if request.method == 'POST':
            form = WalletForm(request.POST)
            if form.is_valid():

                request.POST = request.POST.copy()
                request.POST['user'] = request.user.id 
                data = request.POST.dict()

                creation = requests.post('http://127.0.0.1:8000/api/create_wallet_api', data=data)

                return redirect('wallet:create_wallet')
            else:
                print('form is not valid')
        else:
            form= WalletForm()

        return render(request, "walletcreate.html", {'form':form})
    except Exception as e:
        return e

# Fetching User id
def sample_view(request):
    try:
        current_user = request.user
        return HttpResponse(current_user.id)
    except Exception as e:
        return e

# Fetching Current Wallet
def sample_wallet_view(request):
    try:
        user = request.user.id
        current_wallet = Wallet.objects.filter(user=user)
        # print(current_wallet)
        return HttpResponse(current_wallet)
    except Exception as e:
        return e

# Adding Money
@api_view(['PUT'])
def add_money(request,pk):
    try:
        if request.method == 'PUT':
            if type(request.data) != dict:
                ab = json.loads(request.data)
            else:
                ab = request.data

            if "user" in ab:
                pass
            else:
                ab["user"] = pk
            current_wallet = Wallet.objects.filter(user=ab["user"]).first() ## we can use pk
            current_balance = current_wallet.balance

            # request.data['user'] = request.user.id

            ab['balance'] = int(current_balance) + int(ab['balance'])

            walletserializer = WalletSerializer(current_wallet, data=ab)

            if walletserializer.is_valid():

                walletserializer.save()
                return Response(walletserializer.data)
            else:
                print("Serializer not valid")
            return Response(walletserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return e

# Checking Balance
@api_view(['GET'])
def check_balance(request,pk):
    try:
        wallet = Wallet.objects.get(user=pk)

        if request.method == 'GET':
            walletserializer = WalletSerializer(wallet)
            return Response(walletserializer.data)
    except Exception as e:
        return e

# Delete Wallet Api
@api_view(['DELETE'])
def delete_wallet(request,pk):
    try:
        wallet = Wallet.objects.get(user=pk)
        print(wallet)
        if request.method == 'DELETE':
            wallet.delete()
            return redirect('wallet:create_wallet')
    except Exception as e:
        return e

# Withdraw Money
@api_view(['PUT'])
def withdraw_money(request,pk):
    try:
        if request.method == 'PUT':
            if type(request.data) != dict:
                ab = json.loads(request.data)
            else:
                ab = request.data

            if "user" in ab:
                pass
            else:
                ab["user"] = pk
            current_wallet = Wallet.objects.filter(user=ab["user"]).first() ## we can use pk
            current_balance = current_wallet.balance

            # request.data['user'] = request.user.id

            ab['balance'] = int(current_balance) - int(ab['balance'])

            walletserializer = WalletSerializer(current_wallet, data=ab)

            if walletserializer.is_valid():

                walletserializer.save()
                return Response(walletserializer.data)
            else:
                print("Serializer not valid")
            return Response(walletserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return e

