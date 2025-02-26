from setuptools import setup, find_packages

setup(
  name = 'x-clip',
  packages = find_packages(exclude=[]),
  version = '0.0.16',
  license='MIT',
  description = 'X-CLIP',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/x-clip',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'contrastive learning',
    'CLIP',
  ],
  install_requires=[
    'einops>=0.3',
    'ftfy',
    'regex',
    'torch>=1.6',
    'torchvision'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
