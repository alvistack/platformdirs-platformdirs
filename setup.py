# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='platformdirs',
    version='3.0.1',
    description='A small Python package for determining appropriate platform-specific dirs, e.g. a "user data dir".',
    maintainer_email='Bernát Gábor <gaborjbernat@gmail.com>, Julian Berman <Julian@GrayVines.com>, Ofek Lev <oss@ofek.dev>, Ronny Pfannschmidt <opensource@ronnypfannschmidt.de>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'typing-extensions>=4.4; python_version < "3.8"',
    ],
    extras_require={
        'docs': [
            'furo>=2022.12.7',
            'proselint>=0.13',
            'sphinx-autodoc-typehints!=1.23.4,>=1.22',
            'sphinx>=6.1.3',
        ],
        'test': [
            'appdirs==1.4.4',
            'covdefaults>=2.2.2',
            'pytest-cov>=4',
            'pytest-mock>=3.10',
            'pytest>=7.2.1',
        ],
    },
    packages=[
        'platformdirs',
    ],
    package_dir={'': 'src'},
)
