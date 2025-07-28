# ДАНО:
# - Строка `text`
# - Целое или вещественное число `delay` — количество секунд задержки

# ЧТО НУЖНО СДЕЛАТЬ:
# - Создать асинхронную функцию `delayed_echo(text, delay)`, которая:
#     → делает паузу на `delay` секунд
#     → возвращает строку `text`

# - Создать функцию `echo_all()`, которая:
#     → запускает несколько вызовов `delayed_echo` параллельно
#     → собирает и возвращает их результаты в списке

# ПРИМЕР:
# >>> await echo_all()
# ['hello', 'world', '!']

import asyncio


async def delayed_echo(text, delay):
   pass

async def echo_all():
    pass
