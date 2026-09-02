from setuptools import setup

setup(
    name='platformdirs',
    version='4.11.7',
    description='A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`.',
    maintainer_email='Bernát Gábor <gaborjbernat@gmail.com>, Julian Berman <Julian@GrayVines.com>, Ofek Lev <oss@ofek.dev>, Ronny Pfannschmidt <opensource@ronnypfannschmidt.de>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=[
        'platformdirs',
    ],
    package_dir={'': 'src'},
)
