import pytest

from tasks import limited_runner


@pytest.mark.asyncio
async def test_limited_runner():
    result = await limited_runner()
    assert result == [0, 1, 2, 3, 4]
