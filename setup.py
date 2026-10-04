from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()

        requirement_lst = []

        for line in lines:
            requirement = line.strip()

            if requirement and requirement != "-e .":
                requirement_lst.append(requirement)

        return requirement_lst

    except FileNotFoundError:
        print("requirements.txt file not found.")
        return []


setup(
    name="network-security",
    version="0.0.1",
    author="Dimple",
    author_email = "bhdimple06@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)