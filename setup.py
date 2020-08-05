from setuptools import setup, find_packages
from codecs import open
from os import path
from pathlib import PurePath, Path


__version__ = '0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

entry_point_path = 'xicam.databrowser'

setup(
    name='xicam.databrowser',
    version=__version__,
    description='Data browser plugin for xicam',
    long_description=long_description,
    url='github.com/tangkong/Xi-cam.databrowser',
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='Xi-cam, plugin',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='roberttk',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='roberttk@slac.stanford.edu',
    entry_points={'xicam.plugins.GUIPlugin': [
        f'databrowser = {entry_point_path}:DataBrowserPlugin'
    ]}

    # for entry points: {packagename}
    # package name = databrowser
    # class name = DataBrowserPlugin
    # display name = Data Browser (not used)
)
