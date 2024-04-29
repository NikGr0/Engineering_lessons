

import pandas as pd

d_user = [
    {
        'name': 'Ivan',
        'age': '28',
        'e_mail': 'ivan@mail.com'
    },
    {
        'name': 'Petr',
        'age': '33',
        'e_mail': 'petr@mail.com'
    }
]

df1 = pd.DataFrame(d_user)

df1.to_csv('from_pandas.csv', index=False)

df2 = pd.read_csv('from_pandas.csv')
print(df2)