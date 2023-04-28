result = []
try:
    def divider(a, b):
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a / b


    data = {10: 1, 5: 2, 99: 4, 18: 1, 30: 15, 8 : 4}
    for key in data:
        print(key, data[key])
        res = divider(key, data[key])
        result.append(res)
    print(result)
except IndentationError:
    print("Неправильна табуляція")
except TypeError:
    print("Неправильний тип")
except NameError:
    print("Неправильне ім`я")
except ZeroDivisionError:
    print("Неможна ділити на нуль")
