import importlib
import importlib.util
import os
import sys
from pathlib import Path

from django.apps import AppConfig
from django.apps import apps


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appss.core'

    def ready(self):
        # Loop over all installed apps
        for app_config in apps.get_app_configs():
            admin_dir = Path(app_config.path) / "admin"
            if admin_dir.is_dir():
                admin_pkg = f"{app_config.name}.admin"
                # If the admin package isn’t already in sys.modules,
                # create a dummy package so that the dotted module names can be resolved.
                if admin_pkg not in sys.modules:
                    spec = importlib.util.spec_from_loader(admin_pkg, loader=None, origin=str(admin_dir))
                    module = importlib.util.module_from_spec(spec)
                    # Make sure Python treats this as a package
                    module.__path__ = [str(admin_dir)]
                    sys.modules[admin_pkg] = module

                # Import all .py files in the admin directory (except __init__.py)
                for file in admin_dir.glob("*.py"):
                    if file.name != "__init__.py":
                        module_name = f"{admin_pkg}.{file.stem}"
                        importlib.import_module(module_name)

                # Now import .py files from subdirectories of admin
                for subdir in admin_dir.iterdir():
                    if subdir.is_dir():
                        sub_pkg = f"{admin_pkg}.{subdir.name}"
                        # If the subpackage isn’t in sys.modules (because, say, __init__.py is missing),
                        # register it as a namespace package.
                        if sub_pkg not in sys.modules:
                            spec = importlib.util.spec_from_loader(sub_pkg, loader=None, origin=str(subdir))
                            module = importlib.util.module_from_spec(spec)
                            module.__path__ = [str(subdir)]
                            sys.modules[sub_pkg] = module

                        for file in subdir.glob("*.py"):
                            if file.name != "__init__.py":
                                module_name = f"{sub_pkg}.{file.stem}"
                                importlib.import_module(module_name)

        # Import models in a similar way.
        for app_config in apps.get_app_configs():
            self.import_modules_from_directory(
                app_config.path,
                "models",
                app_config.name,
            )

    def import_modules_from_directory(self, base_path, subdirectory, app_name):
        directory_path = Path(base_path) / subdirectory
        if directory_path.exists():
            modules = [
                f[:-3]  # strip .py
                for f in os.listdir(directory_path)
                if f.endswith(".py") and not f.startswith("__")
            ]
            for module in modules:
                importlib.import_module(f"{app_name}.{subdirectory}.{module}")
