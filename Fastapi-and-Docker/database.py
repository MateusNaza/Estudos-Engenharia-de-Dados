import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _dec
import sqlalchemy.orm as _orm

DATABASE_URL = "postgresql://mateusnaza:password@localhost/fastapi_db"

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(
    autocommit=False, # As transações não são automaticamente confirmadas.
    autoflush=False, # As alterações não são automaticamente enviadas ao banco de dados.
    bind=engine
)

Base = _dec.declarative_base()



def testar_conexao(database_url):
    try:
        engine = _sql.create_engine(database_url)
        with engine.connect() as connection:
            result = connection.execute(_sql.text("SELECT 1"))
            if result.scalar() == 1:
                print("Conexão bem-sucedida!")
            else:
                print("Falha na conexão.")
    except Exception as e:
        print(f"Erro ao conectar: {e}")

# Exemplo de uso
DATABASE_URL = "postgresql://mateusnaza:password@localhost/fastapi_db"

