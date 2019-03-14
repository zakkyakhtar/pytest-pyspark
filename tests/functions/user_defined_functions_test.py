import pytest
from pyspark.sql import functions as F
from pyspark.sql.session import SparkSession

from functions.user_defined_functions import conditional_count


@pytest.fixture(scope="session")
def spark_test_session():
    return (
        SparkSession
        .builder
        .master('local[*]')
        .appName('unit-testing')
        .getOrCreate()
    )


def test_conditional_count(spark_test_session):
    """
    Test the count function with condition
    :param spark_test_session:
    :return:
    """

    test_data = [(2343, 'Y'), (2343, 'Y'), (2343, 'N'),
                 (2112, 'Y'), (2112, 'N'), (2112, 'Y'), (2112, None), (2112, 'Y'),
                 (3981, 'N'), (3981, None)]

    test_data_df = spark_test_session.createDataFrame(
        test_data,
        ["employee_id", "car_owner"])

    expected_data = [(2112, 3), (2343, 2), (3981, 0)]

    expected_df = spark_test_session.createDataFrame(expected_data, ["employee_id", "total_car_owners"])
    expected = expected_df.collect()
    output_df = test_data_df \
        .groupBy("employee_id") \
        .agg(conditional_count('car_owner', F.lit('Y'))
             .alias("total_car_owners"))
    output = output_df.orderBy("employee_id").collect()
    assert output == expected

