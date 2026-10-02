from datetime import datetime, timedelta
import requests

def cotar():
    resultado = []
    hoje = datetime.today()

    for i in range(365):
        data = hoje - timedelta(days=i)

        while True:
            data_str = data.strftime("%m-%d-%Y")

            url = (
                "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
                f"CotacaoDolarDia(dataCotacao=@dataCotacao)?"
                f"@dataCotacao='{data_str}'"
                "&$format=json&$select=cotacaoCompra"
            )

            resposta = requests.get(url)
            dados = resposta.json()

            if dados.get("value"):
                resultado.append(round(dados["value"][0]["cotacaoCompra"], 2))
                break

            data -= timedelta(days=1)

    return resultado
print(cotar())