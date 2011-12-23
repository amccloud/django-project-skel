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
```mkvirtualenv --no-site-packages {{ project_name }}-env```

#### For virtualenv ####
```virtualenv --no-site-packages {{ project_name }}-env```

```cd {{ project_name }}-env```

```source bin/activate```

### Clone the code ###
Obtain the url to your git repository.
```git clone <URL_TO_GIT_RESPOSITORY> {{ project_name }}```

### Install requirements ###
```cd {{ project_name }}```

```pip install -r requirements.txt```

### Configure project ###
```cp {{ project_name }}/__local_settings.py {{ project_name }}/local_settings.py```

```vi {{ project_name }}/local_settings.py```

### Sync database ###
```./manage.py syncdb```

## Running ##
```./manage.py runserver```

Open browser to 127.0.0.1:8000
