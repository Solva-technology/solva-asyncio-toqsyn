# ЗАДАЧА 5: Параллельное выполнение и возврат первого результата

# ДАНО:
# - Несколько задач с разными временами выполнения:
#     → fast_task (0.1 сек)
#     → medium_task (0.3 сек)
#     → slow_task (1 сек)

# ЧТО НУЖНО СДЕЛАТЬ:
# - Написать функцию `first_complete()`, которая:
#     → запускает все задачи параллельно
#     → ждет, пока завершится хотя бы одна из них
#     → возвращает результат самой первой завершившейся

# ПОДСКАЗКА:
# Используйте:
#   `done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)`
import asyncio


async def fast_task():
    pass

async def medium_task():
    pass

async def slow_task():
    pass

async def first_complete():
    pass
