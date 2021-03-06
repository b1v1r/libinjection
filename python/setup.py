"""
libinjection module for python

 Copyright 2012, 2013 Nick Galbreath
 nickg@client9.com
 BSD License -- see COPYING.txt for details
"""

from distutils.core import setup, Extension

MODULE = Extension(
    '_libinjection', [ 'libinjection/libinjection_wrap.c', 'libinjection/libinjection_sqli.c' ],
    swig_opts=['-Wextra', '-builtin'],
    define_macros = [],
    include_dirs = [],
    libraries = [],
    library_dirs = [],
    )

setup (
    name             = 'libinjection',
    version          = '3.4.1',
    description      = 'Wrapper around libinjection c-code to detect sqli',
    author           = 'Nick Galbreath',
    author_email     = 'nickg@client9.com',
    url              = 'http://client9.com/libinjection',
    ext_modules      = [MODULE],
    packages         = ['libinjection'],
    long_description = '''
wrapper around libinjection
''',
       classifiers   = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Database',
        'Topic :: Security',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Topic :: Internet :: Log Analysis',
        'Topic :: Internet :: WWW/HTTP'
        ]
    )
