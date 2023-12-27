def triangle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Равносторонний треугольник"
        elif a == b or a == c or b == c:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"
    else:
        return "Треугольник с такими сторонами не существует"

# Запрашиваем у пользователя длины сторон
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

# Определяем тип треугольника и выводим результат
result = triangle_type(a, b, c)
print(result)