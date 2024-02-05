from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

requirements_file_path = "requirements_dev.txt"

setup(
    name="Xray",
    version="0.0.1",
    author="Vinit",
    author_email="vinit.londhe21@gmail.com",
    install_requires=get_requirements(requirements_file_path),
    package_dir={"": "Xray"},
    packages=find_packages(where="Xray")
)