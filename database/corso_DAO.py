# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente


class CorsoDAO:
    def getAllCorsi(self) -> list[Corso] | None:

        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        if cnx is not None:
            query = "SELECT * FROM corso"
            cursor.execute(query)

            res = []
            for row in cursor:
                res.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))

            cursor.close()
            cnx.close()
            return res
        else:
            print("Non posso connettermi")
            return None

    def getIscritti(self, codins) -> list[Studente] | None:

        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        if cnx is not None:
            query = """SELECT studente.* 
                FROM iscrizione, studente 
                WHERE iscrizione.matricola=studente.matricola AND iscrizione.codins=%s"""
            cursor.execute(query, (codins,))

            res = []
            for row in cursor:
                res.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))

            cursor.close()
            cnx.close()
            return res
        else:
            print("Non posso connettermi")
            return None

    def getCorsi(self, matricola) -> list[Corso] | None:

        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        if cnx is not None:
            query = """SELECT corso.*
            FROM corso, iscrizione
            WHERE iscrizione.codins=corso.codins AND iscrizione.matricola = %s"""
            cursor.execute(query, (matricola,))

            res = []
            for row in cursor:
                res.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))

            cursor.close()
            cnx.close()
            return res
        else:
            print("Non posso connettermi")
            return None

