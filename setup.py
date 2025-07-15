from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)-> List[str]:
    """
    This function will return a list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
name="Machine_learning_project",
version='0.1.0',
author='NedRaph',
author_email='nedraphochieng@gmail.com', 
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)