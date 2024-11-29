import fastapi
import Blockchain as blockchain

bc = blockchain.Blockchain()
app = fastapi.FastAPI()


# Endpoint de minerar blocos
@app.post('/mine_block/')
def mine_block():
    block = bc.mine_block()
    return block


# Endpoint de efetuar transação
@app.post('/new_transaction/')
def new_transaction(sender, recipent, amount):
    transaction = bc.new_transaction(sender, recipent, amount)
    return transaction


# Endpoint que retorna a blockchain completa
@app.get('/chain/')
def get_blockchain():
    chain = bc.chain
    return chain


# Endpoint para verificar a lista de transações que ainda não foram para um bloco
@app.get('/current_transactions/')
def current_transactions():
    transactions = bc.current_transactions
    return transactions



