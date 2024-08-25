"""
mkdir my_new_project
cd my_new_project

python3.12 -m venv venv
source venv/bin/activate

pip install package_name
pip freeze > requirements.txt

docker build -t fastapi_app .
docker run --name fastapi_container -p 8000:80 fastapi_app
docker stop fastapi_container
docker rm fastapi_container

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# You can access the FastAPI app via the NodePort. Open the app in your browser using http://<minikube_ip>:30000.
minikube ip

kubectl delete -f deployment.yaml
kubectl delete -f service.yaml

kubectl get pods
kubectl describe pod pod_name
kubectl get svc
minikube service fastapi-service --url

After rebuilding the image, you can simply update the deployment without deleting it. 
Kubernetes will detect the new image and replace the old pods with new ones running the updated code.
This command tells Kubernetes to restart the pods in your deployment, pulling the updated image:

kubectl rollout restart deployment fastapi-deployment


docker run: This command is used to create and start a new Docker container from an image.

--name fastapi_container: This option names the container fastapi_container. Naming a container makes it easier to reference it in future Docker commands (like stopping or removing it).

-p 8000:80: This option maps port 8000 on the host machine to port 80 inside the container.

Port 8000 (host): The port you use to access your FastAPI application from your browser or API client.
Port 80 (container): The port the application is listening on inside the container. In the Dockerfile, the EXPOSE 80 command specifies this internal port.
fastapi_app: This is the name of the Docker image from which the container is created. This image must already exist, either locally (created via docker build) or available from a Docker registry.
"""

import asyncio
from typing import Callable, List
from fastapi import FastAPI
import uvicorn


app = FastAPI()

type Vector2D[T] = tuple[T, T]
# Type alias for a function that takes a tuple[T, T] and returns an int
type VectorFunction[T] = Callable[[Vector2D[T]], int]


def add[T](vector: Vector2D[T]) -> int:
    """Adds two numbers."""
    return vector[0] + vector[1]


# Generic function that applies an operation on a list of integers
def reduce_vectors[T](vectors: List[Vector2D[T]], operation: VectorFunction[T]) -> List[int]:
    return [operation(vector) for vector in vectors]


# Generic async function that applies an operation on a list of items asynchronously
#async def apply_async_operation(items: List[T], operation: Callable[[T, T], T]) -> List[T]:
#    return [await asyncio.to_thread(operation, item, item) for item in items]


@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}


@app.get("/multiply/{a}/{b}")
async def multiply(a: int, b: int) -> int:
    """Multiplies two numbers asynchronously."""
    await asyncio.sleep(0.1)  # Simulate an async operation
    return a * b


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

    """
    vector = (3, 4)

    print(add(vector))  # Output: 7

    result = asyncio.run(multiply(3, 4))

    print(result)  # Output: 12

    vectors: List[Vector2D[int]] = [
        (1, 1),
        (2, 2),
        (3, 3)
    ]

    print(reduce_vectors(vectors, add))  # Output: [2, 4, 6]
    """

    #result = asyncio.run(apply_async_operation(numbers, multiply))
    #print(result)  # Output: [1, 4, 9, 16, 25]
