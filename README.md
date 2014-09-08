undst
=====

simple api to retrieve data from data.h5<br>
this covers the installation requirements

*virtualenv --no-site-packages undst*
*cd undst/*
*source bin/activate*

*pip install flask*<br>
Successfully installed flask itsdangerous Jinja2 markupsafe Werkzeug

*pip install numpy*<br>
takes about 10min<br>
Successfully installed numpy

*pip install pandas*<br>
forced reboot of my 300MB VPS the 1st time - 2nd time seemed to work:

Successfully installed pandas python-dateutil pytz six<br>
almost done, for ImportError: HDFStore requires PyTables
*pip install tables*<br>
ERROR:: You need numexpr 2.0.0 or greater to run PyTables!

ok, try upgrade

*pip install --upgrade numexpr*<br>

Successfully installed numexpr numpy
<br>
note:
Found numpy 1.9.0 package installed.
<br>
Found numexpr 2.4 package installed.

*pip install tables*<br>
ERROR:: You need Cython 0.13 or greater to compile PyTables!

*pip install --upgrade cython*<br>
Successfully installed cython
<br>
Ok now try to pip install tables
<br>
ERROR:: Could not find a local HDF5 installation.

need this:  https://gist.github.com/rca/b6e5d22c2c4149ea315d
*chmod u+x hdf5_tables_install.sh*<br>
*sh hdf5_tables_install.sh*<br>
Successfully installed tables
<br>
still throws ImportError: HDFStore requires PyTables

error even though in pip freeze!
<br>
server needs pointer to LD_LIBRARY_PATH
<br>
add this line to /etc/environment:

LD_LIBRARY_PATH=/opt/hdf5/lib/

validate there:
*echo $LD_LIBRARY_PATH*<br>
should return /opt/hdf5/lib/<br>
all set with requirements at this point


