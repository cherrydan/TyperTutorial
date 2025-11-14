# site-checker.py is CLI-application
# to show site availability

import typer
import requests
from typing import List
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()


def get_status_emoji(status_code: int) -> str:
    """

    :param status_code:
    :return: text string with emoji
    """
    if 200 <= status_code < 300:
        return "200 OK! "
    elif 300 <= status_code < 400:
        return "300 REDIRECT "
    elif 400 <= status_code < 500:
        return "400 CLIENT_ERROR "
    elif 500 <= status_code < 600:
        return "500 SERVER_ERROR"
    else:
        return "UNKNOWN ERROR"


def main(urls: List[str] = typer.Argument(..., help="Список urls для проверки")):
    """
    Проверяет доступность сайтов, переданных в виде аргумента
    :param urls: урлы сайтов в строку через пробел

    Выводит данные в виде таблицы
    """
    table = Table(title="Результаты прозвона сайтов")
    table.add_column("URL", style="cyan", no_wrap=True)
    table.add_column("Статус-код", justify="center")
    table.add_column("Результат", justify="right", style="green")

    for url in track(urls, description="Проверка сайтов..."):
        try:
            response = requests.get(url, timeout=5)
            status_code = response.status_code
            status_text = get_status_emoji(status_code)
            row_style = ""
            if 300 <= status_code < 400:
                row_style = "yellow"
            elif status_code >= 400:
                row_style = "red"
            table.add_row(url, str(status_code), status_text, style=row_style)
        except requests.exceptions.RequestException as e:
            table.add_row(url, "N/A", f"ERROR {e.__class__.__name__}", style="bold red")
    console.print(table)



if __name__ == '__main__':
    typer.run(main)
