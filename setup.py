from setuptools import find_packages # find all the packages in the entire application/project directory
from setuptools import setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


# Basic parameters setup/metadata to build the app/entire project as package
setup(
    name = 'mlProject',
    version = '0.0.1',
    author = 'Amlan',
    author_email = 'xdf.vtt@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
