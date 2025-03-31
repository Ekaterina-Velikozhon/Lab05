from database.corso_DAO import CorsoDAO
from database.studente_DAO import StudentDAO


class Model:
   def __init__(self):
      self.corsoDAO = CorsoDAO()
      self.studentDAO = StudentDAO()

   def getCorsi(self):
      return self.corsoDAO.getAllCorsi()

   def getIscritti(self, corso):
      return self.corsoDAO.getIscritti(corso)

   def getStudente(self, matricola):
      return self.studentDAO.cercaStudente(matricola)

   def getCorsiStudente(self, matricola):
      return self.corsoDAO.getCorsi(matricola)