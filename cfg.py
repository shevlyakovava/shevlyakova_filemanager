main_dir = r'' # СЮДА НУЖНО ВСТАВИТЬ ВАШУ ДИРЕКТОРИЮ

list_cmds = '''makedir <name> - Создание папки (с указанием имени);
deldir - Удаление папки по имени;
goto - Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;
makefile <name> - Создание пустых файлов с указанием имени;
wrt <name> - Запись текста в файл;
open <name> - Просмотр содержимого текстового файла;
del <name> - Удаление файлов по имени;
copy <file> <newname> <dir> - Копирование файлов из одной папки в другую;
move <file> <dir> - Перемещение файлов;
rename <file> <newname> - Переименование файлов.
where - узнать где находитесь.
\nexit - просто выход
'''
