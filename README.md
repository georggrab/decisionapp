This repository contains a simple Python app exposing a REST API `/decisions` returning random strings from a predefined selection, 
as well as the minimum necessary further configuration in order to achieve the following requirements:

* Means to automatically build (and test) Application containers
* CI/CD pipeline, courtesy of Github Actions, that builds, tests, and deploys new images to DockerHub
* High availability deployment to a Kubernetes cluster
* Automatically update the Kubernetes deployment whenever a new image is published to DockerHub by CI/CD

Furthermore, to showcase using the App, there is a simple `decision-pipeline` that:

* Periodically queries the deployment,
* Logs the data retrieved from the decision API.

The remainder of this document discusses the recommended way of setting up this repository and running it locally for testing.
For details regarding `app-decision`, visit the corresponding directory..


# Getting started

A Kubernetes cluster is required for running the platform. For testing purposes, set up a Kubernetes cluster on your local machine,
for example using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).

For the functionality of updating the Deployment of `app-decision` whenever a new image appears on DockerHub, install the 
[keel](https://keel.sh/) Kubernetes operator that automates this. The easiest way is using [helm](https://helm.sh/):

```bash
helm repo add keel https://charts.keel.sh 
helm repo update
helm upgrade --install keel --namespace=kube-system keel/keel
```

Once the Kubernetes cluster and the keel Operator are installed, apply the following `yaml` file to create the Deployment of our
`decision-app`, including a Service to expose it internally:

```
kubectl apply -f deployment-app-decision.yaml
```

You may verify using `kubectl get pods` that the deployment, with initially three replicas, is coming online as expected.

## CI/CD

CI/CD is [here on Github actions](https://github.com/georggrab/decisionapp/actions), defined through [this file](https://github.com/georggrab/decisionapp/blob/master/.github/workflows/docker-image.yml). This is a very simplified version of a pipeline that we might have triggered by pushes to the main branch or executed when pull requests are opened. The CI/CD builds and tests the Docker Image, and when that is successful, pushes a new `:latest` tag to Dockerhub, as well as a `0.0.x` tag that is continually incremented. The latter tag is then used by keel to detect a new image has appeared and to subsequently rollout a new deployment revision to the cluster.


## Executing the decision pipeline

To execute the decision pipeline, submit the script to the cluster by running

```
kubectl apply -f decision-pipeline.yaml
```


You can now watch the random decisions returned from the endpoint by executing:

```
kubectl logs decision-pipeline -f
```
