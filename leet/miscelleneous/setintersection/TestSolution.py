#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Sun 17:00:00 Sep 15 2019
@author : manoj

Test cases for the Solution Module
"""

import unittest
import logging
from Solution import InnerMedian

test_logger = logging.getLogger("TestLogger")


class TestInnerMedian(unittest.TestCase):
    """

    """
    @classmethod
    def setUpClass(cls):
        test_logger.info(f"Setting up class method: \n")
        cls.inner_median_obj = InnerMedian()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_01_sorted_lists(self):
        """

        Returns:

        """
        # test data
        x, y = [1,2,3], [2,3,3]
        # test
        result_using_smaller_list = \
            self.inner_median_obj.get_inner_median_using_smaller_list(x, y)
        self.assertEqual(result_using_smaller_list, 2.5)

        result_using_builtin = \
            self.inner_median_obj\
                .get_inner_median_using_built_in_intersection(x, y)
        self.assertEqual(result_using_builtin, 2.5)

    def test_02_lists_of_different_lengths(self):
        """

        Returns:

        """
        # test data
        x, y = [3, 1, 2], [1, 2, 3, 4]
        # test
        result_using_smaller_list = \
            self.inner_median_obj.get_inner_median_using_smaller_list(x, y)
        self.assertEqual(result_using_smaller_list, 2.0)

        result_using_builtin = \
            self.inner_median_obj\
                .get_inner_median_using_built_in_intersection(x, y)
        self.assertEqual(result_using_builtin, 2.0)


    def test_03_lists_with_duplicates_1(self):
        """
        """
        # test data
        x, y = [1, 3, 2, 1, 3], [1, 2, 3, 4]
        # test
        result_using_smaller_list = \
            self.inner_median_obj.get_inner_median_using_smaller_list(x, y)
        self.assertEqual(result_using_smaller_list, 2.0)

        result_using_builtin = \
            self.inner_median_obj\
                .get_inner_median_using_built_in_intersection(x, y)
        self.assertEqual(result_using_builtin, 2.0)

    def test_04_lists_with_duplicates_2(self):
        """

        Returns:

        """
        # test data
        x, y = [1, 1, 3, 2, 1, 3], [1, 2, 3, 4]
        # test
        result_using_smaller_list = \
            self.inner_median_obj.get_inner_median_using_smaller_list(x, y)
        self.assertEqual(result_using_smaller_list, 2.0)

        result_using_builtin = \
            self.inner_median_obj\
                .get_inner_median_using_built_in_intersection(x, y)
        self.assertEqual(result_using_builtin, 2.0)

    def test_05_negative_integers(self):
        """

        Returns:

        """
        # test data
        x, y = [-1, 1, -3, -2, 1, 3], [-1, -2, 3, 4, -2]
        # test
        result_using_smaller_list = \
            self.inner_median_obj.get_inner_median_using_smaller_list(x, y)
        self.assertEqual(result_using_smaller_list, -1.0)

        result_using_builtin = \
            self.inner_median_obj\
                .get_inner_median_using_built_in_intersection(x, y)
        self.assertEqual(result_using_builtin, -1.0)

    def test_06_empty_lists(self):
        """

        Returns:

        """
        # test data
        x, y = list(), list()
        expected_value_error_msg = "There were no common elements in x, y"
        # test
        with self.assertRaises(Exception) as context1:
            result_using_smaller_list = \
                self.inner_median_obj.get_inner_median_using_smaller_list(x, y)
        self.assertEqual(str(context1.exception), expected_value_error_msg)
        with self.assertRaises(ValueError) as context2:
            result_using_builtin = \
                self.inner_median_obj.get_inner_median_using_built_in_intersection(x, y)
        self.assertEqual(str(context2.exception), expected_value_error_msg)


    def test_07_identical_lists(self):
        """

        Returns:

        """
        x, y = [-10, -10, -10, -10], [-10,-10,-10,-10]
        # test
        result_using_smaller_list = \
            self.inner_median_obj.get_inner_median_using_smaller_list(x, y)
        self.assertEqual(result_using_smaller_list, -10.0)

        result_using_builtin = \
            self.inner_median_obj\
                .get_inner_median_using_built_in_intersection(x, y)
        self.assertEqual(result_using_builtin, -10.0)


    def test_08_even_sized_set_intersection(self):
        """

        Returns:

        """
        x, y = [-9, -5, -6, -11, -10], [-9, -5, -6, -11]
        # test
        result_using_smaller_list = \
            self.inner_median_obj.get_inner_median_using_smaller_list(x, y)
        self.assertEqual(result_using_smaller_list, -7.5)

        result_using_builtin = \
            self.inner_median_obj\
                .get_inner_median_using_built_in_intersection(x, y)
        self.assertEqual(result_using_builtin, -7.5)


if __name__=="__main__":
    unittest.main()