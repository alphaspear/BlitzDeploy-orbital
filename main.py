# main.py

import os
import importlib
from fastapi import FastAPI

app = FastAPI()

def include_controllers(app):
    controller_dir = 'controller'
    for filename in os.listdir(controller_dir):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]
            module = importlib.import_module(f'{controller_dir}.{module_name}')
            if hasattr(module, 'router'):
                app.include_router(module.router)

include_controllers(app)
