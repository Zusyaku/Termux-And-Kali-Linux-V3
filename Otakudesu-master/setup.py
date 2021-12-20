from setuptools import setup, find_packages
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'otakudesu',
  packages = ['otakudesu'],
  include_package_data=True,
  version = '0.0.9',
  license = 'MIT',
  description = 'Otakudesu Scrapper',
  long_description_content_type = 'text/markdown',
  long_description = open('README.md', 'r').read(),
  author = 'MhankBarBar',
  author_email = 'mhankbarbar@yes.my',
  url = 'https://github.com/MhankBarBar/otakudesu',
  download_url = 'https://github.com/MhankBarBar/otakudesu/archive/0.0.9.tar.gz',
  keywords = ['anime', 'anime sub indo', 'anime scrapper', 'animeindo', 'animelovers', 'otakudesu'],
  install_requires=[
          'validators',
          'requests',
          'bs4'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
