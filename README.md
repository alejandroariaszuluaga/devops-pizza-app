# DevOps Pizza App

The following Django based application consists of two main parts:
1. Order Placement Form: A form that allows users to place orders for pizza. This form
should include:
a. A dropdown menu for selecting the type of pizza (e.g., Margherita, Pepperoni,
Vegetarian, etc.).
b. A text area for comments or special instructions.
2. Orders Table: A page that displays all placed orders in a tabular format. Each row
should display the type of pizza ordered and any comments associated with the order.

## Required CLI tools:
- Docker
- Minikube
- 

## Running Container Locally

To run this container app locally the following commands:

```shell
docker build -t django-pizza-app .
docker run -p 8000:8000 django-pizza-app
```

## Running on Minikube

For this initial setup, Minikube [1] was selected to run this application locally. Any other Kubernetes provider can be used (EKS, GKE, ...) if decided to move to a Production workload.

1. Install the Minikube CLI tool, for MacOS run:
```shell
brew install minikube
```

2. Start and activate Minikube env, this will also point your local `kubectl` profile to the Minikube cluster:
```shell
minikube 
eval $(minikube docker-env)
```

Now there are two options to run this test, if any local testing is needed, the Minikube registry can be used

3. A Deploy image locally to Minikube registry

    1. Enable Minikube Registry add-on:
    ```shell
    minikube addons enable registry
    ```

    2. Build Docker image:
    ```shell
    docker build -t django-pizza-app .
    ```

    3. Tag and push the image to Minikube:
    ```shell
    docker tag django-pizza-app:latest localhost:5000/django-pizza-app:latest
    docker push localhost:5000/django-pizza-app:latest
    ```

    4. Set `k8s/deployment.yaml` `image` value to: `localhost:5000/django-pizza-app:latest`

3. B Use DockerHub image

    1. Make an update on one of the following directories: `pizza_app` or `orders`, or on the `Dockefile`, make a PR and once merged it will trigger a CI pipeline that will build and push the image to `alejandroariaszuluaga/django-pizza-app` DockerHub.

    2. Set `k8s/deployment.yaml` `image` value to: `alejandroariaszuluaga/django-pizza-app:latest`



4. Apply Kubernetes manifests:
```shell
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

5. Port-forward the app to localhost:
```shell
kubectl port-forward svc/django-pizza-app-service 8000:8000
```

6. Access the app through your local browser at http://localhost:8000/



# References
1. https://minikube.sigs.k8s.io/docs/
