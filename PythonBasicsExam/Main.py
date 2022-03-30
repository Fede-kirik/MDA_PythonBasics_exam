from Biblioteca import Biblioteca
from CD import CD
from Libro import Libro
from Studente import Studente


if __name__ == "__main__":  

    #studenti censiti nel sistema bibliotecario
    studente1 = Studente("Tizio", "Rossi")
    studente2 = Studente("Caio", "Bianchi")
    studente3 = Studente("Sempronio", "Verdi")
    

    #libri e cd censiti nel sistema bibliotecario   
    libro1 = Libro("Fisica1", 800)
    libro2 = Libro("Matematica", 570)
    cd = CD("Pink Floyd", 10)

    #inizializzo il registro dei prestiti. Supponiamo che all'inizio nessuna opera sia in prestito.
    registro_prestiti = {}

    #istanza della classe Biblioteca
    biblio = Biblioteca(registro_prestiti)

    #1 STUDENTE1 RICHIEDE UN PRESTITO
    print(f"lo studente {studente1.get_nominativo()} chiede in prestito il libro {libro1.get_titolo()}")
    biblio.effettua_prestito(studente1, libro1)

    print("\n")

    #2 STUDENTE2 RICHIEDE IN PRESTITO IL LIBRO IN POSSESSO DELLO STUDENTE1
    print(f"lo studente {studente2.get_nominativo()} chiede in prestito il libro {libro1.get_titolo()}")
    biblio.effettua_prestito(studente2, libro1)

    print("\n")


    #3 STUDENTE1 RICHIEDE UN SECONDO PRESTITO
    print(f"lo studente {studente1.get_nominativo()} chiede in prestito il libro {libro2.get_titolo()}")
    biblio.effettua_prestito(studente1, libro2)

    print("\n")

    #RIEPILOGO PRESTITI
    biblio.stampa_lista_prestiti()
    print("\n")

    #4 STUDENTE1 RESTITUISCE UNO DEI SUOI PRESTITI
    print(f"lo studente {studente1.get_nominativo()} restituisce dal prestito il libro {libro2.get_titolo()}")
    biblio.restituzione_prestito(studente1, libro2)
    print("\n")

    #RIEPILOGO PRESTITI
    biblio.stampa_lista_prestiti()
    print("\n")

    #5 STUDENTE2 ORA PUO PRENDERE IL PRESTITO IL LIBRO2
    print(f"lo studente {studente2.get_nominativo()} prende in prestito il libro {libro2.get_titolo()}")
    biblio.effettua_prestito(studente2, libro2)
    print("\n")

    #6 STUDENTE3 RICHIEDE IN PRESTITO IL CD 
    print(f"lo studente {studente3.get_nominativo()} chiede in prestito il libro {cd.get_titolo()}")
    biblio.effettua_prestito(studente3, cd)
    print("\n")

    #RIEPILOGO PRESTITI
    biblio.stampa_lista_prestiti()

    