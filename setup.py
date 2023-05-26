from setuptools import setup

setup(
  name='stay-awake',
  version='1.0.0',
  entry_points={
    'console_scripts': [
      'stayawake=stayawake:run'
    ]
  }
)