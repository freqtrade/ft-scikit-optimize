from setuptools import find_packages, setup

try:
    import builtins
except ImportError:
    # Python 2 compat: just to be able to declare that Python >=3.5 is needed.
    import __builtin__ as builtins

# This is a bit (!) hackish: we are setting a global variable so that the
# main skopt __init__ can detect if it is being loaded by the setup
# routine
builtins.__SKOPT_SETUP__ = True

import skopt

VERSION = skopt.__version__

setup(
    name='ft-scikit-optimize',
    version=VERSION,
    description='Sequential model-based optimization toolbox.',
    long_description=open('README.rst').read(),
    url='https://scikit-optimize.github.io/',
    license='BSD 3-clause',
    author='The scikit-optimize contributors, the Freqtrade Team',
    packages=find_packages(include=('skopt.*',),
                           exclude=('*.tests',)),
    # use_scm_version=True,
    python_requires='>= 3.8',
    setup_requires=[
        'setuptools_scm',
    ],
    install_requires=[
        'joblib>=1.2',
        'pyaml>=16.9',
        'numpy>=1.17',
        'scipy>=1.5',
        'scikit-learn>1.1',
    ],
    extras_require={
        'plots': [
            "matplotlib>=2.0.0",
        ],
        'dev': [
            'flake8',
            'pytest',
            'pytest-cov',
            'pytest-xdist',
        ],
        'doc': [
            'sphinx',
            'sphinx-gallery>=0.6',
            'memory_profiler',
            'numpydoc',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: Unix',
    ],
    )
