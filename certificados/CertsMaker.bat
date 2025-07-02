@echo on

rem Define o diretório do JDK
set JAVA_HOME="D:\Arquivos de Programas\Java\jdk-11"
set PATH=%JAVA_HOME%\bin;%PATH%

rem Exibe a versão do Java
java -version

pause

rem =========================
rem Executando o script Python para baixar os certificados
rem =========================
python ..\download_certs.py

rem =========================
rem Criando arquivo certs.jar
rem =========================
jar cvfM certs.jar *.cer

rem Arquivo criado com sucesso!
echo Arquivo certs.jar criado com sucesso!

pause
