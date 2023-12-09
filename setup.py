import re
import os
from setuptools import find_namespace_packages, setup

install_requires = [
    "opencv-python-dkurt",
]

# Add patches as data
folder = "optimum/intel/nncf/patches"
data = [os.path.join(folder, name) for name in os.listdir(folder)]

setup(
    name="test-package-dkurt",
    version="1.2.3,
    description="Tests Used By",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    license="Apache",
    install_requires=install_requires,
)
