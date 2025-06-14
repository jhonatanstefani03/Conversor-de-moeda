Conversor de Moeda - Python
Este é um projeto simples de conversor de moedas feito em Python, que utiliza uma API para obter a cotação em tempo real e realizar a conversão entre diversas moedas.

🚀 Funcionalidades
✔️ Conversão de moedas em tempo real

✔️ Suporte a várias moedas (BRL, USD, EUR, GBP, JPY, etc.)

✔️ Interface no terminal (modo texto)

✔️ Tratamento de erros (entrada inválida, erros de conexão, moedas não suportadas)

🛠️ Tecnologias utilizadas
Python 3

Biblioteca requests (para consumir a API)

API de câmbio ExchangeRate Host

📂 Estrutura do Projeto
bash
Copiar
Editar
conversor-de-moeda/
│
├── main.py               # Arquivo principal (interface)

├── services.py           # Lógica de conversão (regra de negócio)

├── symbols.py            # Lista de símbolos das moedas

└── README.md             # Documentação

🔧 Como executar o projeto
1. Clone o repositório:
bash
Copiar
Editar
git clone https://github.com/seu-usuario/conversor-de-moeda.git
cd conversor-de-moeda
2. Crie um ambiente virtual (opcional, mas recomendado):
bash
Copiar
Editar
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows

3. Execute o programa:
bash
Copiar
Editar
python main.py
⚙️ Como funciona O programa solicita:

Valor a ser convertido

Moeda de origem (ex.: BRL)

Moeda de destino (ex.: USD)

Faz a requisição na API e retorna o valor convertido, exibindo com os símbolos das moedas.

🌎 Moedas Suportadas
🇧🇷 BRL - Real

🇺🇸 USD - Dólar

🇪🇺 EUR - Euro

🇬🇧 GBP - Libra

🇯🇵 JPY - Iene

🇨🇦 CAD - Dólar Canadense

🇨🇭 CHF - Franco Suíço

🇨🇳 CNY - Yuan

🇮🇳 INR - Rúpia

🇦🇺 AUD - Dólar Australiano

🐞 Tratamento de erros implementado
🔸 Entrada inválida (ex.: letras onde pede número)

🔸 Moeda não existente

🔸 Problemas de conexão com a API

🔸 Erros inesperados

📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

🤝 Contribuindo
Sinta-se livre para abrir issues, sugerir melhorias ou fazer pull requests! 









