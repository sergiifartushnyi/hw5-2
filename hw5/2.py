def main():
    while True:
        try:
            operation = input("Введіть математичну операцію (наприклад, 3 + 4): ")

            result = eval(operation)

            print(f"Результат: {result}")

        except Exception as e:
            print(f"Виникла помилка: {e}")

        continue_calculation = input(
            "Бажаєте продовжити? (yes/y для продовження, будь-яка інша клавіша для виходу): ").strip().lower()

        if continue_calculation not in ['yes', 'y']:
            print("Дякуємо за використання калькулятора. На все добре!")
            break


if __name__ == "__main__":
    main()
