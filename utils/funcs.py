from json import load


class Transaction:
    def __init__(self, path):
        with open(path, 'r', encoding='UTF-8') as file:
            self.data = sorted([i for i in load(file) if len(i) > 0 and i['state'] == 'EXECUTED' and
                          'Перевод' in i['description']], key=lambda x: x['date'], reverse=True)

    def date_and_description(self, number):
        """

        return date of transaction and description
        """
        payday = self.data[number]["date"]
        description = self.data[number]['description']

        payday = payday.split('T')[0]
        payday = '.'.join(payday.split('-')[::-1])
        return f'{payday} {description}'

    def trans_path(self, number):
        """

        return the path of transaction: from and to
        """
        from_ = self.data[number]['from'].split()
        to_ = self.data[number]['to'].split()

        card_number = from_[-1]
        card = ''
        for i in range(0, len(card_number), 4):
            card += card_number[i:i + 4] + ' '
        card = card[:7] + '** **** ' + card[-5:]

        count_number = '**' + to_[1][-4:]

        return f'{" ".join(from_[:-1])} {card} -> {to_[0]} {count_number}'

    def trans_sum(self, number):
        """

        return transfer amount and currency
        """
        transfer = self.data[number]['operationAmount']["amount"]
        currency = self.data[number]['operationAmount']["currency"]["name"]

        return f'{transfer} {currency}'

    def results(self, i):
        """

        return transaction info
        """
        return f'{self.date_and_description(i)}\n{self.trans_path(i)}\n{self.trans_sum(i)}\n'
