import datetime
import os

path_dec = os.getcwd()


def dec(path):

    def logger(foo):

        def new_foo(*args, **kwargs):

            dt = datetime.datetime.now().strftime('%d.%m.%y | %H:%M:%S')
            res = foo(*args, **kwargs)

            if len(args) == 0:
                args = 'отсутствуют'
            if len(kwargs) == 0:
                kwargs = 'отсутствуют'
            if res is None:
                res = 'отсутствует'

            with open(f'{path}\\log_file.txt', 'a', encoding='utf-8') as f:
                f.write(f'\n{"*" * 79}\n'
                        f'<<{str(dt)}>>\n'
                        f'Вызвана функция: "{foo.__name__}"\n'
                        f'Аргументы: {args}\n'
                        f'Именованные аргументы: {kwargs}.\n'
                        f'Результат выполнения функции: {res}')

            return res
        return new_foo
    return logger
