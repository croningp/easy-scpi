import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

project_urls = {
    'Source Code':      'https://github.com/bicarlsen/easy-scpi',
    'Bug Tracker':      'https://github.com/bicarlsen/easy-scpi/issues'
}

setuptools.setup(
    name="easy-scpi",
    version="0.1.2",
    author="Brian Carlsen",
    author_email="carlsen.bri@gmail.com",
    description="An easy library for controlling SCPI instruments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[ 'scpi' ],
    url="",
    project_urls = project_urls,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    install_requires=[
        'pyVISA'
    ]
)