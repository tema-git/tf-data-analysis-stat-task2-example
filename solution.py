import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 401141478

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    s = np.sum(x**2) 
    l = chi2.ppf(1 - alpha/2, n)
    r = chi2.ppf(alpha/2, n)
    left = np.sqrt(s/31/l)
    right = np.sqrt(s/31/r)
    return left, right
