# build and install HDF5

# set where HDF5 will be installed; this is needed for pytables and is used in the configuration line for HDF5 below
export HDF5_DIR=/opt/hdf5

# download, configure and install HDF5
curl -O 'http://www.hdfgroup.org/ftp/HDF5/current/src/hdf5-1.8.13.tar.bz2'
tar xjf hdf5-1.8.13.tar.bz2
cd hdf5-1.8.13
./configure --prefix=${HDF5_DIR}
make && sudo make install

# install tables

# the CLANG compiler will abort the compilation when there are unused command line arguments
# unless set, pytables will not compile
export ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future

pip install tables