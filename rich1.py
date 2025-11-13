# составление таблиц при помощи Rich
from rich import print
from rich.table import Table

table = Table(title="Список моих любимых фреймворков")

table.add_column("Название", justify="left", style="cyan", no_wrap=True)
table.add_column("Язык", style="magenta")
table.add_column("Для чего", justify="right", style="green")

table.add_row("Fast-API", "Python", "Web-API")
table.add_row("React", "JavaScript", "Frontend")
table.add_row("Typer", "Python", "CLI-apps")

print(table)
