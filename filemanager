import os
import shutil

from cfg import main_dir
from cfg import list_cmds

current_dir = r''
main_path = main_dir
status = False


def menu():
    global current_dir
    global main_path
    while True:
        cmd = input('Введите команду (помощь - help): ').split()

        if cmd[0] == 'help':  
            print(list_cmds)

        elif cmd[0] == 'makedir':  
            try:
                create_dir(cmd[1])
            except Exception as e:
                print(e)
            except IndexError:
                print('Неверно введена команда!')

        elif cmd[0] == 'deldir':  
            try:
                delete_dir(cmd[1])
            except Exception as e:
                print(e)
            except:
                print('Неверно введена команда')

        elif cmd[0] == 'goto':  
            try:
                if cmd[1] == 'up':
                    if current_dir != main_path:
                        current_dir = '\\'.join(current_dir.split('\\')[:-1])
                        where()
                    else:
                        print('Вы не можете покинуть корневую папку!')
                else:
                    current_dir = main_path + '\\' + cmd[1]
                    where()
            except:
                print('Неверно введена команда')

        elif cmd[0] == 'makefile':
            try:
                mkfile(cmd[1])
            except IndexError:
                print('Неверно введена команда')
            except:
                print('Невозможно создать такой файл')

        elif cmd[0] == 'wrt':
            try:
                write(cmd[1], ' '.join(cmd[2:]))
            except:
                print('Неверно введена команда')

        elif cmd[0] == 'open':
            try:
                read(cmd[1])
            except Exception as e:
                print(e)
            except:
                print('Неверно введена команда')
        elif cmd[0] == 'del':
            try:
                rmfile(cmd[1])
            except Exception as e:
                print(e)
            except:
                print('Неверно введена команда')


        elif cmd[0] == 'copy':
            try:
                move_cp(cmd[1], cmd[2], cmd[3])
            except Exception as e:
                print(e)
            except:
                print('Неверно введена команда')

        elif cmd[0] == 'move':
            try:
                move(cmd[1], cmd[2])
            except Exception as e:
                print(e)
            except:
                print('Неверно введена команда')

        elif cmd[0] == 'rename':
            try:
                rename(cmd[1], cmd[2])
            except:
                print('Неверно введена команда')


        elif cmd[0] == 'where':
            where()


        elif cmd[0] == 'exit':
            break


        else:
            print('Неверная команда, введите заново!')


def create_dir(name):
    os.mkdir(current_dir + '\\' + name)


def delete_dir(name):
    os.rmdir(current_dir + '\\' + name)


def read(name):
    f = open(current_dir + '\\' + name, 'r')
    text = f.readlines()
    f.close()
    for i in text:
        print(i, end='')
    print()

def write(name, text):
    print(text)
    f = open(current_dir + '\\' + name, 'w')
    f.write(text)
    f.close()

def mkfile(name):
    my_file = open(current_dir + '\\' + name, "w+")


def rmfile(name):
    os.remove(current_dir + '\\' + name)


def rename(name, newname):
    os.rename(current_dir + '\\' + name, newname)


def move(name, path):
    shutil.move(current_dir + '\\' + name, current_dir + '\\' + path)


def move_cp(name, path, newname):
    shutil.copy(current_dir + '\\' + name, current_dir + '\\' + path)
    os.rename(current_dir + '\\' + path + '\\' + name, newname)


def where():
    print(f'Вы сейчас здесь {current_dir}')


if __name__ == "__main__":
    if main_path == r'' or not (os.path.exists(main_path)):
        status = False
        main_path = input('Введите корректный путь к файлу')
    else:
        status = True
        current_dir = main_dir
        menu()
