from django.db import models
from django.db.models.deletion import CASCADE, PROTECT

# class BlockchainTransactions(models.Model):
#     #The columns must match the Blockchain class and viceversa
#     block_index = models.BigIntegerField(default=None,null=True)
#     block_timestamp = models.CharField(max_length = 255, default=None,null=True)
#     nonce = models.BigIntegerField(default=None,null=True)
#     previous_block_hash = models.CharField(max_length = 255, default=None,null=True)
#     node = models.IntegerField(default=None,null=True)
#     temp = models.IntegerField(default=None,null=True)
#     trans_timestamp = models.CharField(max_length = 255, default=None,null=True)
    
#     def __str__(self):
#         return f"{self.block_index}, {self.node}"
    
class BlockchainTransactions(models.Model):
    #The columns must match the Blockchain class and viceversa
    block_index = models.BigIntegerField(default=None,null=True)
    block_timestamp = models.CharField(max_length = 255, default=None,null=True)
    nonce = models.BigIntegerField(default=None,null=True)
    previous_block_hash = models.CharField(max_length = 255, default=None,null=True)
    last_trans_timestamp = models.CharField(max_length = 255, default=None,null=True)
    transactions = models.JSONField(null=True)
    
    def __str__(self):
        return f"{self.block_index}, {self.block_timestamp}"