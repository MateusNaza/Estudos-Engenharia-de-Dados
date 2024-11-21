import hashlib
import json

class Blockchain:
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return  hashlib.sha256(block_string).hexdigest()


block = {
    'index': 1,
    'timestamp': 1633024800,
    'transactions': [{'sender': 'Alice', 'recipient': 'Bob', 'amount': 50}],
    'proof': 100,
    'previous_hash': '1'
}

# Calculando o hash do bloco
block_hash = Blockchain.hash(block)
print(f'\nHash do bloco: {block_hash}\n\
Transações: {block["transactions"]}\n\n')



