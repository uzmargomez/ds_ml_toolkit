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
        'python-dotenv',
        'google-oauth',
        'google-auth',
        'requests',
        'seldon-core',
        'numpy',
        'google-cloud-bigquery-storage',
        'google-cloud-storage',
        'google-cloud-bigquery[bqstorage,pandas]',
        'pyarrow',
        'tqdm',
    ]
)