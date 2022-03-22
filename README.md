# Django Real State

Web application for exploring real state listings.

## Instructions

You must have **python3** installed on your machine in order to run this project. You will aso need the packages specified in the requirements.txt file, instructions on that below.

Clone this repository by running:

```bash
git clone git@github.com:JorgePasco1/django-real-state.git
```

Move to the project home directory:

```bash
cd django-real-state
```

### Virtual env

Creating a virtual environment is recommended to avoid overwriting global installs of this project's dependencies.

To create a virtual env, create a `venv` folder inside the project's directory, and activate it, as follows:

```bash
python3 -m venv venv
. venv/bin/activate
```

**Note:** If you prefer using another tool to handle environments, like conda, you can create and activate a new environment with it.

### Envrionment Variables

Set up your env variables in a file named `.env`, there's an example file on `/btre/`.

### Running the project

Start the server by running:

```bash
python manage.py runserver
```
