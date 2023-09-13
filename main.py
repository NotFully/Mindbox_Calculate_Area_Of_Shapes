import geometry.shapes as sc


def main():
    shapes = []

    while True:
        print("Выберите действие:")
        print("1. Добавить круг")
        print("2. Добавить треугольник")
        print("3. Вывести площади всех фигур")
        print("4. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            try:
                radius = float(input("Введите радиус круга: "))
                shapes.append(sc.Circle(radius))
                print("Круг добавлен.")
            except Exception as ex:
                print(ex)

        elif choice == "2":
            try:
                side1 = float(input("Введите длину первой стороны треугольника: "))
                side2 = float(input("Введите длину второй стороны треугольника: "))
                side3 = float(input("Введите длину третьей стороны треугольника: "))
                shapes.append(sc.Triangle(side1, side2, side3))
                print("Треугольник добавлен.")
            except Exception as ex:
                print(ex)

        elif choice == "3":
            if not shapes:
                print("Список фигур пуст.")
            else:
                for i, shape in enumerate(shapes, 1):
                    print(f"Фигура {i}: Площадь = {shape.area():.2f} кв. ед.")
                    if isinstance(shape, sc.Triangle) and shape.is_right_triangle():
                        print("  Этот треугольник прямоугольный.")

        elif choice == "4":
            print("Программа завершена.")
            break

        else:
            print("Некорректный выбор. Введите номер действия снова.")


if __name__ == "__main__":
    main()
