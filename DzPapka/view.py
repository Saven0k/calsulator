import log
import  main


def read_write():
    with open('phonesbook.txt' , 'r') as f:
        data =  f.read()
        log.wr2('Прочитана инфа из справочника')
    return data