import pandas as pd
import random
from .blockchain import Blockchain
from .custom_functions import rndTimeStamp_hourly
from copy import deepcopy

LOW = 38
HIGH = 45




# timestamps = rndTimeStamp_hourly(2023, 10)
# print(timestamps)
def create_blockchain(duration, nodes, daily_readings):
    df = pd.DataFrame(columns = ['block_index', 'block_timestamp', 'nonce', 'previous_block_hash', 'node', 'temp', 'trans_timestamp'])
    init_timestamp = rndTimeStamp_hourly(2023, 0, 1)

    blockchain = Blockchain(init_timestamp = init_timestamp)


    for day in range(duration):
        timestamp = rndTimeStamp_hourly(2023, day, 1)[0]
        new_block = blockchain.add_new_block(timestamp)
        block_list = blockchain.block_to_list(new_block)
        
        for node in range(nodes):
            timestamps = rndTimeStamp_hourly(2023, day, daily_readings) #Generates # timestamps for that day
            for timestamp in timestamps:
                temp = int(random.uniform(LOW, HIGH))
                new_block['transactions'].append(
                    {
                    'node': node,
                    'temp': temp,
                    'timestamp': timestamp
                    }
                )
                trans_list = deepcopy(block_list)
                trans_list.extend([node, temp, timestamp])
                df.loc[len(df)] = trans_list
                
            new_block['last_trans_timestamp'] = timestamp
            

    # return df
    return blockchain
