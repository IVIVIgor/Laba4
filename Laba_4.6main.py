from Laba_4_6 import count_elements_above_value # type: ignore

def main():
    # Пример списка
    list_A = [10, 20, 30, 40, 50]
    # Заданное значение
    k = 25
    # Подсчитываем количество элементов списка, превышающих заданное значение
    count = count_elements_above_value(list_A, k)
    print(f"Количество элементов списка, превышающих значение {k}: {count}")

if __name__ == "__main__":
    main()
