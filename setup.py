import setuptools
from version import __version__

setuptools.setup(
    name="newPassword",                      # This is the name of the package
    version=__version__,                     # Version number from version.py
    author="Nipun Dogra",                    # Full name of the author
    description="Password generator package",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),     # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPI website
    python_requires='>=3.6',                # Minimum version requirement of the package
    install_requires=[]                     # Install other dependencies if any
)
