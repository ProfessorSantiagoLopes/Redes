import whois
host = input('Insira o domínio:')
w = whois.whois(host)
print(w)