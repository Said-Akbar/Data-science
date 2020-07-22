# 7/22/2020 Saidakbar P
# docstrings
import inspect
# check doc string for a function
raw_docstring = split_and_stack.__doc__
formatted_docstring = inspect.getdoc(split_and_stack)

def count_letter(content, letter):
    """Counts the number of times `letter` appears in `content`.

    Args:
      content (str): The string to search.
      letter (str): The letter to search for.

    Returns:
      int
    Raises:
       ValueError: `letter` must be a single character string.
    """
    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` must be a single character string.')
    return len([char for char in content if char == letter])

formatted_docstring = inspect.getdoc(count_letter)
print(formatted_docstring)

def standardize(df_col):
    """takes a list and returns z-score for the list
    
    Args:
       one-dimension list of number
    Returns:
       a single number z-score for the given list
    """
    z_score = (df_col-df_col.mean())/df_col.std()
    return z_score

df['y1_z'] = standardize(df['y1_gpa'])
df['y2_z'] = standardize(df['y2_gpa'])
df['y3_z'] = standardize(df['y3_gpa'])
df['y4_z'] = standardize(df['y4_gpa'])

#INITIAL CODE
def find_mean(values):
    """Gets the mean and median of a list of `values`

    Args:
      values (iterable of float): A list of numbers

    Returns:
      tuple (float, float): The mean and median
    """
    return sum(values)/len(values)

def find_median(values):
    midpoint = int(len(values) / 2)
    if len(values) % 2 == 0:
        median = (values[midpoint - 1] + values[midpoint]) / 2
    else:
        median = values[midpoint]
    return median

list_mean = find_mean([1,2,3])
list_median = find_median([1,2,3,4])
# lists are mutable
a = [1, 2, 3]
b = a
a.append(4)
print(b)
b.append(5)
print(a)
a = 42

def foo(var=[]):
    var.append(1)
    return var

print(foo()) # [1]
print(foo()) # [1, 1]
# use var=None to get a new list (include 'if list is None')
def add_column(values, df=None):
    """Adds a column of `values` to a DataFrame `df`.
    The column will be named "col_<n>" where "n" is
    the numerical index of the column.

    Args:
        values (iterable): The values of the new column
        df (DataFrame, optional): The DataFrame to update.
          If no DataFrame is passed, one is created by default.

    Returns:
        DataFrame
    """
    if df is None:
        df = pd.DataFrame()
    df['col_{}'.format(len(df.columns))] = values
    return df

df_1=add_column(values=range(10))
df_2 = add_column(values=range(10))