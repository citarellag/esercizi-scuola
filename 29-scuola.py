'''Dato un elenco di città, con l'indicazione per ciascuna di esse del nome e delle temperature massima e minima registrate in un giorno, si devono contare quante città hanno superato nel giorno un valore prefissato per l'escursione termica, ottenuta per differenza tra temperatura massima e minima.
Organizza un programma che, dopo aver richiesto il valore da controllare dell'escursione termica, per ogni città dell'elenco ripeta la richiesta dei dati: 
(nome, temperatura massima e minima),
calcoli l'escursione termica e controlli se l'escursione è maggiore del valore prefissato: 
in questo caso, incrementa il contatore delle città selezionate. Alla fine della ripetizione comunica il numero delle città registrato nel contatore. '''

città = []
ltmax = []
ltmin = []
r = 0
n = 0
while True:
    n += 1
    print("Digita nome della città numero", n)
    nomec = input()
    città.append(nomec)
    print("Digita il valore massimo della temperatura giornaliera di", nomec)
    vtmax = int(input())
    ltmax.append(vtmax)
    print("Digita il valore minimo della temperatura giornaliera di", nomec)
    vtmin = int(input())
    ltmin.append(vtmin)
    stop2 = input("Premi 0 se hai finito le città, premi qualsiasi altro tasto per continuare ")
    if stop2 == "0":
        break
    else:
        pass

print("Inserire valore massimo dell'escursione termica che può accettare il contatore")
escursione_max = int(input())
for i in range(n):
    esc_città = ltmax[i]-ltmin[i]
    if escursione_max < esc_città:
        r += 1
        print("\nI valori delle città che non rientrano nel range del contatore sono:", r,"\n...")
    else:
        pass
print("\nOra tutti i valori delle", n,"città rientrano nel range del contatore")