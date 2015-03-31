#!/bin/bash
LD_LIBRARY_PATH='/opt/hdf5/lib/'
export LD_LIBRARY_PATH
source /home/super_jgreenleaf/undst/bin/activate
cd /home/super_jgreenleaf/undst
bin/python bin/gunicorn hello:app --bind 127.0.0.1:4000

#source /home/super_jgreenleaf/undst/bin/activate
#python -W ignore::DeprecationWarning bin/gunicorn hello:app --bind 127.0.0.1:4000

#/home/super_jgreenleaf/undst/bin/python /usr/local/bin/gunicorn hello:app --bind 127.0.0.1:4000 --log-level=debug --log-file /tmp/flask_via_gunicorn.log --error-logfile /tmp/flask_via_gunicorn.error.log