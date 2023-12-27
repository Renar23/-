def format_time(seconds):
    # Рассчитываем количество дней, часов, минут и секунд
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    # Выводим результат в формате D:HH:MM:SS
    formatted_time = "{:02}:{:02}:{:02}:{:02}".format(int(days), int(hours), int(minutes), int(seconds))
    return formatted_time

# Получаем от пользователя количество секунд
user_input = int(input("Введите количество секунд: "))

# Форматируем и выводим результат
result = format_time(user_input)
print("Время в формате D:HH:MM:SS:", result)
