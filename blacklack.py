import random

def play_21():
    print("Добро пожаловать в игру '21 очко'!")
    
    # Инициализация карт
    player_cards = [random.randint(2, 11), random.randint(2, 11)]
    dealer_cards = [random.randint(2, 11)]
    
    print(f"\nВаши карты: {player_cards}, Сумма: {sum(player_cards)}")
    print(f"Карта дилера: {dealer_cards[0]}")
    
    # Ход игрока
    while True:
        choice = input("\n1 - Взять карту\n2 - Остановиться\nВыберите действие: ")
        if choice == '1':
            player_cards.append(random.randint(2, 11))
            print(f"\nВаши карты: {player_cards}, Сумма: {sum(player_cards)}")
            if sum(player_cards) > 21:
                print("Перебор! Вы проиграли.")
                return
        elif choice == '2':
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
    
    # Ход дилера
    dealer_cards.append(random.randint(2, 11))
    while sum(dealer_cards) < 17:
        dealer_cards.append(random.randint(2, 11))
    
    print(f"\nКарты дилера: {dealer_cards}, Сумма: {sum(dealer_cards)}")
    
    # Определение победителя
    player_sum = sum(player_cards)
    dealer_sum = sum(dealer_cards)
    
    if dealer_sum > 21:
        print("Дилер перебрал! Вы выиграли!")
    elif player_sum > dealer_sum:
        print("Вы выиграли!")
    elif player_sum == dealer_sum:
        print("Ничья!")
    else:
        print("Вы проиграли.")

# Запуск игры
play_21()
