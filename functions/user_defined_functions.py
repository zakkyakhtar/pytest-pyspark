from pyspark.sql import functions as F


def conditional_count(column_name, condition_value):
    """
    Takes the column name of the dataframe and performes a count on the records matching the value
    :param column_name:
    :param condition_value:
    :return: count of records matching the condition_value
    """
    return F.sum(
        F.when(
            F.col(column_name) == condition_value, 1
        ).otherwise(0)
    )
