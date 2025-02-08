from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django-model-generator",
    version="0.1.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Django app for generating boilerplate code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/django-model-generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Django>=3.2",
        "django-unfold>=0.5.0",
        "djangorestframework>=3.14.0",
        "django-filter>=23.0",
    ],
)