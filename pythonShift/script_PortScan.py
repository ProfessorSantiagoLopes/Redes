import socket

host = input("Insira o dominio: ")
portas = [21,22,23,80,443,3306]
print ("Portas Abertas:")
for porta in portas:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    codigoRetorno = sock.connect_ex((host, porta))
    sock.close()
    if codigoRetorno == 0:
        print (porta)