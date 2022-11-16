from Opera import Opera
from Studente import Studente
import pprint

class Biblioteca:

    #costruttore
    def __init__(self, registro: dict) -> None:
        self.registro = registro

    #metodo che implementa il prestito
    def effettua_prestito(self, studente: Studente, opera: Opera) -> None:
        
        if opera.in_prestito: 
            print(f"Volume già in prestito!\n")
        else: 
            print("Volume disponibile!")
            opera.colloca_in_prestito()
            opera.produci_scheda()

            if studente.get_nominativo() not in self.registro:
                self.registro[studente.get_nominativo()] = [opera.get_titolo()]
            else:
                self.registro[studente.get_nominativo()].append(opera.get_titolo())

            
    #metodo che implementa la restituzione di un prestito
    def restituzione_prestito(self, studente: Studente, opera: Opera) -> None:
        if opera.in_prestito: 
            self.registro[studente.get_nominativo()].remove(opera.get_titolo())
            opera.restituzione_dal_prestito()
            print("restituzione effettuata")
        else: 
            print("Lo studente non ha in prestito questo articolo!")

    #metodo che stampa il riepilogo di tutti i prestiti effettuati
    def stampa_lista_prestiti(self) -> None:
        print("LISTA DI TUTTI I PRESTITI EFFETTUATI")
        #for item in self.lista_prestiti:
        pprint.pprint(f"{self.registro}")


    