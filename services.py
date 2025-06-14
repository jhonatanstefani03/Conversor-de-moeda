import requests
from symbols import simbolos_moedas


def conversor_moeda(valor, moeda_origem, moeda_destino):
    api_key = '5a6c49a0efcd6feb71e70f992828c342'
    url = (
        f'https://api.exchangerate.host/convert?'
        f'from={moeda_origem}&to={moeda_destino}&amount={valor}&access_key={api_key}'
    )

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados =  resposta.json()
    
        if dados.get("success", True):
            resultado = dados['result']
            simbolo_origem = simbolos_moedas.get(moeda_origem, moeda_origem)
            simbolo_destino = simbolos_moedas.get(moeda_destino, moeda_destino)

            return{
                'valor_origem': valor,
                'valor_convertido': round(resultado,2),
                'simbolo_origem': simbolo_origem,
                'simbolo_destino': simbolo_destino
            }
        else:
            raise  ValueError('Erro na conversão dos dados da API')
        
    except Exception as e:
        print(f"Erro: {e}")
        return None