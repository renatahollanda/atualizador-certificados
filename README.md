# Projeto de Download de Certificados

## Descrição
Este projeto é uma ferramenta para baixar certificados SSL/TLS de vários sites e salvá-los como arquivos `.cer`. O script em Python utiliza o OpenSSL para buscar certificados de URLs especificadas e organiza-os em um arquivo `.jar`.

## Pré-requisitos

Para executar este projeto, é preciso ter os seguintes softwares instalados:

- **Java JDK 11**: Necessário para criar o arquivo `.jar`.
  - [Download do JDK 11](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)
- **Python 3.8+**: Necessário para executar o script de download de certificados.
  - [Download do Python](https://www.python.org/downloads/)
- **OpenSSL**: Necessário para a execução do script Python.
  - [Download do OpenSSL](https://slproweb.com/products/Win32OpenSSL.html) (Windows) ou use o gerenciador de pacotes do seu sistema (Linux/macOS).

## Configuração

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/renatahollanda/atualizador-certificados.git
   cd atualizador-certificados
   ```

2. **Prepare o arquivo de entrada**: Crie um arquivo chamado `dicionario.txt` no diretório do projeto com URLs e nomes de arquivos correspondentes:
    ```txt
    example.com, exemplo_certificado
    sub.dominio.gov.br, certificado_gov
    ```

3. **Executando o arquivo .bat:** No diretório do projeto, execute o arquivo `CertsMaker.bat` no cmd:
    ```bash
    CertsMaker.bat
    ```

## Configuração
O arquivo `CertsMaker.bat` irá:

1. Definir o diretório do Java.
2. Chamar o script Python para baixar os certificados.
3. Criar um arquivo .jar contendo todos os certificados baixados.

Os certificados serão salvos no diretório `./certificados/` como arquivos `.cer`, e o arquivo `.jar` será criado no mesmo diretório.

## Estrutura de Arquivos
**atualizador-certificados/**

* **certificados/**: Pasta para certificados baixados
  * **CertsMaker.bat**: Script para executar o processo

* **dicionario.txt**: Arquivo de entrada com URLs e nomes de arquivos

* **download_certs.py**: Script principal para download de certificados

* **README.md**: Documentação

## Solução de Problemas
* **Erro ao executar o arquivo `.bat`:**
  * Certifique-se de que o Java JDK, Python e OpenSSL estão instalados e configurados corretamente no PATH do sistema.

* **Certificados não baixados:**
  * Verifique se o arquivo `dicionario.txt` está formatado corretamente e se as URLs estão acessíveis.
