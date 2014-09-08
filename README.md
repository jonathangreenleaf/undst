undst
=====

simple api to retrieve data from data.h5<br>
this covers the installation requirements

*virtualenv --no-site-packages undst
*cd undst/
*source bin/activate

*pip install flask
Successfully installed flask itsdangerous Jinja2 markupsafe Werkzeug

*pip install numpy
takes about 10min
Successfully installed numpy

*pip install pandas
forced reboot of my 300MB VPS the 1st time - 2nd time seemed to work:
Successfully installed pandas python-dateutil pytz six

almost done, for ImportError: HDFStore requires PyTables
*pip install tables
ERROR:: You need numexpr 2.0.0 or greater to run PyTables!

ok, try upgrade
*pip install --upgrade numexpr

Successfully installed numexpr numpy
note:
Found numpy 1.9.0 package installed.
Found numexpr 2.4 package installed.

*pip install tables
ERROR:: You need Cython 0.13 or greater to compile PyTables!
*pip install --upgrade cython
Successfully installed cython

Ok now try to pip install tables
ERROR:: Could not find a local HDF5 installation.

need this:  https://gist.github.com/rca/b6e5d22c2c4149ea315d
*chmod u+x hdf5_tables_install.sh
*sh hdf5_tables_install.sh
Successfully installed tables

still throws ImportError: HDFStore requires PyTables
error even though in pip freeze!

server needs pointer to LD_LIBRARY_PATH
add this line to /etc/environment:
LD_LIBRARY_PATH=/opt/hdf5/lib/
validate there:
*echo $LD_LIBRARY_PATH
should return /opt/hdf5/lib/
all set with requirements at this point


