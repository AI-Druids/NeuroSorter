import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AUTO_SPIKE_SORTING_GUI",
    packages = ['AUTO_SPIKE_SORTING_GUI'],
    version="0.0.1",
    author="Val-Calvo, Mikel and Alegre-Cortés, Javier",
    author_email="mikel1982mail@gmail.com, jalegre@umh.es",
    description="An automatic spike-sorting graphical interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AI-Druids/PySorter",
    keywords = ['AUTOMATIC', 'SPIKE', 'SORTING','GRAPHICAL','INTERFACE'],
    install_requires=[            # I get to this in a second
          'numpy',
          'matplotlib',
          'tensorflow==2.0',
          'PyQt5',
          'sklearn'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
