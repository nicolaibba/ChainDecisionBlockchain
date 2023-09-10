import datetime
import hashlib
import json

class Blockchain():
    def __init__(self, init_timestamp):
        self.chain = []
        self.create_block(nonce = 1, previous_hash = '0', timestamp=init_timestamp)

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
    
    def create_block(self, nonce, previous_hash, timestamp):
        
        block = {
                'block_index': len(self.chain),
                 'block_timestamp': timestamp,
                 'nonce': nonce,
                 'previous_block_hash': previous_hash,
                 'last_trans_timestamp': None,
                 'transactions': []
                 }
        self.chain.append(block)
        return block
    
    def add_new_block(self, timestamp):
        previous_block = self.get_previous_block()
        nonce = previous_block['nonce']
        new_nonce = self.proof_of_work(nonce)
        previous_block_hash = self.hash(previous_block)
        new_block = self.create_block(new_nonce, previous_block_hash, timestamp)
        
        return new_block
    
    def block_to_list(self, block):
        return [block['block_index'], block['block_timestamp'], block['nonce'], block['previous_block_hash']]
    
