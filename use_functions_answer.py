score = 0
purchase = []

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню ')
    if choice == '1':
        score = int(input('На сколько пополнить счет? '))
        print(score)

    elif choice == '2':
        purchase_question_score = int(input('На какую суммы Вы хотите сделать покупку? '))
        if score < purchase_question_score:
            print('У Вас недостаточно средств на счете')
        else:
            purchase_question = input('Что вы хотите купить? ')
            purchase.append(purchase_question)
            score = score - purchase_question_score
            print(purchase)
            print(score)
    elif choice == '3':
        print('Вы купили', purchase)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
