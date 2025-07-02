import os
import subprocess


def download_certificado(url, nomeArquivo):
    """Baixa o certificado do site usando OpenSSL"""
    try:
        # Remove o prefixo 'https://' e qualquer caminho adicional
        host = url.split("//")[-1].split("/")[0]  # Extrai apenas o host
        comando = (
            f"echo | openssl s_client -connect {host}:443 "
            f"-servername {host} | openssl x509 -outform PEM > "
            f"certificados\\{nomeArquivo}.cer"
        )

        # Executa o comando
        subprocess.run(comando, shell=True, check=True)
        print(f"Certificado salvo como {nomeArquivo}.cer")
    except subprocess.CalledProcessError as erro:
        print(f"Erro ao baixar o certificado de {url}: {str(erro)}")


def ler_arquivo_dicionario(caminhoArquivo):
    """
    Lê o arquivo de dicionário e retorna uma lista de tuplas
    (url, nomeArquivo)
    """
    registros = []
    try:
        with open(caminhoArquivo, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha and ',' in linha:
                    url, nomeArquivo = linha.split(',', 1)
                    registros.append((url.strip(), nomeArquivo.strip()))
    except FileNotFoundError:
        print(f"Erro: Arquivo {caminhoArquivo} não encontrado.")
    return registros


def main():
    # Cria a pasta "certificados" se não existir
    if not os.path.exists("certificados"):
        os.makedirs("certificados")

    # Lê o arquivo de dicionário
    registros = ler_arquivo_dicionario("dicionario.txt")

    if not registros:
        print("Nenhum registro encontrado no arquivo 'dicionario.txt'.")
        return

    for url, nomeArquivo in registros:
        download_certificado(url, nomeArquivo)


if __name__ == "__main__":
    main()
