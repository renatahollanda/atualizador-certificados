@echo on
REM ==============================================================
REM Configuração do ambiente Java (ajuste o caminho se necessário)
REM ==============================================================
set "JAVA_HOME=D:\Arquivos de Programas\Java\jdk-11"
set "PATH=%JAVA_HOME%\bin;%PATH%"

REM Versão Java
java -version

pause

REM Movendo para a raiz do projeto (pasta acima da atual "scripts")
cd /d "%~dp0.."

REM ======================================================
REM Executando o script Python para baixar os certificados
REM ======================================================
python -m src

REM ==========================================================
REM Criando o arquivo certs.jar dentro da pasta "certificados"
REM ==========================================================
cd certificados
jar cvfM certs.jar *.cer

echo ===================================================
echo Arquivo certs.jar criado com sucesso!
echo Local: %cd%\certs.jar
echo ===================================================

pause
