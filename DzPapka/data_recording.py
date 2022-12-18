import log
def write(scn , nm , ph , inf, item_numbeer , phonebook):
    log.wr2('Создан справочник')
    phonebook[f'Номер записи {item_numbeer}'] = [scn, nm , ph , inf]
    log.wr2('Добавленны данные в  справочник')
    return phonebook

