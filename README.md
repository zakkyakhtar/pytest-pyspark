# pytest-pyspark
A sample project to organise your pyspark project. It demonstrates the use of `pytest` to unit test PySpark methods. It also demonstrates the use of pytest's conftest.py feature which can be used for dependency injection. In this case SparkSession is being injected to the test cases.

# How to use it
* The files containing main methods should be kept outside the package
* Create an egg file by running `python setup.py bdist_egg`
* Submit your spark application:
`spark-submit --py-files=pytest-pyspark-1.0.egg main.py`

# How to Run Test cases
* Create a virtual environment: `virtualenv pyspark-venv`
* Activate the virtual environment: `source pyspark-ven/bin/activate`
* Install the test's dependency: `pip install -r test_requirements.txt`
* Run the test: `pytest`
In order to generate the unit test report in junit xml and coverage report in Cobetura xml format:
`py.test --cov-report xml:./reports/coverage.xml 
         ----junitxml=./reports/unit-test.xml`
