import hashlib
import json
from time import time
from flask import Flask, jsonify, request

class Blockchain:

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', nounce=100)  # Criação do bloco Gênesis

    def new_block(self, nounce, previous_hash=None):
        # Estrutura do bloco
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'nounce': nounce,
            'previous_hash': previous_hash or self.hash(self.chain[-1])  # Ele pega o hash do bloco anterior automaticamente se precisar
        }

        # Resetando a lista de transações
        self.current_transactions = []

        # Acrescentando o bloco na lista de blocos
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        # Aqui será gerado um dicionário para cada transação e colocado na lista de transações
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        # Retorna o índice do bloco onde será armazenada essa transação
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """O dicionário do bloco deve estar na ordem correta
        pois senão pode gerar um hash diferente dependendo da ordem"""
        block_string = json.dumps(block, sort_keys=True).encode()  # Conversão de dicionário para json
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def nounce_of_work(self, last_nounce):
        nounce = 0
        while self.valid_nounce(last_nounce, nounce) is False:
            nounce += 1
        return nounce

    @staticmethod
    def valid_nounce(last_nounce, nounce):
        guess = f'{last_nounce}{nounce}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'  # Aqui é definido a regra de como o hash deve começar

# Inicializando o nó
app = Flask(__name__)

# Instanciando a Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    # Executa o algoritmo de prova de trabalho para obter a próxima prova
    last_block = blockchain.last_block
    last_nounce = last_block['nounce']
    nounce = blockchain.nounce_of_work(last_nounce)

    # Precisamos receber uma recompensa por encontrar a prova
    # O remetente é "0" para significar que este nó minerou uma nova moeda
    blockchain.new_transaction(
        sender="0",
        recipient="your_address",
        amount=1,
    )

    # Adiciona o novo bloco à cadeia
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(nounce, previous_hash)

    response = {
        'message': "Novo Bloco Forjado",
        'index': block['index'],
        'transactions': block['transactions'],
        'nounce': block['nounce'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Verifica se os campos necessários estão no POST
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Valores faltando', 400

    # Cria uma nova transação
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transação será adicionada ao Bloco {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
