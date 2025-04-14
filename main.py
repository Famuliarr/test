def chat_bot():
    target_number = 42  # Загаданное число
    print("Привет! Я бот, который будет с тобой говорить, пока ты не угадаешь моё число.")
    print("Подсказка: число находится в диапазоне от 1 до 100. Попробуй угадать!")

    while True:
        user_input = input("Твоя догадка (или 'выход' для завершения): ").strip().lower()

        # Проверяем, хочет ли пользователь выйти
        if user_input == 'выход':
            print("До свидания! Возвращайся ещё.")
            break

        # Проверяем, является ли ввод числом
        if not user_input.isdigit():
            print("Пожалуйста, введи число!")
            continue

        guess = int(user_input)

        # Проверяем, угадал ли пользователь число
        if guess == target_number:
            print(f"Поздравляю! Ты угадал число {target_number}. Игра завершена.")
            break
        elif guess < target_number:
            print("Моё число больше. Попробуй ещё раз!")
        else:
            print("Моё число меньше. Попробуй ещё раз!")

# Запускаем бота
if __name__ == "__main__":
    chat_bot()