import sys
import setuptools

# Default version number
default_version = "1.1.7.7"

# Extract version number from command line arguments
version = None
for arg in sys.argv:
    if arg.startswith('--version'):
        version = arg.split('=')[1]
        sys.argv.remove(arg)
        break

if version is None:
    version = default_version  # Use the default version number if not provided via command line

setuptools.setup(
    name="newPassword",                      # This is the name of the package
    version=version,                         # Version number provided via command line or default
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
