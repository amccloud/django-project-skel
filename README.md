# {{ project_name|title }} Django Project #
## Prerequisites ##

- python >= 2.5
- pip
- virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python enviroment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages {{ project_name }}-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages {{ project_name }}-env
cd {{ project_name }}-env
source bin/activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_THIS_GIT_RESPOSITORY>
```

### Install requirements ###
```bash
cd django-project-skel
pip install -r requirements.txt
```

### Configure project ###
```bash
django-admin.py startproject --template=./django-project-skel {{ project_name }}
```

### Sync database ###
```bash
python manage.py syncdb
python manage.py migrate
```

## Running ##
```bash
python manage.py runserver
```

Open browser to http://127.0.0.1:8000
