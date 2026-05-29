# Session 7 Part 2 quiz

## Question 1

What does `movies.isnull().sum()` show?

- The total number of rows.
- Missing values per column.
- Duplicate rows only.
- The average value of each numeric column.

Answer: 2
Type: single
Time: 45
Explanation: `isnull()` marks missing values and `sum()` counts them by column.


## Question 2

Why might you use `movies.copy()` before cleaning?

- To test cleaning steps without changing the original DataFrame.
- To delete the original DataFrame.
- To make pandas run without importing it.
- To convert a CSV file into JSON.

Answer: 1
Type: single
Time: 45
Explanation: A copy lets you experiment while preserving the raw data.


## Question 3

Which method can fill missing values?

- `fillna()`
- `findna()`
- `replace_columns()`
- `missing()`

Answer: 1
Type: single
Time: 45
Explanation: `fillna()` replaces missing values with a chosen value.


## Question 4

What does `value_counts(dropna=False)` do?

- Counts values and includes missing values in the count.
- Deletes missing values before counting.
- Converts all values to numbers.
- Shows only the first five values.

Answer: 1
Type: single
Time: 60
Explanation: `dropna=False` keeps missing values visible in the count.


## Question 5

Which statement is the safest?

- Always replace missing numeric values with zero.
- Always delete rows with missing values.
- Decide how to handle missing values based on the column and analysis goal.
- Ignore all missing values.

Answer: 3
Type: single
Time: 60
Explanation: Missing-value handling is a data decision, not an automatic rule.


## Question 6

What is one risk of filling missing ratings with the mean?

- It can hide missingness and reduce variation in the data.
- It changes the column name.
- It makes the DataFrame impossible to print.
- It creates duplicate column names.

Answer: 1
Type: single
Time: 60
Explanation: Mean filling can make the data look cleaner than it really is.


## Question 7

What does interpolation do?

- Estimates missing numeric values between known values.
- Deletes all missing rows.
- Converts text columns to uppercase.
- Counts duplicate rows.

Answer: 1
Type: single
Time: 60
Explanation: Interpolation estimates missing numeric values using surrounding values.


## Question 8

When is interpolation most likely to make sense?

- When rows have a meaningful order, such as weeks or time.
- When filling a movie genre column.
- When renaming columns.
- When counting unique values.

Answer: 1
Type: single
Time: 60
Explanation: Interpolation depends on order, so it is most suitable for ordered numeric data.
