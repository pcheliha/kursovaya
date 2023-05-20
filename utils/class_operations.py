from datetime import datetime
import re


class Operations:
    '''
     создание класса операция
     '''

    def __init__(self, id=[]):
        self.id = id

    def __repr__(self):
        return f'{self.id}'

    def date(self):
        '''информация о дате совершения операции'''
        date1 = datetime.strptime(self.id['date'], '%Y-%m-%dT%H:%M:%S.%f')

        date1 = date1.strftime('%d.%m.%Y')
        return date1

    def organizations(self):
        '''
         получение организаций
        '''
        organizations1 = self.id['description']

        return organizations1

    def from_(self):
        '''
         Возвращает внешний вид карты
        '''
        try:
            from_ = self.id['from']
            return from_
        except KeyError:
            return ''

    def where(self):
        '''
         возвращает номер счета в нужном виде
         '''
        try:
            where1 = self.id['to']
            where1 = where1.replace(where1[5:-4], '**')
            return where1
        except KeyError:
            return ''

    def operationAmount(self):
        '''
         метод возвращает сумму и валюту
         '''
        return f'{self.id["operationAmount"]["amount"]} {self.id["operationAmount"]["currency"]["name"]}'

    def hiding_card(self):
        '''Возвращает карту в нужном виде'''
        try:
            card = Operations.from_(self).split(" ")
            card_num = re.findall(r'\d\d\d\d', card[-1])
            card_num = ' '.join(card_num)
            card_num = card_num.replace(card_num[7:-5], '** ****')
        except KeyError:
            return ''
        else:
            return f'{card[0]} {card_num}'

    def new_score(self):
        try:
            from_ = self.id['from']
            from_ = from_.replace(from_[5:-4], '**')
            return from_
        except KeyError:
            return ''

