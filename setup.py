# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='platformdirs',
    version='4.2.2',
    description='A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`.',
    maintainer_email='Bernát Gábor <gaborjbernat@gmail.com>, Julian Berman <Julian@GrayVines.com>, Ofek Lev <oss@ofek.dev>, Ronny Pfannschmidt <opensource@ronnypfannschmidt.de>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    extras_require={
        'docs': [
            'furo>=2023.9.10',
            'proselint>=0.13',
            'sphinx-autodoc-typehints>=1.25.2',
            'sphinx>=7.2.6',
        ],
        'test': [
            'appdirs==1.4.4',
            'covdefaults>=2.3',
            'pytest-cov>=4.1',
            'pytest-mock>=3.12',
            'pytest>=7.4.3',
        ],
        'type': [
            'mypy>=1.8',
        ],
    },
    packages=[
        'platformdirs',
    ],
    package_dir={'': 'src'},
)
