# Typer tutorial

import typer


def main(name: str,
         lastname: str = typer.Option("", help="Фамилия пользователя"),
         formal: bool = typer.Option(False,"--formal"  , "-f",
                                     help='Использовать формальное обращение'),

         ):
    """
    Говорит "привет" пользователю, опционально используя формальное обращение по ключу --formal
    :param lastname:
    :param name: обязательный
    :param formal:
    :return: None
    """
    if formal:
        print(f'Добрый день, {name} {lastname}!')
    else:
        print(f'Привет, {name} {lastname}!')


if __name__ == '__main__':
    typer.run(main)
