+++
date = '2026-04-25'
draft = false
title = 'Pandas Core Operations'
+++

Pandas is the standard Python library for data manipulation and analysis.

### Reading Data
Load data from a CSV file into a DataFrame.

```python
import pandas as pd

df = pd.read_csv('dataset.csv')
```

### Exploring Data
Basic methods to inspect the dataset.

```python
df.head()       # View first 5 rows
df.info()       # Summary of columns and data types
df.describe()   # Statistical summary of numerical columns
```

### Filtering Data
Extract specific rows based on conditions.

```python
# Filter where age is greater than 30
filtered_df = df[df['age'] > 30]

# Multiple conditions
filtered_df = df[(df['age'] > 30) & (df['department'] == 'Engineering')]
```

### Handling Missing Values
Deal with `NaN` values.

```python
df.dropna()               # Drop rows with any missing values
df.fillna(0)              # Replace missing values with 0
df.fillna(df.mean())      # Replace missing values with column mean
```
