import random #генерация соучайных чисел (карт)

def play_21(): #содание функции, содержащая всю логику игры
    print("Добро пожаловать в игру '21 очко'!")
    
    # Инициализация карт
    player_cards = [random.randint(2, 11), random.randint(2, 11)] #игрок получает 2 случайных карты от 2 до 11
    dealer_cards = [random.randint(2, 11)] #диллер 1, вторая будет добавлена потом
    
    print(f"\nВаши карты: {player_cards}, Сумма: {sum(player_cards)}") #показывает карты игрока и их сумму
    print(f"Карта дилера: {dealer_cards[0]}") #показывает одну карту диллера
    
    # Ход игрока
    while True: #бесконечный цикл хода игрока
        choice = input("\n1 - Взять карту\n2 - Остановиться\nВыберите действие: ") #предлагает выбор(взять карту/остановиться)
        if choice == '1':
            player_cards.append(random.randint(2, 11)) #при выборе "1" добавляет новую карту игроку, проверка, не превыспл ли игрок 21 очко
            print(f"\nВаши карты: {player_cards}, Сумма: {sum(player_cards)}")
            if sum(player_cards) > 21:
                print("Перебор! Вы проиграли.")
                return
        elif choice == '2': #при выборе "2" завершает ход игрока
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
    
    # Ход дилера
    dealer_cards.append(random.randint(2, 11)) #диллер получает вторую карту
    while sum(dealer_cards) < 17: #диллер бурет карты, пока сумма не достигнет 17 или более
        dealer_cards.append(random.randint(2, 11))
    
    print(f"\nКарты дилера: {dealer_cards}, Сумма: {sum(dealer_cards)}") #показывает все карты диллера и их сумму
    
    # Определение победителя
    player_sum = sum(player_cards)
    dealer_sum = sum(dealer_cards) #вычисление суммы карт игрока и диллера
    
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
