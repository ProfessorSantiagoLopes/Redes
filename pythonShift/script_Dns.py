import socket
dominio = input('Insira o domínio:')
nomes = ["ns1","ns2","www","ftp","smtp","pop","intranet","painel","on","www2"]

for nome in nomes:
    DNS = nome + "." + dominio
    try:
        print(DNS + ":" + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass