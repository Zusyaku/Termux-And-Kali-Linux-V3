from setuptools import setup
from steganography import __version__
import os

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read()
f.close()

setup(
    name='steganography',
    version=__version__,
    description="Digital image steganography of encrypted text",
    long_description=long_description,
    author='haminiku',
    author_email='ferdi.kennedy@protonmail.com',
    url='https://github.com/kennedy69/steganography',
    packages=['steganography'],
    package_dir={'steganography': 'steganography'},
    include_package_data=True,
    install_requires=["pillow"],
    license='MIT License',
    zip_safe=False,
    keywords=["Implementation Hide Text In Image with encryption", "stegano", "steganography",
              "Digital image steganography of encrypted text"],
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
    entry_points={
        'console_scripts': [
         'steganography = steganography.steganography:main',
        ],
    },
)
