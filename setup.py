from setuptools import setup, find_packages

setup(
    name="its-cdktf-base",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    # Optional: Add metadata about the package
    description="Set of reusable infrastructure constructs to build Azure resources with CDK using Terraform.",
    author="Mason Putney, Joshua Hughes",
    author_email="mason@itsolutionsco.com",
    url="https://dev.azure.com/itsc-dev/its_cdktf_base",
)
