"""20. Write a function called ‘perform_hypothesis_test’ that takes two lists of numbers as input, 
representing two samples. The function should perform a two-sample t-test and return the p-value. 
Use the ‘scipy.stats’ module in Python to calculate the t-test and p-value."""

import scipy.stats as stat
from scipy.stats import shapiro
from scipy.stats import levene



def check_normality(sample1,sample2):
    try:
        p_value_1=shapiro(sample1)[1]
        p_value_2=shapiro(sample2)[1]
        
        if p_value_1 > 0.05 and p_value_2 >0.05:
            return 1
        else:
            return 0
    except Exception as e:
        raise e
        
def check_variance(sample1,sample2):
    try:
        p_value=levene(sample1,sample2)[1]
        if p_value > 0.05:
            return 1
        else:
            return 0
    except Exception as e:
        raise e
    
def perform_ttest(sample_1,sample_2):
    try:
        if check_normality(sample_1,sample_2)==1 and check_variance(sample_1,sample_2)==1:
            t_statistic=stat.ttest_ind(sample_1,sample_2)[0]
            p_value=stat.ttest_ind(sample_1,sample_2)[1]

            result={"t-statistic":t_statistic,"p-value":p_value} 
            return result
        else:
            return "These two columns don't satisfy the assumption of normality or assumption of equal variance"
    except Exception as e:
        raise e

        

if __name__=="__main__":
    sample1 = [5, 10, 15, 20, 25]
    sample2 = [10, 20, 30, 40, 50]
    print(perform_ttest(sample1,sample2))