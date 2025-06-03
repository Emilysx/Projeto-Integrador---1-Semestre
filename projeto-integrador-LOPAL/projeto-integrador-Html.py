import pandas as pd

# Função que retorna a quantidade com o emoji
def estoque(valor):
    if valor == 0:
        return f"{valor} Produto - 🔴 Vazia"
    elif valor == 1:
        return f"{valor} Produto - 👍🏼 Ok"
    else:
        return f"{valor} Produtos - 🟢 Cheia"

# função para gerar o html
def gerar_html_com_estoque(csv_entrada, html_saida):
    # le os dados e tranforma em tabela
    tabela = pd.read_csv(csv_entrada)

    html = """
    <html>
    <head>
        <title>Status das Esteiras - Monitoramento de Estoque</title>
    </head>
    <body>
        <h1>Status das Esteiras - Monitoramento de Estoque</h1>
        <table border='1' cellpadding='10' cellspacing='0'>
            <tr>
                <th>Data</th>
                <th>Hora</th>
                <th>Esteira 1</th>
                <th>Esteira 2</th>
                <th>Esteira 3</th>
            </tr>
    """

    for linha in tabela.itertuples():
        esteira1 = estoque(linha.esteira1)
        esteira2 = estoque(linha.esteira2)
        esteira3 = estoque(linha.esteira3)

        html += f"""
            <tr>
                <td>{linha.Date}</td>
                <td>{linha.Time}</td>
                <td>{esteira1}</td>
                <td>{esteira2}</td>
                <td>{esteira3}</td>
            </tr>
        """

    html += """
        </table>
        <h4> Criado por Emily Gabrielle Oliveira - 1DS-TB-18 </h4>
    </body>
    </html>
    """

    with open(html_saida, "w", encoding="utf-8") as arquivo:
        arquivo.write(html)

    print(f"HTML criado com sucesso: {html_saida}")

# para rodar a função
gerar_html_com_estoque("Projeto_IntegradorCSV.csv", "Relatorio_Esteiras.html")
