from bs4 import BeautifulSoup
import requests
 
URL = 'https://www.timeout.com/newyork/movies/best-movies-of-all-time'
 
response = requests.get(URL)
response.raise_for_status()
 
movies_list = response.text
soup = BeautifulSoup(movies_list, 'html.parser')
 
tags_list = soup.find_all(name='h3', class_='card-title')
movie_rankings = [(item.getText()) for item in tags_list]
 
file_string = ''
 
for movie in movie_rankings:
    movie_rank = movie.strip()
    if movie_rank[0] != 'C':
        file_string += f'{movie_rank} \n'
 
with open('lista_filmes.txt', 'w', encoding='utf-16') as file:
    file.write(file_string)