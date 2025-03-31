from database.DB_connect import get_connection
from model.studente import Studente


class StudentDAO:
    def cercaStudente(self, matricola) -> Studente | None:
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        if cnx is not None:
            query = "SELECT * FROM studente WHERE matricola = %s"
            cursor.execute(query,(matricola,))

            row = cursor.fetchone()
            if row is not None:
                res = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
            else:
                res = None

            cursor.close()
            cnx.close()
            return res
        else:
            print("Non posso connettermi")
            return None

