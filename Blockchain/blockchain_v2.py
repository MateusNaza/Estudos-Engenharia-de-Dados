import hashlib
import json
from time import time

class Blockchain:

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='0', nonce=0)  # Criando o Bloco Gênesis

    # Cria novos blocos
    def new_block(self, nonce, previous_hash):
        block = {
            # Metadados do Bloco
            'index': len(self.chain) + 1,
            'timestamp': time(),

            # Transações
            'transactions': self.current_transactions,

            # Prova de Trabalho
            'previous_hash': previous_hash,
            'nonce': nonce
        }

        # Limpa as transações
        self.current_transactions = []

        # Adiciona o bloco à blockchain
        self.chain.append(block)
        return block

    # Método para gerar os Hashs
    @staticmethod    
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self):
        previous_block = json.dumps(self.chain[-1], indent=4)
        nonce = 0

        while True:
            guess = self.hash(previous_block)
            if guess.startswith('000'):
                return guess
            nonce += 1

    
# Criando uma instância da Blockchain
bloco = Blockchain()

print(bloco.proof_of_work())
