###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module data_analyser.py
###

## Import necessary libraries
import pandas as pd

## Function to calculate the correlation matrix
def calculate_correlation(data):
    """
    Calculate the correlation matrix for the given DataFrame.

    This function computes the pairwise correlation of columns in the 
    DataFrame using the Pearson correlation coefficient. The resulting 
    correlation matrix shows the strength and direction of the linear 
    relationship between the variables.

    Parameters:
        data (pd.DataFrame): A pandas DataFrame containing the data for which 
                             the correlation matrix is to be calculated.

    Returns:
        pd.DataFrame: A DataFrame representing the correlation matrix, where 
                       each element (i, j) is the correlation coefficient 
                       between the i-th and j-th columns of the input DataFrame.
    """
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
        
    # Return the correlation matrix
    return correlation_matrix
    
## Function to calculate descriptive statistics of data
def calculate_descriptive_statistics(data):
    """
    Calculate descriptive statistics for the given DataFrame.

    This function computes various descriptive statistics for each column 
    in the DataFrame, including count, mean, standard deviation, minimum, 
    maximum, and quartiles. It also includes the count of missing values 
    for each column.

    Parameters:
        data (pd.DataFrame): A pandas DataFrame containing the data for which 
                             descriptive statistics are to be calculated.

    Returns:
        pd.DataFrame: A DataFrame containing the descriptive statistics for 
                       each column, with statistics as rows and column names 
                       as the index. The output includes a count of missing 
                       values for each column.
    """
    # Calculate descriptive statistics
    stats = data.describe(include='all').T
    stats['missing_values'] = data.isnull().sum()
        
    return stats