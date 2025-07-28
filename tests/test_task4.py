import pytest

from tasks import run_divisions


@pytest.mark.asyncio
async def test_run_divisions():
    result = await run_divisions()
    assert result == [5.0, "Ошибка деления", 2.0]
