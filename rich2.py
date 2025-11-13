# Прогресс-бар при помощи rich
from rich.progress import track
from rich import print

import time

for step in track(range(20), description="Обработка данных"):
    time.sleep(0.5)

print("[bold green]Готово![/bold green]")

