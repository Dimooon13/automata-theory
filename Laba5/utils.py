import logging

def get_d_data(
        start_vertex: list[str],
        end_vertex: list[str],
        alphabet: list[str],
        table_data: list[dict[str]]
) -> tuple[list[str], list[str], list[dict[str]]]:
    p_table_data: list[dict[str]] = []
    queue = [{"index": 0, "data": start_vertex}]
    p_start_vertex = ["P0"]
    p_end_vertex = []

    index = 0
    while queue:
        current_p = queue.pop(0)
        p_index = current_p["index"]
        logging.info(f"> P{p_index} = {current_p['data']}")

        if current_p["data"]:
            for el in end_vertex:
                if el in current_p["data"]:
                    p_end_vertex.append(f"P{p_index}")
                    break

        for symbol in alphabet:
            new_p_data = list()
            for s in current_p["data"]:
                d_row: dict = [row for row in table_data if row["from"] == s][0]
                data = d_row["to"][alphabet.index(symbol)]
                if data is None:
                    continue
                if type(data) is list:
                    for el in data:
                        if el not in new_p_data:
                            new_p_data.append(el)
                else:
                    new_p_data.append(data)
                logging.info(f"\t({s}; {symbol})-> {data}")

            if not new_p_data:
                logging.info(f"(P{p_index}; {symbol})-> ∅")
                p_table_data.append({"from": f'P{p_index}', "to": new_p_data, "mask": f"∅", "symbol": symbol})
                continue

            if new_p_data in [p["to"] for p in p_table_data]:
                view_index = int([p["mask"] for p in p_table_data if p["to"] == new_p_data][0][1:])
            else:
                index += 1
                view_index = index

                if new_p_data and view_index not in [p["index"] for p in queue]:
                    queue.append({"index": view_index, "data": new_p_data})

            logging.info(f"(P{p_index}; {symbol})-> {new_p_data} == P{view_index}")

            p_table_data.append({"from": f'P{p_index}', "to": new_p_data, "mask": f"P{view_index}", "symbol": symbol})

    return p_start_vertex, p_end_vertex, p_table_data


def check_word(input_value, p_start_vertex, p_end_vertex, p_table_data):
    current_p = p_start_vertex[0]
    for symbol in input_value:
        row = [row for row in p_table_data if row["from"] == current_p and row["symbol"] == symbol][0]
        if row["mask"] == "∅":
            return False
        current_p = row["mask"]
    return current_p in p_end_vertex


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