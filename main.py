from utils.class_operations import Operations
from utils.function import sort_operations

date_json = sort_operations()

def main():
    '''
    основной код
    '''
    for i in date_json:
        operations = Operations(i)
        print('\n')
        print(f'{operations.date()} {operations.organizations()}')
        if 'Перевод со счета на счет' in operations.organizations():
            print(f'{operations.new_score()} -> {operations.where()}')
        elif 'Открытие вклада' in operations.organizations():
            print(f'-> {operations.where()}')
        else:
            print(f'{operations.hiding_card()} -> {operations.where()}')
        print(f'{operations.operationAmount()}')




main()



