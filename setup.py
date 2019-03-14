from setuptools import setup

setup(
    name='pyspark-pytest',
    version='1.0',
    packages=['functions', 'util'],
    license='',
    url='https://pyspark.dev',
    author='Zakky Akhtar',
    description='',
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
