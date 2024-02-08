import os
from pathlib import Path
import logging

#logging String

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(mesaage)s:')

project_name='cnnClassifier'

list_of_files=[
    '.github/workflow/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py'
    'Config/cofig.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'templates/index.html'
]