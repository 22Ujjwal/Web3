class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        
        self.new_block(previous_hash=1, proof=100) # make the genesis block
        
    def new_block(self):
        # make a new block and 
        # adds it to the chain (Build-Link)
        pass
    
    def new_transaction(self):
        # Adds a new transaction to the list of transactions (Stacking)
        pass
    
    @staticmethod
    def hash(block):
        # Hashes a Block, fr fun!
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain, order served!
        pass