"""
mkdir my_new_project
cd my_new_project

python3.12 -m venv venv
source venv/bin/activate

pip install package_name
pip freeze > requirements.txt
"""

import asyncio
from typing import Callable, List


type Vector2D[T] = tuple[T, T]
# Type alias for a function that takes a tuple[T, T] and returns an int
type VectorFunction[T] = Callable[[Vector2D[T]], int]


def add[T](vector: Vector2D[T]) -> int:
    """Adds two numbers."""
    return vector[0] + vector[1]


async def multiply(a: int, b: int) -> int:
    """Multiplies two numbers asynchronously."""
    await asyncio.sleep(0.1)  # Simulate an async operation
    return a * b


# Generic function that applies an operation on a list of integers
def reduce_vectors[T](vectors: List[Vector2D[T]], operation: VectorFunction[T]) -> List[int]:
    return [operation(vector) for vector in vectors]


# Generic async function that applies an operation on a list of items asynchronously
#async def apply_async_operation(items: List[T], operation: Callable[[T, T], T]) -> List[T]:
#    return [await asyncio.to_thread(operation, item, item) for item in items]


if __name__ == "__main__":
    print(add(3, 4))  # Output: 7
    result = asyncio.run(multiply(3, 4))
    print(result)  # Output: 12

    vectors: List[Vector2D[int]] = [
        (1, 1),
        (2, 2),
        (3, 3)
    ]

    print(reduce_vectors(vectors, add))  # Output: [2, 4, 6]
    
    #result = asyncio.run(apply_async_operation(numbers, multiply))
    #print(result)  # Output: [1, 4, 9, 16, 25]

