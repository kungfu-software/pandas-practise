http://pandas.pydata.org/pandas-docs/dev/api.html  #api-doc


len(df)                     series + value        df[df.c == value]
df.head()                   series + series2      df[(df.c >= value) & (df.d <  value)]
df.tail()                   series.notnull()      df[(df.c < value) | (df.d != value)]
df.COLUMN                   series.isnull()       df.sort('column')
df['COLUMN']                series.order()        df.sort(['column1', 'column2'])

df.COLUMN == Series

df.COLUMN.str.startswith('xxx')
df.COLUMN.str.contains('xxx')
df.COLUMN.str.len()
df.COLUMN.value_counts()
df.sort_index()
df.plot(x='a', y='b', kind='bar|scatter')
df[['column1', 'column2']]
