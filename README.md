# UmerArshad_DiceAssignment2
Github Actions Assignment

## Github repository
The Github repository is created for Assignment 2 here:
https://github.com/umerm64/UmerArshad_DiceAssignment2

The repository contains a simple flask application that handles certain routes.


## Workflow
The workflow file is present here:
https://github.com/umerm64/UmerArshad_DiceAssignment2/blob/main/.github/workflows/a2_build_test_deploy.yml

### Triggers
The workflow will run on the following events:
* push on `main` branch
* manual trigger (extra support)

### Jobs

#### Build and push
The first job(`job1_build_push_image`) builds and pushes the docker images to dockerHub under my profile (https://hub.docker.com/u/umerarshad123)

#### Test
The second job(`job2_test_app`) is responsible for testing the flask application by running unit tests (present in the file `test_app.py`)
This job is dependent upon the first job (`job1_build_push_image`)

#### Deploy
The third job is responsible to deploy the built docker image on a self-hosted runner. Any VM can be used as a self-hosted runner.
I have tried with the local Ubuntu VM and an AWS EC2 instance.

### Env variables
The dockerHub username and password are provided by repository secrets.\
`${{ secrets.docker_username }}`\
`${{ secrets.docker_password }}`

