import log
import data_recording
import main


def impt_1():
#gg.txt
    with open('gg.txt' , 'r') as gg:
        data = str(gg.read()).split()
    def go(data):
        gg1 = int(input("Введите номер на который надо поставить эту запись: "))
        if main.phonebook[gg1]:
            print("Это место заанято")
            go(data)
        else:
            data_recording.write(data[0], data[2] , data[3] , data[4] , main.phonebook , gg1 )
    go(data)
    log.wr2(f"Человек выбрал импортировать из файла gg.txt")


def impt_2():
#text.txt
    with open('Text.txt' , 'r') as gg:
        data = str(gg.read()).split()
    def go(data):
        gg1 = int(input("Введите номер на который надо поставить эту запись: "))
        if main.phonebook[gg1]:
            print("Это место заанято")
            go(data)
        else:
            data_recording.write(data[0], data[2] , data[3] , data[4] , main.phonebook , gg1 )
    go(data)
    log.wr2(f"Человек выбрал импортировать из файла Text.txt")



def impt_3():
#   number.tt
    with open('Nuber..txt' , 'r') as gg:
        data = str(gg.read()).split()
    def go(data):
        gg1 = int(input("Введите номер на который надо поставить эту запись: "))
        if main.phonebook[gg1]:
            print("Это место заанято")
            go(data)
        else:
            data_recording.write(data[0], data[2] , data[3] , data[4] , main.phonebook , gg1 )
    go(data)
    log.wr2(f"Человек выбрал импортировать из файла Nuber.txt")