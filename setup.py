#!/usr/bin/env python
#-*- coding: utf-8 -*-

from ooni import __version__
import os
from os.path import join as pj
import sys
from distutils.core import setup

install_requires = [
    'txsocksx>=0.0.2',
    'scapy>=2.2.0',
    'dnspython>=1.10.0',
    'parsley>1.0',
]

dependency_links = [
    'https://people.torproject.org/~ioerror/src/mirrors/ooniprobe'
]

data_files = []
for root, dirs, file_names in os.walk('data/'):
    files = []
    for file_name in file_names:
        if not file_name.endswith('.pyc'):
            files.append(pj(root, file_name))
    data_files.append([pj('/usr/share/ooni', root), files])

with open('requirements.txt') as f:
    for line in f:
        if line.startswith("#") or line.startswith('http'):
            continue
        install_requires.append(line)

setup(
    name="ooni-probe",
    version=__version__,
    author="Arturo Filastò",
    author_email = "art@torproject.org",
    url="https://ooni.torproject.org/",
    package_dir={'ooni': 'ooni'},
    data_files=data_files,
    packages=['ooni', 'ooni.api', 'ooni.templates', 'ooni.tests', 'ooni.utils'],
    scripts=["bin/ooniprobe"],
    dependency_links=dependency_links,
    install_requires=install_requires,
)
