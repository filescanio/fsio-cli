from setuptools import setup, find_packages

setup(
    name="filescan-cli",
    version="1.0.0",
    description="Cli client for Filescan service",
    author="Andrii Naidenko",
    author_email="shlerp11@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    url="https://www.filescan.io",
    install_requires=[
        "colorama==0.4.4",
        "asyncio==3.4.3",
        "requests==2.27.1"
    ],
)
