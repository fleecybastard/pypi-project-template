from setuptools import setup, find_packages

setup(
    name='project-name',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        "pydantic>=2.6.0"
    ],
    author='just-me',
    description='this is a simple project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
