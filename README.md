<div align="center">

<h1>Task Manager</h1>

[![Actions Status](https://github.com/SanichMakakich/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/SanichMakakich/python-project-52/actions)
[![Linter and Tests](https://github.com/SanichMyshkin/python-project-52/actions/workflows/django-test_and_lint.yml/badge.svg)](https://github.com/SanichMyshkin/python-project-52/actions/workflows/django-test_and_lint.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/9fbede7f94882cc43b8b/maintainability)](https://codeclimate.com/github/SanichMyshkin/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9fbede7f94882cc43b8b/test_coverage)](https://codeclimate.com/github/SanichMyshkin/python-project-52/test_coverage)

[![Deploy on Railway](https://railway.app/button.svg)](https://web-production-a9f18.up.railway.app/)

</div>

## About

A task management web application built with Python and [Django](https://www.djangoproject.com/) framework. It allows
you to set tasks, assign performers and change their statuses. Registration and authentication are required to work with
the system.

To provide users with a convenient, adaptive, modern interface, the project uses
the [Bootstrap](https://getbootstrap.com/) framework.

The frontend is rendered on the backend. This means that the page is built by the DjangoTemplates backend, which returns
prepared HTML. And this HTML is rendered by the server.

[PostgreSQL](https://www.postgresql.org/) is used as the object-relational database system.

### Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Bootstrap 4](https://getbootstrap.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Poetry](https://python-poetry.org/)
* [Gunicorn](https://gunicorn.org/)
* [Whitenoise](http://whitenoise.evans.io/en/latest/)
* [Rollbar](https://rollbar.com/)
* [Flake8](https://flake8.pycqa.org/en/latest/)

### Details

For **_user_** authentication, the standard Django tools are used. In this project, users will be authorized for all
actions, that is, everything is available to everyone.

Each task in the task manager usually has a **_status_**. With its help you can understand what is happening to the
task, whether it is done or not. Tasks can be, for example, in the following statuses: _new, in progress, in testing,
completed_.

**_Tasks_** are the main entity in any task manager. A task consists of a name and a description. Each task can have a
person to whom it is assigned. It is assumed that this person performs the task. Also, each task has mandatory fields -
author (set automatically when creating the task) and status.

**_Labels_** are a flexible alternative to categories. They allow you to group the tasks by different characteristics,
such as bugs, features, and so on. Labels are related to the task of relating many to many.

When the tasks become numerous, it becomes difficult to navigate through them. For this purpose, a *
*_filtering mechanism_** has been implemented, which has the ability to filter tasks by status, performer, label
presence, and has the ability to display tasks whose author is the current user.

---

## Installation

To install, you need to download the project to a convenient directory with the command:

```
git clone git@github.com:MyshkinSanich/python-project-52.git
```

next, you need to go to the directory itself using the command:

```
cd python-project-52
```

Create `.env` file in the root folder and add following variables:

```dotenv
DATABASE_URL=postgresql://{provider}://{user}:{password}@{host}:{port}/{db}
SECRET_KEY={your secret key} # Django will refuse to start if SECRET_KEY is not set
ROLL_BAR={your rolbar key}
```
Finally enter the installation command
```bash
>> make install
>> make migrate
```


---

## Usage

Start the Gunicorn Web-server by running:

```shell
>> make start
```

By default, the server will be available at http://0.0.0.0:8000.

It is also possible to start it local in development mode using:

```shell
>> make dev
```

### Makefile Commands

<dl>
    <dt><code>make install</code></dt>
    <dd>Install all dependencies of the package.</dd>
    <dt><code>make migrate</code></dt>
    <dd>Generate and apply database migrations.</dd>
    <dt><code>make dev</code></dt>
    <dd>Run Django development server at http://127.0.0.1:8000/</dd>
    <dt><code>make start</code></dt>
    <dd>Start the Gunicorn web server at http://0.0.0.0:8000 if no port is specified in the environment variables.</dd>
    <dt><code>make lint</code></dt>
    <dd>Check code with flake8 linter.</dd>
    <dt><code>make test</code></dt>
    <dd>Run tests.</dd>
    <dt><code>make shell</code></dt>
    <dd>Start Django shell (iPython REPL).</dd>
</dl>

---
> GitHub [@SanichMyshkin](https://github.com/SanichMyshkin) &nbsp;
> LinkedIn [@Myshkin Alexndr](https://www.linkedin.com)