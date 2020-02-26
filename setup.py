from setuptools import setup, find_packages

with open("./README.md") as f:
    long_description = f.read()

setup(
    name='sech3r',
    version='4.2',
    author="Captain Nick Lucifer",
    author_email="naryal2580@gmail.com",
    url="https://github.com/naryal2580/sech3r",
    download_url='https://github.com/naryal2580/sech3r/tarball/master',
    description="HTTP Security Header Checker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    py_modules=['sech3r'],
    scripts=['bin/sech3r'],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    python_requires='>=3',
 )
