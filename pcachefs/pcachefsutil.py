"""
Utility methods used across pcachefs.
"""
import errno
import os
import sys

DEBUG = True
def debug(*words):
    if DEBUG:
        sys.stderr.write('DEBUG: %s\n' % ' '.join(str(word) for word in words))

# Error codes
# source: /usr/lib/syslinux/com32/include/errno.h
E_NO_SUCH_FILE = -errno.ENOENT
E_NOT_PERMITTED = -errno.EPERM
E_IO_ERROR = -errno.EIO
E_PERM_DENIED = -errno.EACCES
E_READ_ONLY = -errno.EROFS
E_NOT_IMPL= -errno.ENOSYS
E_INVALID_ARG = -errno.EINVAL


def is_read_only_flags(flags):
    access_flags = os.O_RDONLY | os.O_WRONLY | os.O_RDWR
    return flags & access_flags == os.O_RDONLY
