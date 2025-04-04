# Django Model Suite File Generator

This project provides a custom Django management command that automatically generates boilerplate files for a specified
model within a Django application. It creates admin configurations (list view, change view, permissions, context,
displays), API files (serializers, views, URLs, filters, pagination), domain files (selectors, services, validators),
and field definitions—all tailored for the given model.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [How It Works](#how-it-works)
5. [File Structure](#file-structure)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features

- **Automated file generation**: With a single command, generate all necessary boilerplate files for a model.
- **Extensible**: Easily add or modify generators to customize the files you want to create.
- **Organized output**: Automatically places generated files in logical paths under your app (e.g., `admin/<model>/`,
  `api/<model>/`, `domain/selectors/`, etc.).

---

## Installation

1. install the package

```aiignore
pip install django-model-suite
```

2. **Add to `INSTALLED_APPS`**: Make sure the app containing this management command (and the `django_model_suite` if
   it's a separate app) is listed in your `INSTALLED_APPS` in `settings.py`:

   ```python
   INSTALLED_APPS = [
       # ...
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    "django.contrib.admin",  # required
    'django_model_suite',
       # ...
   ]
   ```

3. **Optional Configuration**: You can customize the following settings in your `settings.py`:

   ```python
   # Custom path for BaseModelAdmin (default: 'django_model_suite.admin')
   BASE_MODEL_ADMIN_PATH = 'your_app.admin'
   ```

---

## Usage

1. **Run the command** to generate files for a specific model

   ```bash
    python manage.py generate_files <app_name> <model_name> --components admin domain api
    ```
   example: 
   ```bash
    python manage.py generate_files users customer
    ```

---

## How It Works

The command uses several generator classes (e.g., `FieldsGenerator`, `ListViewGenerator`, `SerializerGenerator`, etc.)
each responsible for creating a specific part of the Django scaffolding. Once you call:

python manage.py generate_files <app_name> <model_name>

The command:

1. **Resolves the app path** based on the `app_name` provided.
2. **Retrieves the list of fields** for the specified `model_name`.
3. **Iterates over a predefined list of components** (e.g., `fields`, `admin`, `api`, `selectors`, `services`,
   `validators`).
4. **Generates boilerplate files** in each of these sections by calling the respective generators with the model name,
   app name, and field definitions.

---

## File Structure

After running the command, you'll typically see the following structure in your app (depending on which components the
script generates):

```
your_app/
│
├─ fields/
│   └─ fields_<model_name>.py               (Generated fields definitions)
│
├─ admin/
│   └─ <model_name>/
│       ├─ list_view_<model_name>.py        (List view for model in Django admin)
│       ├─ change_view_<model_name>.py      (Change view for model in Django admin)
│       ├─ permissions_<model_name>.py      (Permissions handling in admin)
│       ├─ context_<model_name>.py          (Context data for admin templates)
│       ├─ display_<model_name>.py          (Display logic for admin list/change)
│       └─ admin_<model_name>.py            (Main Admin registration)
│
├─ api/
│   └─ <model_name>/
│       ├─ serializer_<model_name>.py       (Django Rest Framework serializer)
│       ├─ view_<model_name>.py             (ViewSets or API views)
│       ├─ url_<model_name>.py              (API URL configurations)
│       ├─ filter_<model_name>.py           (Filter classes for the model API)
│       └─ pagination_<model_name>.py       (Pagination settings for the model API)
│
└─ domain/
    ├─ selectors/
    │   └─ selector_<model_name>.py          (Query logic)
    ├─ services/
    │   └─ service_<model_name>.py           (Business logic services)
    └─ validators/
        └─ validator_<model_name>.py         (Validation logic)
```

You can then import and integrate these files as needed in your Django project.

---

## Next Features

- **Inline Template**: Inline should be use the field permissions.
- **Field Permissions**: Should include users, show_in_creating, other_conditions
- **Custom BaseModelAdmin Path**: Configure the import path for BaseModelAdmin in your settings.
- 