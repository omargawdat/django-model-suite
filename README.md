# Django Model Suite

[![PyPI version](https://badge.fury.io/py/django-model-suite.svg)](https://badge.fury.io/py/django-model-suite)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Django package that automatically generates standardized boilerplate code for your Django models following domain-driven design principles and best practices.

## Overview

Django Model Suite eliminates repetitive coding tasks by generating a complete suite of files for each model in your Django application. With a single command, you can create a fully-functional architecture including:

- **Admin Interface**: List views, change views, permissions, context providers, display configurations, and resources
- **REST API**: Serializers, views, URL configurations, filters, and pagination
- **Domain Logic**: Selectors, services, and validators
- **Field Definitions**: Clean field organization and management

## Features

- **One Command, Many Files**: Generate dozens of boilerplate files with a single command
- **Best Practices Baked In**: Follow domain-driven design and architectural best practices automatically
- **DRF Integration**: Complete REST API scaffolding with Django Rest Framework
- **Django Unfold Support**: Built-in support for the modern Django Unfold admin theme
- **Customizable**: Generate only the components you need
- **Clean Architecture**: Promotes separation of concerns and maintainable code structure
- **Time-Saving**: Eliminate hours of repetitive coding for each model

## Installation

```bash
pip install django-model-suite
```

Then add it to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'django_model_suite',
    # ...
]
```

## Requirements

- Python 3.8+
- Django 5.0+
- Django Unfold 0.45.0+
- Django Rest Framework 3.14.0+
- Django Filter 23.0+

## Usage

### Basic Usage

Generate all components for a model with a single command:

```bash
python manage.py generate_files <app_name> <model_name>
```

Example:

```bash
python manage.py generate_files users customer
```

### Selective Generation

Generate only specific components:

```bash
python manage.py generate_files <app_name> <model_name> --components admin api
```

Available component groups:
- `admin`: Admin interface files
- `domain`: Domain logic files (selectors, services, validators)
- `api`: REST API files

You can also specify individual components:
- `fields`: Field definitions
- `selectors`: Query selectors
- `services`: Business logic services
- `validators`: Data validation

### Configuration

Customize the package behavior in your project's `settings.py`:

```python
# Custom path for BaseModelAdmin (default: 'django_model_suite.admin')
BASE_MODEL_ADMIN_PATH = 'your_app.admin'
```

## Generated Structure

After running the command, your app will have the following structure:

```
your_app/
│
├─ fields/
│   └─ <model_name>.py                 # Field definitions
│
├─ admin/
│   └─ <model_name>/
│       ├─ __init__.py                 # Package initialization
│       ├─ admin.py                    # Main Admin registration
│       ├─ change_view.py              # Change view configuration
│       ├─ context.py                  # Context data providers
│       ├─ display.py                  # Display configuration
│       ├─ inline.py                   # Inline model configuration
│       ├─ list_view.py                # List view configuration
│       ├─ permissions.py              # Permission handling
│       └─ resource.py                 # Resource configuration
│
├─ api/
│   └─ <model_name>/
│       ├─ __init__.py                 # Package initialization
│       ├─ filters.py                  # API filtering options
│       ├─ pagination.py               # Custom pagination settings
│       ├─ serializers.py              # DRF serializers
│       ├─ urls.py                     # API URL routing
│       └─ views.py                    # API views and viewsets
│
└─ domain/
    ├─ selectors/
    │   └─ <model_name>.py             # Query logic
    ├─ services/
    │   └─ <model_name>.py             # Business logic
    └─ validators/
        └─ <model_name>.py             # Validation logic
```

## Benefits

- **Consistency**: Maintain a consistent code structure across your entire project
- **Productivity**: Focus on business logic rather than boilerplate code
- **Maintainability**: Cleanly organized code following best practices
- **Scalability**: Architecture designed to support project growth
- **Onboarding**: Easier onboarding for new developers with consistent patterns

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Omar Gawdat - [GitHub](https://github.com/omargawdat)