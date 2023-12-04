import os
import fnmatch

from typing import List
from setuptools import (
    find_packages,
    setup
)

# from pathutility._version import __version__
PKG_ROOT = os.path.dirname((os.path.abspath(__file__)))

def get_version() -> float:
    specs = {}
    version_var = '__version__'
    version_file = os.path.join(
        PKG_ROOT, c, '_version.py'
    )

    with open(version_file, 'r') as file:
        code = file.read()
        # Executing code to get the version variable
        exec(code, specs)
        try:
            version = specs[version_var]
        except KeyError:
            raise AttributeError(f'Cannot find {version_var} in {version_file}')
        else:
            return version

def get_requirements() -> List[str]:
    with open(os.path.join(PKG_ROOT, 'requirements.txt')) as f:
        req = filter(lambda x: x != '', [
                     x for x in f.read().splitlines() if '#' not in x])
    return list(req)


def get_package_data_files(pattern: str) -> List[str]:

    path = os.path.join(PKG_ROOT, 'decoratorsutility')

    if isinstance(pattern, str):
        pattern = [pattern]

    file_has_pattern = lambda file, wildcard: fnmatch.fnmatch(file, wildcard)

    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if any([file_has_pattern(name, pat) for pat in pattern]):
                result.append(os.path.join(root, name))
    return result

setup(
    name='decoratorsutility',
    version=get_version(),
    author='anglisanosa',
    author_email='marcanglisano@gmail.com',
    # url='https://github.com/anglisano/decoratorsutility.git',
    description='decorators utility',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(
        include=['decoratorsutility'+'.*', 'decoratorsutility']
    ),
    package_data={
        'decoratorsutility': [
            *get_package_data_files(pattern='*.yml'),
            *get_package_data_files(pattern='*.html'),
            *get_package_data_files(pattern='*.txt'),
        ]
    },
    install_requires=get_requirements(),
    python_requires='>=3.8',
    project_urls={
        'Documentation': 'https://anglisanosa.github.io/decoratorsutility/',
        'Bug Reports': 'https://github.com/anglisanosa/decoratorsutility/issues',
        'Source': 'https://github.com/anglisanosa/decoratorsutility',
    },
    license='',
)