import os
import platform
from pathlib import Path
import shutil


def main():
    # 1. Вывести имя вашей ОС
    os_name = platform.system()
    print(f"Имя операционной системы: {os_name}")

    # 2. Вывести путь до папки, в которой вы находитесь
    current_dir = Path.cwd()
    print(f"Текущий рабочий каталог: {current_dir}")

    # 3. Рассортировать файлы по расширениям
    # Словарь для группировки файлов по расширению
    extension_groups = {}
    # Словарь для хранения общей статистики по каждой группе
    stats = {}

    # Проходим по всем элементам в текущей директории
    for item in current_dir.iterdir():
        # Работаем только с файлами (игнорируем папки и этот скрипт)
        if item.is_file() and item.name != __file__:
            # Получаем расширение файла в нижнем регистре
            ext = item.suffix.lower()
            # Если расширения нет (например, файл .gitignore), используем "no_extension"
            if ext == '':
                ext = '.no_extension'

            # Добавляем файл в соответствующую группу
            if ext not in extension_groups:
                extension_groups[ext] = []
            extension_groups[ext].append(item)

    # Создаем папки и перемещаем файлы
    for ext, files in extension_groups.items():
        # Создаем имя для папки (убираем точку в начале)
        folder_name = ext[1:] if ext.startswith('.') else ext
        folder_path = current_dir / folder_name

        # Создаем папку, если ее еще нет
        folder_path.mkdir(exist_ok=True)

        total_size = 0
        moved_count = 0

        # Перемещаем каждый файл в соответствующую папку
        for file_path in files:
            try:
                # Перемещаем файл
                destination = folder_path / file_path.name
                shutil.move(str(file_path), str(destination))
                moved_count += 1
                total_size += destination.stat().st_size
            except Exception as e:
                print(f"Ошибка при перемещении файла {file_path}: {e}")

        # Сохраняем статистику для этой группы
        stats[ext] = {
            'count': moved_count,
            'total_size': total_size,
            'folder_path': folder_path
        }

        # Выводим сообщение о переносе
        if moved_count > 0:
            size_gb = total_size / (1024 ** 3)
            print(f"В папке с {folder_name} файлами перенесено {moved_count} файлов, "
                  f"их общий размер - {size_gb:.2f} гигабайт")

    # 4. Переименовать как минимум один файл
    # Ищем первую непустую папку с файлами
    for ext, stat_info in stats.items():
        folder_path = stat_info['folder_path']
        files_in_folder = list(folder_path.iterdir())

        if files_in_folder and any(file.is_file() for file in files_in_folder):
            # Берем первый файл в папке
            for file in files_in_folder:
                if file.is_file():
                    old_file = file
                    break

            # Создаем новое имя для файла
            old_name = old_file.name
            new_name = f"renamed_{old_name}"
            new_file = old_file.parent / new_name

            # Переименовываем файл
            try:
                old_file.rename(new_file)
                print(f"Файл {old_name} был переименован в {new_name}")
                break  # Переименовали один файл и выходим
            except Exception as e:
                print(f"Ошибка при переименовании файла {old_name}: {e}")
                break


if __name__ == "__main__":
    main()