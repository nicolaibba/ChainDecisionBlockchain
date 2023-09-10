from django.shortcuts import render, redirect
import datetime
import time
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
from .blockchain import Blockchain
from .models import BlockchainTransactions

DURATION = 100
NODES = 3
DAILY_READINGS = 24

class MainView(View):
    
    template_name = 'blockchain/index.html'

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        
        BlockchainTransactions.objects.all().delete()
        start = time.time()
        # df = create_blockchain(DURATION, NODES, DAILY_READINGS)
        # print(df.head())
        blocks = create_blockchain(DURATION, NODES, DAILY_READINGS)
        instances = []
        for block in blocks.chain[1:]:
            block['transactions'] = json.dumps(block['transactions'])
            instances.append(BlockchainTransactions(**block))
            
        BlockchainTransactions.objects.bulk_create(instances)
        print(time.time() - start)
        return redirect('homepage')


def block_view(request, id):
    
    block = BlockchainTransactions.objects.filter(block_index=id)
    transactions = json.loads(block[0].transactions)
    block = list(block.values("block_index", "block_timestamp", "nonce", "previous_block_hash", "last_trans_timestamp"))[0]
    context = {
        'block': block,
        'transactions': transactions

    }  
    return render(request, 'blockchain/blockview.html', context=context)