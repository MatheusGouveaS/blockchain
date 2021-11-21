from blockchain import Blockchain
from datetime import datetime
from random import uniform

if __name__ == '__main__':
  blockchain = Blockchain()
  
  increment = uniform(0, datetime.utcnow().timestamp())

  blockchain.add_new_block(datetime.utcnow().timestamp() + increment)
  blockchain.add_new_block(datetime.utcnow().timestamp() + increment)
  blockchain.add_new_block(datetime.utcnow().timestamp() + increment)

  print(blockchain.get_all())