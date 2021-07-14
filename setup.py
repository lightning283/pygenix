import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name= "pygenix" ,
    version = "0.6", 
    author="lightning283",
    author_email="deadtarget283@gmail.com",
    description="A Python Package That Contains Text Aimations And Some Useful Utils",
    long_description=long_description,
    install_requires=['speechrecognition', 'pyaudio '],
    long_description_content_type="text/markdown",
    url="https://github.com/lightning283/pygenix",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)