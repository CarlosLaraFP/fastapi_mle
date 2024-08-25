import pytest
# import asyncio
from main import add, multiply, reduce_vectors


def test_add():
    assert add((3, 4)) == 7
    assert add((-1, 1)) == 0
    assert add((0, 0)) == 0


def test_apply_operation():
    vectors = [
        (1, 1),
        (2, 2),
        (3, 3)
    ]

    result = reduce_vectors(vectors, add)

    assert result == [2, 4, 6]


# decorator used to mark this test function as an asynchronous test
@pytest.mark.asyncio
async def test_multiply():
    result = await multiply(3, 4)
    assert result == 12

    result = await multiply(-1, 1)
    assert result == -1

    result = await multiply(0, 100)
    assert result == 0
