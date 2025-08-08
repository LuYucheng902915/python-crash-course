# 11-2. Population:
# Modify your function so it requires a third parameter, population.
# It should now return a single string of the form City, Country – population xxx, such as Santiago, Chile – population 5000000.
# Run the test again, and make sure test_city_country() fails this time.
# Modify the function so the population parameter is optional.
# Run the test, and make sure test_city_country() passes again.
# Write a second test called test_city_country_population() that verifies you can call your function with the values 'santiago', 'chile', and 'population=5000000'.
# Run the tests one more time, and make sure this new test passes.

'''
(python-crash-course-3.11) luyucheng@LAPTOP-TA9F45GS:~/learning/python-learning/python-crash-course$ pytest src/python_crash_course/ch11_testing_your_code/exercises/test_cities.py
======================================================================================================================================================= test session starts =======================================================================================================================================================
platform linux -- Python 3.11.9, pytest-8.4.1, pluggy-1.6.0
rootdir: /home/luyucheng/learning/python-learning/python-crash-course
configfile: pyproject.toml
collected 4 items

src/python_crash_course/ch11_testing_your_code/exercises/test_cities.py .F..                                                                                                                                                                                                                                                [100%]

============================================================================================================================================================ FAILURES =============================================================================================================================================================
_____________________________________________________________________________________________________________________________________________________ test_city_country_fail ______________________________________________________________________________________________________________________________________________________

    def test_city_country_fail():
        """Does a simple city and country pair work?"""
>       santiago_chile = city_country_fail("santiago", "chile")
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: city_country_fail() missing 1 required positional argument: 'population'

src/python_crash_course/ch11_testing_your_code/exercises/test_cities.py:12: TypeError
===================================================================================================================================================== short test summary info =====================================================================================================================================================
FAILED src/python_crash_course/ch11_testing_your_code/exercises/test_cities.py::test_city_country_fail - TypeError: city_country_fail() missing 1 required positional argument: 'population'
=================================================================================================================================================== 1 failed, 3 passed in 0.04s ===================================================================================================================================================
'''
