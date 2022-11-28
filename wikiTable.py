import pandas as pd

money = pd.read_html('https://en.wikipedia.org/wiki/List_of_Hindi_films_of_2022')
print(len(money))
