# Typer tutorial
# Also demonstrates rich text module

import typer
from rich import print


def main(name: str,
         lastname: str = typer.Option("", help="Фамилия пользователя"),
         age: int = typer.Option(0, "--age", "-a", help="Указать возраст"),
         formal: bool = typer.Option(False, "--formal", "-f",
                                     help='Использовать формальное обращение'),

         ):
    """
    Говорит "привет" пользователю, опционально показывая возраст, если выбран формальный стиль
    :param age: int
    :param lastname: необязательныйы
    :param name: обязательный
    :param formal:
    :return: None
    """
    if formal:

        if age in range(0, 6):
            print(f"Привет, {name}!")
            print("[bold green]Ты ребёнок![/bold green]")
        elif age in range(6, 13):
            print(f"Привет, {name}!")
            print("[bold green]Ты всё ещё ребёнок![/bold green]")
        elif age in range(13, 21):
            print(f"Привет, {name} {lastname}!")
            print("[bold yellow]Ты подросток[/bold yellow]")
        elif age in range(21, 60):
            print(f"Добрый день, {name} {lastname}!")
            print("[bold red]Вы уже взрослый человек![/bold red]")
        elif age in range(60, 100):
            print(f"Добрый день, {name} {lastname}!")
            print("[bold red]Вы уже пожилой человек![/bold red]")
        else:
            print(f"[bold red]Шанс прожить {age} лет слишком мал в наше время![/bold red]")

    else:
        print(f'Привет, {name} {lastname}!')


if __name__ == '__main__':
    typer.run(main)
