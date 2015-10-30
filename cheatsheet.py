len(df)                     series + value        df[df.c == value]
df.head()                   series + series2      df[(df.c >= value) & (df.d <  value)]
df.tail()                   series.notnull()      df[(df.c < value) | (df.d != value)]
df.COLUMN                   series.isnull()       df.sort('column')
df['COLUMN']                series.order()        df.sort(['column1', 'column2'])

