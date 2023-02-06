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
