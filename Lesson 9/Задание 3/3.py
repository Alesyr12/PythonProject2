def simple_process_file(input_filename, output_filename):

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for line in lines:
                line = line.strip()
                if not line:
                    output_file.write('\n')
                    continue

                words = line.lower().split()
                if not words:
                    output_file.write('\n')
                    continue

                # Считаем частоту слов
                word_count = {}
                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1

                # Находим самое частое слово
                max_count = 0
                most_common_word = ""

                for word, count in word_count.items():
                    if count > max_count:
                        max_count = count
                        most_common_word = word

                output_file.write(f"{most_common_word} {max_count}\n")

        print(f"Обработка завершена. Результат записан в файл: {output_filename}")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_filename}' не найден.")


# Использование
if __name__ == "__main__":
    input_file = "Text 3.txt"
    output_file = "output.txt"

    simple_process_file(input_file, output_file)