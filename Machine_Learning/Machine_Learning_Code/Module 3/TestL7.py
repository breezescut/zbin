#!/usr/bin/env python

__author__ = 'Bem.Zheng'

import unittest
from pandas import DataFrame, Series
import numpy

class TestL7(unittest.TestCase):

    # 练习:平均铜牌数
    def n_test_avg_medal_count(self):
        countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                     'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                     'Austria', 'France', 'Poland', 'China', 'Korea',
                     'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                     'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                     'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

        gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3,
                3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4,
                  3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
        bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2,
                  2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

        olympic_medal_counts = {'country_name': Series(countries),
                                'gold': Series(gold),
                                'silver': Series(silver),
                                'bronze': Series(bronze)}
        df = DataFrame(olympic_medal_counts)

        # YOUR CODE HERE
        print(df)
        print('-' * 50)
        df = df.bronze[df.gold >= 1]
        print(type(df))
        avg_bronze_at_least_one_gold = numpy.mean(df)

        print(avg_bronze_at_least_one_gold)

    # 练习:平均金, 银和铜牌数
    def n_test_avg_medal_count(self):
        '''
        Using the dataframe's apply method, create a new Series called 
        avg_medal_count that indicates the average number of gold, silver,
        and bronze medals earned amongst countries who earned at 
        least one medal of any kind at the 2014 Sochi olympics.  Note that
        the countries list already only includes countries that have earned
        at least one medal. No additional filtering is necessary.
        
        You do not need to call the function in your code when running it in the
        browser - the grader will do that automatically when you submit or test it.
        '''
    
        countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                     'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                     'Austria', 'France', 'Poland', 'China', 'Korea', 
                     'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                     'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                     'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']
    
        gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
        bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
        
        olympic_medal_counts = {'country_name':countries,
                                'gold': Series(gold),
                                'silver': Series(silver),
                                'bronze': Series(bronze)}    
        df = DataFrame(olympic_medal_counts)
        
        # YOUR CODE HERE
        df = df[(df.gold + df.silver + df.bronze) >= 1][['gold', 'silver', 'bronze']]
        avg_medal_count = df.apply(numpy.mean)
        print(avg_medal_count)

        df = df[(df.gold + df.silver + df.bronze) >= 2]
        print(df)
        return avg_medal_count

    # 练习: 奥林匹克奖牌分数
    def test_numpy_dot(self):
        '''
        Imagine a point system in which each country is awarded 4 points for each
        gold medal,  2 points for each silver medal, and one point for each 
        bronze medal.  
    
        Using the numpy.dot function, create a new dataframe called 
        'olympic_points_df' that includes:
            a) a column called 'country_name' with the country name
            b) a column called 'points' with the total number of points the country
               earned at the Sochi olympics.
               
        You do not need to call the function in your code when running it in the
        browser - the grader will do that automatically when you submit or test it.
        '''
    
        countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                     'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                     'Austria', 'France', 'Poland', 'China', 'Korea', 
                     'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                     'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                     'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']
    
        gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
        bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
     
        # YOUR CODE HERE
        all_media = numpy.array([gold, silver, bronze])
        print(all_media)

        points = all_media.transpose().dot([4,2,1])
        olympic_points_df = DataFrame({'country':countries, 'points':points})
        print(olympic_points_df)
        
        return olympic_points_df    
        