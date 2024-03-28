import logging

from prettytable import PrettyTable

from utils import get_d_data, check_word


def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s')
    logging.getLogger().setLevel(logging.WARNING)  # Устанавливаем уровень логирования на WARNING
    alphabet = []
    print("Введите алфавит. Напишите 'end' для завершения ввода")
    while True:
        value = input("Введите символ: ")
        if value == 'end':
            break
        if len(value) != 1:
            print("Введено не одно значение")
            continue
        alphabet.append(value)

    while True:
        count_of_vertex = input("Введите кол-во вершин: ")
        if not count_of_vertex.isdigit():
            print("Введено не число")
            continue
        count_of_vertex = int(count_of_vertex)
        if count_of_vertex < 1:
            print("Введено не положительное число")
            continue
        break

    # -------------- Конечные вершины --------------
    print("Введите конечные вершины. Напишите 'end' для завершения ввода")
    end_vertex = []
    while True:
        vertex = input("Введите конечную вершину: ")
        if vertex.replace(" ", "").lower() == 'end':
            break
        if vertex not in [f"q{i}" for i in range(count_of_vertex)]:
            print("Введена не вершина")
            continue
        end_vertex.append(vertex)

    # ----------------- Ввод таблицы -----------------
    print("Введите переходы в формате: q0,q1,q2")
    table_data = []
    for i in range(count_of_vertex):
        row = []
        for j in range(len(alphabet)):
            value = input(f"Введите переход из q{i} по {alphabet[j]}: ").replace(" ", "").split(",")
            if value == ['-']:
                value = None
            row.append(value)
        table_data.append({"from": f'q{i}', "to": row})

    # ----------------- Вывод таблицы -----------------
    table = PrettyTable()
    table.field_names = [" "] + alphabet
    for row in table_data:
        row = [row["from"]] + row["to"]
        for i in range(len(row)):
            if row[i] is None:
                row[i] = "∅"
            if type(row[i]) is list:
                row[i] = ", ".join(row[i])
        table.add_row(row)
    print(table)

    # -------------- Начальные вершины --------------
    start_vertex = []
    for row in table_data:
        is_start = True
        for row2 in table_data[1:]:
            for list_of_el in row2["to"]:
                if list_of_el is None:
                    continue
                if row["from"] in list_of_el:
                    is_start = False
                    break
        if is_start:
            start_vertex.append(row["from"])
    print(f"Начальные вершины: {start_vertex}")

    # ----------- Детерминированный автомат -----------
    p_start_vertex, p_end_vertex, p_table_data = get_d_data(
        start_vertex=start_vertex,
        end_vertex=end_vertex,
        alphabet=alphabet,
        table_data=table_data
    )

    # ----------------- Вывод таблицы -----------------
    table = PrettyTable()
    table.field_names = [" "] + alphabet
    rows = []
    count_of_rows = len(p_table_data) // len(alphabet)
    for i in range(count_of_rows):
        row = [f"P{i}"]
        for el in [_ for _ in p_table_data if _["from"] == f"P{i}"]:
            row.append(el["mask"])
        rows.append(row)
        table.add_row(row)
    print(table)

    # -------------- Допускает ли автомат слово -------------------
    print("\n\n Проверка: Допускает ли автомат введенное слово ('end' чтобы закончить)\n\n")

    while True:
        input_value = input("Введите слово: ")
        if input_value.replace(" ", "").lower() == 'end':
            break

        if check_word(input_value, p_start_vertex, p_end_vertex, p_table_data):
            print("ДА")
        else:
            print("НЕТ")


if __name__ == '__main__':
    main()