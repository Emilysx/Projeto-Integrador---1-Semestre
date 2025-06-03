import pandas as pd

def gerar_relatorio_excel(caminho_csv, caminho_excel):
    # para ler o arquivo csv
    df = pd.read_csv(caminho_csv, sep=',')

    # para salvar o arquivo excel usando os valoes da tabela
    df.to_excel(caminho_excel, index=False)

    # Mostra caso o arquivo foi gerado
    print(f"Relatório gerado com sucesso em:  {caminho_excel}")

# função principal do programa
def main():
    caminho_csv = "Projeto_IntegradorCSV.csv"  # arquivo CSV
    caminho_excel = "Relatorio_de_Estoque.xlsx"   # nome do arquivo excel que vai ser criado
    gerar_relatorio_excel(caminho_csv, caminho_excel)

if __name__ == "__main__":
    main()
