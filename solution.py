import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 1022285388 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    successes = np.array([x_success, y_success])
    samples = np.array([x_cnt, y_cnt])
    test = proportions_ztest(count=successes, nobs=samples,  alternative='smaller')
    if test[1] < 0.08:
      answer = True
    else:
      answer = False
    return answer # Ваш ответ, True или False
