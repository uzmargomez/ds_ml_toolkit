import setuptools

with open("README.md", "r") as fh:
        long_description = fh.read()

setuptools.setup(
    name="ds_ml_toolkit",
    version="0.0.1",
    author="Uzmar Gomez",
    author_email="uzmar.gomez@ciencias.unam.mx",
    description="Toolkit for datascience and mlops",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uzmargomez/ds_ml_toolkit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.5',
    install_requires=[
        'python-dotenv>=0.17.1',
        'google-oauth>=1.0.1',
        'requests>=2.25.1',
        'seldon-core>=1.7.0',
        'numpy>=1.20.3'
    ]
)