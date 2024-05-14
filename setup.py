# setup.py

from setuptools import setup, find_packages

setup(
    name="ptz_camera_control",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "ptz_camera_control=ptz_camera_control.gui:start_gui",
        ],
    },
    author="Steven Eldredge",
    author_email="texquads@gmail.com",
    description="A package to control PTZ cameras via a GUI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Texquad/ptz_camera_control",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)