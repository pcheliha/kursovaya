from datetime import datetime

class Operations:
     '''
     создание класса операция
     '''

     def __init__(self, id = []):
         self.id = id


     def date(self):
         '''информация о дате совершения операции'''
         date1 = datetime.strptime(self.id['date'], '%Y-%m-%dT%H:%M:%S.%f')

         date1 = date1.strftime('%d.%m.%Y')
         return date1