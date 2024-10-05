import pandas as pd
from matplotlib import pyplot as plt 

df = pd.read_csv('Netflix.csv')

print(df.head(10))
print(df.tail(10))
print(df.loc[df['imdb_score'].idxmax()])
print("media de duração de show: "+ str(df[df['type'] == 'SHOW']['runtime'].mean()))
print("media de duração dos filmes: "+ str(df[df['type'] == 'MOVIE']['runtime'].mean()))
print("Show com a maior duração:")
print(df.loc[df[df['type'] == 'SHOW']['runtime'].idxmax()])
print("Filme com a maior duração:")
print(df.loc[df[df['type'] == 'MOVIE']['runtime'].idxmax()])
print("Filmes por ano")
print(df[df['type'] == 'MOVIE']['release_year'].value_counts().head(10))
print("Filmes por categoria")
print(df[df['type'] == 'MOVIE']['age_certification'].value_counts())
print("Campos vazios")
print(df.isnull().sum())

plt.plot(df[df['type']=='MOVIE'].groupby('release_year')['imdb_score'].mean().index,df[df['type']=='MOVIE'].groupby('release_year')['imdb_score'].mean())
plt.title('Média de IMDb por ano filme')
plt.xlabel('Ano')
plt.ylabel('IMDb')
plt.grid(True)
plt.show()

plt.plot(df[df['type']=='SHOW'].groupby('release_year')['imdb_score'].mean().index,df[df['type']=='SHOW'].groupby('release_year')['imdb_score'].mean())
plt.title('Média de IMDb por ano show')
plt.xlabel('Ano')
plt.ylabel('IMDb')
plt.grid(True)
plt.show()


plt.plot(df[df['type']=='SHOW'].groupby('release_year')['imdb_votes'].mean().index,df[df['type']=='SHOW'].groupby('release_year')['imdb_votes'].mean())
plt.title('Média de votantes por ano show')
plt.xlabel('Ano')
plt.ylabel('votantes')
plt.grid(True)
plt.show()


plt.plot(df[df['type']=='MOVIE'].groupby('release_year')['imdb_votes'].mean().index,df[df['type']=='MOVIE'].groupby('release_year')['imdb_votes'].mean())
plt.title('Média de votantes por ano filme')
plt.xlabel('Ano')
plt.ylabel('votantes')
plt.grid(True)
plt.show()