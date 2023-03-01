# Berardinelli Daniele | CC UNIVPM 

import base64
from Crypto.Cipher import AES

messaggio_b64 = "" #Inserisci qui il b64
messaggio = base64.b64decode(messaggio_b64)

key = b'' #Inserisci la chiave di cifratura

# Inizio Bruteforce 
lista_iv = [bytes([i]) * 16 for i in range(256)]  

for iv in lista_iv:
    cifrario = AES.new(key, AES.MODE_CBC, iv)
    messaggio_decriptato = cifrario.decrypt(messaggio[16:])
    messaggio_unpaddato = messaggio_decriptato[:-messaggio_decriptato[-1]]
    try:
        messaggio_finale = messaggio_unpaddato.decode('utf-8')
        print(f'IV trovato: {iv.hex()}')
        print(messaggio_finale)
    except UnicodeDecodeError:
        pass
