import random
import time
import json
from datetime import datetime

def save_statistics(attempts, game_time, result):
    """Сохраняет статистику игры в файл"""
    try:
        # Пытаемся загрузить существующую статистику
        with open('guess_number_stats.json', 'r') as f:
            stats = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Если файла нет или он пустой, создаем новую статистику
        stats = []
    
    # Добавляем новую запись
    stats.append({
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'attempts': attempts,
        'time_seconds': round(game_time, 2),
        'result': result
    })
    
    # Сохраняем обновленную статистику
    with open('guess_number_stats.json', 'w') as f:
        json.dump(stats, f, indent=4)

def play_game():
    """Основная функция игры"""
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать!")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()
    
    while True:
        try:
            guess = int(input("Введите вашу догадку (1-100): "))
        except ValueError:
            print("Пожалуйста, введите целое число!")
            continue
        
        if guess < 1 or guess > 100:
            print("Число должно быть в диапазоне от 1 до 100!")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Загаданное число больше.")
        elif guess > secret_number:
            print("Загаданное число меньше.")
        else:
            end_time = time.time()
            game_time = end_time - start_time
            print(f"Поздравляю! Вы угадали число за {attempts} попыток и {round(game_time, 2)} секунд!")
            save_statistics(attempts, game_time, 'win')
            break
        
        if attempts >= 10:
            end_time = time.time()
            game_time = end_time - start_time
            print(f"К сожалению, вы не угадали число за 10 попыток. Это было число {secret_number}.")
            save_statistics(attempts, game_time, 'lose')
            break

def show_statistics():
    """Показывает статистику предыдущих игр"""
    try:
        with open('guess_number_stats.json', 'r') as f:
            stats = json.load(f)
            
        print("\nСтатистика игр:")
        print("-" * 50)
        print(f"{'Дата':<20} | {'Попыток':<8} | {'Время (с)':<10} | {'Результат':<10}")
        print("-" * 50)
        
        for game in stats[-10:]: # Показываем последние 10 игр
            print(f"{game['date']:<20} | {game['attempts']:<8} | {game['time_seconds']:<10} | {game['result']:<10}")
        
        # Вычисляем общую статистику
        wins = sum(1 for game in stats if game['result'] == 'win')
        total_games = len(stats)
        win_rate = (wins / total_games * 100) if total_games > 0 else 0
        
        print("\nОбщая статистика:")
        print(f"Всего игр: {total_games}")
        print(f"Побед: {wins} ({win_rate:.1f}%)")
        
    except (FileNotFoundError, json.JSONDecodeError):
        print("Статистика пока недоступна. Сыграйте хотя бы одну игру!")

def main():
    while True:
        print("\nМеню:")
        print("1. Начать новую игру")
        print("2. Показать статистику")
        print("3. Выход")
        
        choice = input("Выберите действие (1-3): ")
        
        if choice == '1':
            play_game()
        elif choice == '2':
            show_statistics()
        elif choice == '3':
            print("Спасибо за игру! До свидания!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()
