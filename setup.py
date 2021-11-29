from setuptools import setup
import datetime

DATE = datetime.datetime.now()

setup(name='elevator-task',
    version='0.0.4',
    description='Elevator project',
    url='https://github.com/a0morshna/elevator-task.git',
    author='Morshna Alexandra',
    keywords='package',
    install_requires=[],
    include_package_data=True,
    setup_requires=['wheel'],
    zip_safe=False)