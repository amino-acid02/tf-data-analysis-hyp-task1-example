import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 1022285388 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    test = proportions_ztest(count=[x_success, y_success], nobs=[x_cnt, y_cnt], alternative = 'smaller')
    if test[1] < 0.08:
      answer = False
    else:
      answer = True
    return answer # Ваш ответ, True или False
