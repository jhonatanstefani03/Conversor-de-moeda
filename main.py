from services import conversor_moeda

def main():
    while True:
        try:
            valor = float(input('Digite o valor: '))
            moeda_origem = input('Digite a moeda de origem (ex: BRL, USD, EUR): ').upper()
            moeda_destino = input('Digite a moeda de destino: ').upper()

            resultado = conversor_moeda(valor, moeda_origem, moeda_destino)

            if resultado:
                print(
                    f"{resultado['simbolo_origem']}{resultado['valor_origem']} "
                    f"equivale a {resultado['simbolo_destino']}{resultado['valor_convertido']}"
                )
            else:
                print("Não foi possível realizar a conversão.")

        except ValueError:
            print("Digite um número válido para o valor!")

        continuar = input('Deseja fazer outra conversão? (s/n): ').lower()
        if continuar != 's':
            break


if __name__ == "__main__":
    main()