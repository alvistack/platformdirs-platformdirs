# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='platformdirs',
    version='4.3.6',
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
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    extras_require={
        'docs': [
            'furo>=2024.8.6',
            'proselint>=0.14',
            'sphinx-autodoc-typehints>=2.4',
            'sphinx>=8.0.2',
        ],
        'test': [
            'appdirs==1.4.4',
            'covdefaults>=2.3',
            'pytest-cov>=5',
            'pytest-mock>=3.14',
            'pytest>=8.3.2',
        ],
        'type': [
            'mypy>=1.11.2',
        ],
    },
    packages=[
        'platformdirs',
    ],
    package_dir={'': 'src'},
)
