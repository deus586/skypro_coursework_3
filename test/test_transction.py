from utils.funcs import Transaction
PATH = 'operations.json'


def test_date():
    example = Transaction(PATH)
    assert example.date_and_description(1) == '19.11.2019 Перевод организации'
    assert example.date_and_description(0) == '07.12.2019 Перевод организации'


def test_path():
    example = Transaction(PATH)
    assert example.trans_path(0) == 'Visa Classic 2842 87** **** 9012  -> Счет **3655'
    assert example.trans_path(1) == 'Maestro 7810 84** **** 5568  -> Счет **2869'


def test_payment():
    example = Transaction(PATH)
    assert example.trans_sum(0) == '48150.39 USD'
    assert example.trans_sum(1) == '30153.72 руб.'


def test_results():
    example = Transaction(PATH)
    assert example.results(0) == ('07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012  -> Счет **3655\n'
                                  '48150.39 USD\n')
    assert example.results(1) == ('19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568  -> Счет **2869\n'
                                  '30153.72 руб.\n')
