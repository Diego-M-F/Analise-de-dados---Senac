from sqlalchemy import create_engine, text

host = ''
user = ''
password = ''
database = ''


def conecta_banco():
    try:
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

        with engine.connect() as conexao:
            query = 'SELECT * FROM importacao_mini'

            resultado = conexao.execute(text(query))

            if resultado.rowcount > 0:
                for item in resultado:
                    # print(item)
                    # print(item[0], item[1], item[2])
                    print(item[9])

    except Exception as e:
        print(f'Erro: {e}')


conecta_banco()

