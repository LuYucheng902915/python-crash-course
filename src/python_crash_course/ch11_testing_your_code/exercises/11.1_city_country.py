# 11-1. City, Country:
# Write a function that accepts two parameters: a city name and a country name.
# The function should return a single string of the form City, Country, such as Santiago, Chile.
# Store the function in a module called city_functions.py, and save this file in a new folder so pytest won’t try to run the tests we’ve already written.
# Create a file called test_cities.py that tests the function you just wrote.
# Write a function called test_city_country() to verify that calling your function with values such as 'santiago' and 'chile' results in the correct string.
# Run the test, and make sure test_city_country() passes.

"""
(python-crash-course-3.11) luyucheng@LAPTOP-TA9F45GS:~/learning/python-learning/python-crash-course$ pytest src/python_crash_course/ch11_testing_your_code/exercises/test_cities.py
======================================================================================================================================================= test session starts =======================================================================================================================================================
platform linux -- Python 3.11.9, pytest-8.4.1, pluggy-1.6.0
rootdir: /home/luyucheng/learning/python-learning/python-crash-course
configfile: pyproject.toml
collected 1 item

src/python_crash_course/ch11_testing_your_code/exercises/test_cities.py .                                                                                                                                                                                                                                                   [100%]

======================================================================================================================================================== 1 passed in 0.01s ========================================================================================================================================================
"""
