# Minimal sysconfigdata for embedded McRogueFace Python
# This provides the build_time_vars needed by sysconfig module

import sys
import os

# Get the actual prefix from sys.prefix (set by McRogueFace at init)
_prefix = os.path.normpath(sys.prefix)

build_time_vars = {
    # Core paths
    'prefix': _prefix,
    'exec_prefix': _prefix,
    'LIBDIR': os.path.join(_prefix, 'lib'),
    'LIBDEST': os.path.join(_prefix, 'Lib'),
    'BINLIBDEST': os.path.join(_prefix, 'Lib'),
    'BINDIR': os.path.dirname(sys.executable),
    'INCLUDEPY': os.path.join(_prefix, 'include'),
    'INCLUDEDIR': os.path.join(_prefix, 'include'),
    'CONFINCLUDEDIR': os.path.join(_prefix, 'include'),
    'CONFINCLUDEPY': os.path.join(_prefix, 'include'),
    'LIBPC': os.path.join(_prefix, 'lib', 'pkgconfig'),
    'DESTLIB': os.path.join(_prefix, 'Lib'),
    'DESTSHARED': os.path.join(_prefix, 'lib'),

    # Version info
    'VERSION': f'{sys.version_info[0]}.{sys.version_info[1]}',
    'py_version': f'{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}',
    'py_version_short': f'{sys.version_info[0]}.{sys.version_info[1]}',
    'py_version_nodot': f'{sys.version_info[0]}{sys.version_info[1]}',

    # ABI info
    'ABIFLAGS': getattr(sys, 'abiflags', ''),
    'EXT_SUFFIX': '.cpython-314-x86_64-linux-gnu.so',
    'SOABI': 'cpython-314-x86_64-linux-gnu',
    'Py_DEBUG': 0,
    'Py_GIL_DISABLED': 0,

    # Platform info
    'platlibdir': 'lib',
    'MULTIARCH': 'x86_64-linux-gnu',
    'HOST_GNU_TYPE': 'x86_64-linux-gnu',
    'BUILD_GNU_TYPE': 'x86_64-pc-linux-gnu',

    # Host prefix (for cross-compilation scenarios, same as prefix for native)
    'host_prefix': _prefix,
    'host_exec_prefix': _prefix,

    # Additional commonly needed vars
    'LDLIBRARY': 'libpython3.14.so',
    'INSTSONAME': 'libpython3.14.so.1.0',
    'PY_CFLAGS': '',
    'BLDSHARED': 'gcc -shared',
    'CC': 'gcc',
    'CXX': 'g++',
    'OPT': '-O2',
    'CFLAGS': '',
    'LDFLAGS': '',
    'srcdir': _prefix,
    'VPATH': '',
}
