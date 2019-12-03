from setuptools import setup, find_packages

setup(
    name='demo',
    version='1.0',
    author='Jisuk Byun',
    description='',
    long_description='./README.md',
    long_description_content_type='text/markdown',
    url='https://github.com/SweepFlaw/demo',
    install_requires=[
        'position-learning==1.0'
    ],
    dependency_links=[
        'https://github.com/SweepFlaw/position-learning/tarball/master#egg=position-learning-1.0'
    ],
    packages=find_packages(),
    python_requires='>=3.4'
)