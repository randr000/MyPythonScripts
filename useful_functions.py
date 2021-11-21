def count_distinct(series):
    """Takes a Pandas Series and prints out a string with the series name and the # of distinct values in that series"""
    
    print('The number of distinct values in the {name} column is {x}.'.format(name=series.name,x=series.nunique()))
    
def unique_values(series):
    """Takes a Pandas Series and returns a DataFrame with all unique values and their counts"""
    
    return series.value_counts(dropna=False).rename_axis('Unique Values').reset_index(name='Counts')

def print_row_count(dframe):
    """Takes a dataframe and prints out the total number of rows in a formatted string."""
    
    row_count = len(dframe)
    print('Current Row Count: {:,}'.format(row_count))
    
def count_null(series):
    """Takes a series and counts and prints the number of null and not null values"""
    
    print("Series name: {}".format(series.name))
    print("The number of missing values is {:,}.".format(series.isnull().sum()))
    print("The number of not null values is {:,}.".format(series.notnull().sum()))
    
def plot_bool_bar(series, title="insert title"):
    """Plots a bar chart sepcifying the series and title. Only for use with boolean series"""
    
    y_count = sum(series.apply(lambda x: 1 if x else 0))
    n_count = sum(series.apply(lambda x: 1 if x == False else 0))
    plt.bar(['Y','N'], [y_count, n_count])
    plt.title(title)
    plt.ylabel('Count')
    plt.show
