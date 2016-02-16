#!/usr/bin/env python

import shutil

# Copy src to dst. (cp src dst)
shutil.copy(src,dst)

# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src,dst)

# Copy directory tree (cp -R src dst)
shutil.copytree(src,dst)

# Move src to dst (mv src dst)
shutil.move(src,dst)

# Use symlink instead of target file
shutil.copy2(src,dst,follow_symlinks=False)

# Preserve symlink in copied dirs
shutil.copytree(src,dst,symlinks=True)

# Ignore files during copy
def ignore_pyc_files(dirname,filenames):
    return [name in filenames if name.endswith('.pyc')]

shutil.copytree(src,dst,ignore=ignore_pyc_files)

# Ignore patterns
shutil.copytree(src,dst,ignore=shutil.ignore_patterns('*~','*.pyc'))


# Get the directories

filenames = '~/langs/file'

import os.path

print os.path.basename(filename)

print os.path.dirname(filename)

print os.path.cplit(filename)

print os.path.join('/new/dir', os.path.basename(filename))

print os.path.expanduser('~/langs/file')

# Error handling

try:
    shutil.copytree(src,dst)
except shutil.Error as e:
    for src,dst,msg in e.args[0]:
        # src is source name
        # dst is destination name
        # mst is error message from exeption
        print(dst,src,msg)
