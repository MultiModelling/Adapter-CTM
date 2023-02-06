# MMvIB CTM price profile adapter

The project is based on TNO's Flask REST API template. For more information, see below.

## To deploy Minio
Branch Minio from the Mutlimodelling organisation
Use: `docker-compose build` to build the image
Run the image using `docker-compose up -d`.

## Test the model adapter locally

1. create a ```.env``` file based on the ```.env.template``` file by coopying ```.env.template``` and uncommenting all except the last line
2. run 'pip install -e .' to install required packages
3. run the ```test_ctm.py``` application from the Adapter-CTM directory

## Flask REST API Template

This is a skeleton application for a REST API. It contains a modular setup that should prevent annoying circular imports
that are sometimes an issue when scaling up Flask applications. It also contains a
generic library of code developed in other projects (under tno/shared).

The key dependencies are:

- [Flask-smorest](https://flask-smorest.readthedocs.io): A REST API framework built on top
  of [marshmallow](https://marshmallow.readthedocs.io/).
