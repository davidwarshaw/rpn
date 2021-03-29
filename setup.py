from setuptools import setup

setup(name='rpn',
      version='0.1',
      description='Reverse Polish Notation calculator',
      url='http://github.com/davidwarshaw',
      author='David Warshaw',
      author_email='david.warshaw@gmail.com',
      license='MIT',
      packages=['rpn', 'rpn.operators'],
      scripts=['bin/rpn'],
      zip_safe=False)
