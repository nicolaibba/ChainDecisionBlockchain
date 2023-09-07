from django.shortcuts import render, redirect
import datetime
import hashlib
import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.response import Response
from rest_framework import status

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(nonce = 1, previous_hash = '0', message=None)

    def create_block(self, nonce, previous_hash, message):
        block = {
                'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'nonce': nonce,
                 'previous_hash': previous_hash,
                 'message': message
                 }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_nonce):
        new_nonce = 1
        check_nonce = False
        while check_nonce is False:
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nonce = True
            else:
                new_nonce += 1
        return new_nonce

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_nonce = previous_block['nonce']
            nonce = block['nonce']
            hash_operation = hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    
blockchain = Blockchain()


class MineBlock(APIView):
    def get(self, request):
        # Get the latest block from your blockchain
        latest_block = blockchain.get_previous_block()
        
        # Your mining logic here (if any)

        # Construct a response dictionary
        response_data = {
            'message': 'Congratulations, you just mined a block!',
            'index': latest_block['index'],
            'timestamp': latest_block['timestamp'],
            'nonce': latest_block['nonce'],
            'previous_hash': latest_block['previous_hash']
        }
        # Return the response using DRF's Response class
        return Response(response_data, status=status.HTTP_200_OK)

class MainView(View):
    
    template_name = 'PyChain/index.html'

    def get(self, request, *args, **kwargs):
        latest_block = blockchain.get_previous_block()
        print(latest_block)
        print(len(blockchain.chain))
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        
        message = request.POST.get('message', None)
        if message:
            latest_block = blockchain.get_previous_block()
            nonce = latest_block['nonce']
            new_nonce = blockchain.proof_of_work(nonce)
            block_hash = blockchain.hash(latest_block)
            new_block = blockchain.create_block(new_nonce, block_hash, message)
            
        # return render(request, self.template_name)
        return redirect('homepage')


class GetChain(APIView):
    def get(self, request):
        # Your get_chain logic here
        # Construct a response dictionary
        response_data = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain)
        }
        # Return the response using DRF's Response class
        return Response(response_data, status=status.HTTP_200_OK)

class IsValid(APIView):
    def get(self, request):
        # Your is_valid logic here
        is_valid = blockchain.is_chain_valid(blockchain.chain)
        if is_valid:
            response_data = {'message': 'All good. The Blockchain is valid.'}
        else:
            response_data = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
        # Return the response using DRF's Response class
        return Response(response_data, status=status.HTTP_200_OK)
