#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'Pillow>=3.1.1',
    'pyephem>=3.7.6.0',
    'configparser>=3.5.0',
    'requests>=2.17.3'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='vegindex',
    version='0.1.0',
    description="Python package to generate vegetation index timeseries",
    long_description=readme + '\n\n' + history,
    author="Thomas Milliman",
    author_email='thomas.milliman@unh.edu',
    url='https://github.com/tmilliman/vegindex',
    packages=[
        'vegindex',
    ],
    package_dir={'vegindex':
                 'vegindex'},
    entry_points={
        'console_scripts': [
            'generate_roi_timeseries=vegindex.generate_roi_timeseries:main',
            'generate_summary_timeseries=vegindex.generate_summary_timeseries:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='vegindex',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
