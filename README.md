[![CI](https://github.com/nogibjj/706_Week06_YL/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/706_Week06_YL/actions/workflows/cicd.yml)

# 706_Week06_YL

This repository includes the main tasks for Week 6:

* `Makefile` is a configuration file used in Unix-based systems for automating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.
* `.devcontainer` includes a Dockerfile and `devcontainer.json`. The `Dockerfile` within this folder specifies how the container should be built, and other settings in this directory may control development environment configurations.
* `Workflows` includes GitHub Actions, which contain configuration files for setting up automated build, test, and deployment pipelines for your project.
* `.gitignore` is used to specify which files or directories should be excluded from version control when using Git.
* `README.md` is the instruction file for the readers.
* `main.py` is a Python file that contains the main function.
* `test_main.py`  is a test file for `descriptive.py` that can successfully run in IDEs.
* `requirements.txt` is to specify the dependencies (libraries and packages) required to run the project.
* `mylib` contains the script for extracting, querying, transforming and loading the database: `extract.py`, `query.py`, `transform_load.py`
* `query.md` contains the query to be executed, including join, aggregate, and sort operations.

## Project description

* Connect to a SQL Databricks database using `databricks` module
* Design a SQL query involving joins, aggregation, and sorting
* Provide explanations for the query logic and the result

## Project environment

* Use codespace for scripting
* Container built in `devcontainers` and virtual environment activated via `requirements.txt`
* To run the code, use the command `python main.py` in the terminal
* After the launching the workspace in Azure Databricks, I got a database named `default`. Then I retrive `SERVER_HOSTNAME`, `HTTP_PATH` and `TOKEN` from `SQL-WAREHOUSES`. I store them in a hidden `.env` file here and use these them in my `load` function to connect to Databricks. I also store them in `Action` under `Secrets and Variables` in the repo `Settings`.

## Query explanation & expected results

The query returns the total number of match played for the women world cup, group by countries.
![Alt text](figures/res.png)

## Check format & errors

1. make format

2. make lint

3. make test

## Reference

https://github.com/nogibjj/sqlite-lab