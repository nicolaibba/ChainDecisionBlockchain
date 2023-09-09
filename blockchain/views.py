from django.shortcuts import render, redirect
import datetime
import hashlib
import json
import pandas as pd
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.response import Response
from rest_framework import status

from .create_blockchain import create_blockchain
from .models import BlockchainTransactions

DURATION = 5
NODES = 3
DAILY_READINGS = 2

class MainView(View):
    
    template_name = 'blockchain/index.html'

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        
        BlockchainTransactions.objects.all().delete()
        
        df = create_blockchain(DURATION, NODES, DAILY_READINGS)
        print(df.head())

        # instances = df.apply(lambda row: BlockchainTransactions(**row.to_dict()), axis=1)
        instances = list(df.apply(lambda row: BlockchainTransactions(**row.to_dict()), axis=1))
        # print(instances)
        BlockchainTransactions.objects.bulk_create(instances)
        
        return redirect('homepage')


def block_view(request, id):
    
    transactions = BlockchainTransactions.objects.filter(block_index=id)
    first = list(transactions.values('block_index', 'block_timestamp', 'nonce', 'previous_block_hash'))[0]
    print(first)
    context = {
        'block_info': first,
        'transactions': transactions
    }  
    return render(request, 'blockchain/blockview.html', context=context)