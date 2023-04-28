# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:28:01 2023

@author: Devanshi
"""

import pandas as pd

# read the movie_data csv file
user_new_data = pd.read_csv('D:/e/Sem6/powerbiproject/Project-5/mubi_ratings_user_data.csv/mubi_ratings_user_cleaned_data.csv',low_memory=False)

user_new_data[['user_trialist', 'user_subscriber', 'user_eligible_for_trial', 'user_has_payment_method']] = user_new_data[['user_trialist', 'user_subscriber', 'user_eligible_for_trial', 'user_has_payment_method']].replace({True: 1, False: 0})


# write the merged data to a new csv file
user_new_data.to_csv('user_new_data.csv', index=False)
