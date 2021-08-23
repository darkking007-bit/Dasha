import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"Dasha/Modules/{plugin_name}.py")
    name = "Dasha.Modules.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Dasha.Modules." + plugin_name] = load
    print("Dasha has Imported " + plugin_name)
