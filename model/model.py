from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

   # --- LETTURA TUTTE LE AUTO ---
    def get_automobili(self) -> list[Automobile] | None:
        """
        Legge tutte le automobili presenti nel database.
        Restituisce una lista di oggetti Automobile o None se vuoto/errore.
        """
        try:
            cnx = get_connection()
            cursor = cnx.cursor()

            # Query SQL per ottenere tutte le auto
            query = """SELECT codice, marca, modello, anno, posti, disponibile FROM automobile;"""
            cursor.execute(query)

            result = []
            for row in cursor:
                # Crea un oggetto Automobile per ogni riga letta
                auto = Automobile(
                    codice=row[0],
                    marca=row[1],
                    modello=row[2],
                    anno=row[3],
                    posti=row[4],
                    disponibile=bool(row[5])
                )
                result.append(auto)

            cursor.close()
            cnx.close()

            # Se la lista è vuota restituisce None
            return result if result else None

        except Exception as e:
            print("Errore in get_automobili:", e)
            return None

    # --- RICERCA AUTO PER MODELLO ---
    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
        Cerca tutte le automobili nel database che contengono nel modello
        la stringa specificata (case insensitive).
        """
        try:
            cnx = get_connection()
            cursor = cnx.cursor()

            # Query SQL parametrica (evita SQL injection)
            query = """SELECT codice, marca, modello, anno, posti, disponibile
                       FROM automobile
                       WHERE modello LIKE %s;"""
            cursor.execute(query, (f"%{modello}%",))

            result = []
            for row in cursor:
                auto = Automobile(
                    codice=row[0],
                    marca=row[1],
                    modello=row[2],
                    anno=row[3],
                    posti=row[4],
                    disponibile=bool(row[5])
                )
                result.append(auto)

            cursor.close()
            cnx.close()

            return result if result else None

        except Exception as e:
            print("Errore in cerca_automobili_per_modello:", e)
            return None