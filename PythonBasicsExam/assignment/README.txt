In questo esempio ho pensato di mettere in pratica i concetti della programmazione ad oggetti in python
realizzando un piccolo programma che simula la gestione di una Biblioteca.

Le classi che ho utilizzato sono le seguenti:

-Opera: classe madre che definisce gli oggetti prestabili all'interno della biblioteca quali Libri o CD.
        Le istanze della classe opera sono caratterizzate dai seguenti attributi:
        -titolo: stringa che caratterizza il titolo dell'opera
        -in_prestito: booleano che identifica se l'opera si trova in prestito o no

        Oltre agli attributi la classe Opera implementa alcuni metodi: 
        -   colloca_in_prestito: metodo che in caso di concessione in prestito dell'opera imposta la variabile booleana in_prestito a True
        -   restituzione_dal_prestito: metodo che in caso di restituzione dal prestito di un'opera imposta la variabile booleana in_prestito a False
        -   get_titolo e set_titolo: sono i metodi getter e setter che consentono rispettivamente di ottenere e impostare il titolo dell'opera
        -   __repr__: override del metodo __repr__ che personalizza l'output della funzione builtin print() quando viene invocata su un oggetto della classe Opera
        -   produci_scheda: dichiarazione ma non implementazione del metodo che sarà implementato nelle sottoclassi e che si occupa della redazione della scheda riepilogativa di un'opera.

-Libro: sottoclasse della classe Opera. Una istanza di questa classe rappresenta un libro della Biblioteca caratterizzato dai seguenti attributi:
    - gli attributi titolo e in_prestito sono ereditati dalla classe madre Opera
    - numero_pagine: ulteriore attributo di istanza che definisce il numero di pagine del libro
    Per la classe Libri ho implementato i seguenti metodi:
    - get_numero_pagine: metodo getter che permette di ottenere il numero di pagine del libro
    - set_numero_pagine: metodo Setter che permette di impostare il numero di pagine del libro
    - produci_scheda: override del metodo produci_scheda ereditato dalla classe madre Opera. Qui il metodo viene implementato in modo da produrre la scheda riepilogativa per l'oggetto Libro
    
-CD: sottoclasse della classe Opera. Una istanza di questa classe rappresenta un CD della Biblioteca caratterizzato dai seguenti attributi:
    - gli attributi titolo e in_prestito sono ereditati dalla classe madre Opera
    - numero_tracce: ulteriore attributo di istanza che definisce il numero di tracce del CD
    Per la classe CD ho implementato i seguenti metodi:
    - get_numero_tracce: metodo getter che permette di ottenere il numero di brani del CD
    - set_numero_tracce: metodo Setter che permette di impostare il numero di brani del CD
    - produci_scheda: override del metodo produci_scheda ereditato dalla classe madre Opera. Qui il metodo viene implementato in modo da produrre la scheda riepilogativa per l'oggetto CD

-Studente: classe che definisce gli studenti che usufruiscono dei prestiti della biblioteca. 
    per ogni studente sono definiti i seguenti attributi di istanza:
    - nome
    - cognome
    Sono inoltre definiti i metodi: 
    - set_nome: metodo che consente di impostare il nome dello studente
    - set cognome: metodo che consente di impostare il cognome dello studente
    - get_nominativo: metodo che restituisce nome e cognome dello studente

-Biblioteca: questa clsse rappresenta il sistema di gestione della biblioteca.
    Una istanza della Biblioteca è caratterizzata dall'attributo "registro". si stratta di un dizionario sul quale saranno registrati i prestiti effettuati.
    La classe Biblioteca implementa i seguenti metodi:
    - effettua_prestito: metodo che gestisce il prestito di un'opera ad uno studente. Questo metodo controlla se l'opera da mandare in prestito è presente in archivio o si trova in prestito.
                        Nel caso in cui l'opera può andare in prestito aggiorna il "registro" e cambia il flag in_prestito su True. 
    - restituzione_dal_prestito: metodo che gestisce il ritiro delle opere concesse in prestito. Ad ogni opera riconsegnata dagli studenti rimuove la corrispondente vode dal registro ed 
                        aggiorna il flag in_prestito su False.
    - stampa_lista_prestiti: metodo che stamapa a schermo il dizionario "registro" che riporta per ogni studente la lista delle opere che ha in prestito.

- modulo Main.py: In questo modulo python è contenuto il main. Qui sono instanziate le classi sopra descritte e avviene la gestione della biblioteca tramite l'esecuzione dei prestiti e delle restituzioni.
