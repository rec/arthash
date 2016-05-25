#!/usr/bin/env python3

import hashlib, sys

def file_hash(filename, hasher=hashlib.sha256, chunksize=10000000):
    with open(filename, 'rb') as f:
        h = hasher()
        while True:
            chunk = f.read(chunksize)
            if not chunk:
                return h.hexdigest()
            h.update(chunk)

def add_hash_to(fname, **kwds):
    open(fname + '.sha256.txt', 'w').write(file_hash(fname, **kwds) + '\n')


if __name__ == '__main__':
    for filename in sys.argv[1:]:
        try:
            add_hash_to(filename)
        except Exception as e:
            print('Exception |', e, '| trying to hash', filename)
