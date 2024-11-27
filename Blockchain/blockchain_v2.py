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
    

    # Aqui é tem a regra do hash e também é gerado o nonce
    def proof_of_work(self):
        last_block = json.dumps(self.chain[-1], sort_keys=True)
        nonce = 0

        while True:
            merge_block_nonce = f"{last_block}{nonce}"
            guess = self.hash(merge_block_nonce)

            if guess.startswith('7777'):
                return guess, nonce
            nonce += 1


    def mine_block(self):
        previous_hash, nonce = self.proof_of_work()
        block = self.new_block(nonce, previous_hash)
        return block
    

    def new_transaction(self, sender, recipient, amount):
        # Aqui será gerado um dicionário para cada transação e colocado na lista de transações
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        # Retorna o índice do bloco onde será armazenada essa transação
        return self.chain[0]
    
# Criando uma instância da Blockchain
bloco = Blockchain()
bloco.new_transaction('Mateus', 'Larissa', 20)
bloco.new_transaction('Mateus', 'Larissa', 1)
bloco.new_transaction('Mateus', 'Larissa', 99)
bloco_1 = bloco.mine_block()
bloco.new_transaction('Bob', 'Larissa', 20)
bloco.new_transaction('Mateus', 'Bob', 1)
bloco.new_transaction('Mateus', 'Bob', 99)
bloco_2 = bloco.mine_block()
bloco_2 = bloco.mine_block()
bloco_4 = bloco.mine_block()


print(json.dumps(bloco.chain, sort_keys=True))
print(f'\n\n\n{bloco.hash('')}')

