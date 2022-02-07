FROM python:3

COPY /code /code 

COPY setup.py ./

RUN pip install wheel && pip install setuptools && pip install packaging && pip install appdirs

RUN python3 setup.py sdist bdist_wheel

