from setuptools import setup, find_packages

setup(
    name='satannot',
    version='1.0.2',
    author='Marin Volarić',
    author_email='marin.volaric1@gmail.com',
    description='A BLAST-based annotation and sequence extraction tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mvolar/satannot',
    packages=find_packages(),
    install_requires=[
        'polars',
        'biopython',
    ],
    entry_points={
        'console_scripts': [ 
            'satannot = satannot.__main__:main',
            'satannot-annotate = satannot.annotate:annotate',
            'satannot-extract = satannot.extract:extract',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
