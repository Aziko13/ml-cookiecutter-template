# ml-cookiecutter-template

This repository contains cookiecutter template for ML/DS projects


## Requirements to use the cookiecutter template

* Python 2.7 or 3.5+
* Cookiecutter Python package >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

```
$ pip install cookiecutter
```

or

```
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

##  To start a new project

* Navigate to a repository where you want to create a new ML/DS project
* Run `cookiecutter https://github.com/Aziko13/ml-cookiecutter-template.git`
* Cookiecutter will ask some questions and then will create repos skeleton

## The resulting directory structure 
```
├── docs               <- Open-source license if one is chosen
│   ├── Makefile       <- Makefile with convenience commands like `make setup` or `make test`
├── kubeflow           <- Kueflow pipeliens scripts
├── models             <- Trained models
├── notebooks          <- Jupyter notebooks
├── scripts            <- Scripts
├── src                <- Source code
│   ├── configs        <- Configs to run pipelines/scripts
│   │   ├── dev        <- Development environment configs
│   │   ├── prd        <- Production environment configs
│   ├── data           <- Source data
│   ├── features       <- Code to create features for modeling
│   ├── logs           <- Logs
│   ├── models         <- Model classes
│   ├── tests          <- Tests
│   ├── utils          <- Helpers functions
├── .gitignore         <- Git ingonre file
├── Dockerfile         <- Docker file
├── README.md          <- The top-level README for developers using this project.
```