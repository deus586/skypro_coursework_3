import funcs
PATH = '/home/misha/PycharmProjects/coursework_3/utils/operations.json'

if __name__ == '__main__':
    # print five last transactions
    transfer = funcs.Transaction(PATH)
    for i in range(5):
        print(transfer.results(i))
