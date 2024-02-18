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
For details regarding `app-decision` and `decision-pipeline`, visit the respective project directories.


# Getting started

A Kubernetes cluster is required for running the platform. For testing purposes, set up a Kubernetes cluster on your local machine,
for example using [kind](https://kind.sigs.k8s.io/docs/user/quick-start/).
