import log
import os

def export_data_txt(data):
    if os.path.exists('DzPapka/export.txt'):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'export.txt')
        os.remove(path)
    else:
        with open('export.txt' , 'w') as file:
            log.wr2("Экспортировал в зарешение .txt")
            file.write(f'{data}\n')

def export_data_exl(data):
    if os.path.exists('DzPapka/export.csv'):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'export.csv')
        os.remove(path)
    else:
        with open('export.csv' , 'w') as file:
            log.wr2("Экспортировал в зарешение .csv")
            file.write(data)
