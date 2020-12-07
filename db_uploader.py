genres= {
          '28' : "액션", '12': "모험", '16' : "애니메이션", '35' : "코미디", '80' : "범죄",
          '99' : "다큐멘터리", '18': "드라마", '10751' : "가족", '14' : "판타지", '36' : "역사",
          '27' : "공포", '10402' : "음악", '9648' : "미스터리", '10749' : "로맨스", '878' : "SF",
          '10770' :"TV 영화", '53' : "스릴러", '10752' : "전쟁", '37' : "서부"
          }
    

# import csv
import sqlite3
import requests
import time

# r = requests.get(url)
# movie_dict = r.json()
# conn = sqlite3.connect('db.sqlite3')
# c = conn.cursor()
# c.execute("INSERT INTO movies_movies VALUES ('1', '레고왕', 'sdlkfnsdlkfnsdlkf', 'sdlkfnslknlkkn', '4', 'wangyo', '9.33')")
# conn.commit()
# conn.close()


url1 = 'https://api.themoviedb.org/3/movie/now_playing?api_key=fcca119ad1cb6de2fb83bfb7df0c4a5e&language=ko-kr&page=1&region=kr'

def page1():
  r = requests.get(url1)
  movie_dict = r.json()
  conn = sqlite3.connect('db.sqlite3')
  for i in range(0, 20):
      id = i+1
      title = movie_dict['results'][i]['title']
      img_url = f"https://image.tmdb.org/t/p/w500{movie_dict['results'][i]['poster_path']}"
      story = movie_dict['results'][i]['overview']
      story = story.replace("'", "‘")
      people = movie_dict['results'][i]['popularity']
      rate = movie_dict['results'][i]['vote_average']
      genre = movie_dict['results'][i]['genre_ids']
      real_genre = []
      for j in range(len(genre)):
          for k in genres:
              if str(genre[j]) == k:
                    real_genre.append(genres[k])
      final_genre = ' '.join(real_genre)
      c = conn.cursor()
      c.execute(f"INSERT INTO movies_movies VALUES ('{i+1}', '{title}', '{img_url}','{story}' ,'{people}', '{rate}', '{final_genre}')")
      conn.commit()
  conn.close()

url2 = 'https://api.themoviedb.org/3/movie/now_playing?api_key=fcca119ad1cb6de2fb83bfb7df0c4a5e&language=ko-kr&page=2&region=kr'
def page2():
  r = requests.get(url2)
  movie_dict = r.json()
  conn = sqlite3.connect('db.sqlite3')
  for i in range(0, 20):
      id = i+21
      title = movie_dict['results'][i]['title']
      img_url = f"https://image.tmdb.org/t/p/w500{movie_dict['results'][i]['poster_path']}"
      story = movie_dict['results'][i]['overview']
      story = story.replace("'", "‘")
      people = movie_dict['results'][i]['popularity']
      rate = movie_dict['results'][i]['vote_average']
      genre = movie_dict['results'][i]['genre_ids']
      real_genre = []
      for j in range(len(genre)):
          for k in genres:
              if str(genre[j]) == k:
                    real_genre.append(genres[k])
      final_genre = ' '.join(real_genre)
      c = conn.cursor()
      c.execute(f"INSERT INTO movies_movies VALUES ('{i+21}', '{title}', '{img_url}','{story}' ,'{people}', '{rate}', '{final_genre}')")
      
      conn.commit()
  conn.close()

url3 = 'https://api.themoviedb.org/3/movie/now_playing?api_key=fcca119ad1cb6de2fb83bfb7df0c4a5e&language=ko-kr&page=3&region=kr'
def page3():
  r = requests.get(url3)
  movie_dict = r.json()
  conn = sqlite3.connect('db.sqlite3')
  for i in range(0, 20):
      id = i+41
      title = movie_dict['results'][i]['title']
      img_url = f"https://image.tmdb.org/t/p/w500{movie_dict['results'][i]['poster_path']}"
      story = movie_dict['results'][i]['overview']
      story = story.replace("'", "‘")
      people = movie_dict['results'][i]['popularity']
      rate = movie_dict['results'][i]['vote_average']
      genre = movie_dict['results'][i]['genre_ids']
      real_genre = []
      for j in range(len(genre)):
          for k in genres:
              if str(genre[j]) == k:
                    real_genre.append(genres[k])
      final_genre = ' '.join(real_genre)
      c = conn.cursor()
      c.execute(f"INSERT INTO movies_movies VALUES ('{i+41}', '{title}', '{img_url}','{story}' ,'{people}', '{rate}', '{final_genre}')")
      
      conn.commit()
  conn.close()


url4 = 'https://api.themoviedb.org/3/movie/now_playing?api_key=fcca119ad1cb6de2fb83bfb7df0c4a5e&language=ko-kr&page=4&region=kr'
def page4():
  r = requests.get(url4)
  movie_dict = r.json()
  conn = sqlite3.connect('db.sqlite3')
  for i in range(0, 20):
      id = i+61
      title = movie_dict['results'][i]['title']
      img_url = f"https://image.tmdb.org/t/p/w500{movie_dict['results'][i]['poster_path']}"
      story = movie_dict['results'][i]['overview']
      story = story.replace("'", "‘")
      people = movie_dict['results'][i]['popularity']
      rate = movie_dict['results'][i]['vote_average']
      genre = movie_dict['results'][i]['genre_ids']
      real_genre = []
      for j in range(len(genre)):
          for k in genres:
              if str(genre[j]) == k:
                    real_genre.append(genres[k])
      final_genre = ' '.join(real_genre)
      c = conn.cursor()
      c.execute(f"INSERT INTO movies_movies VALUES ('{i+61}', '{title}', '{img_url}','{story}' ,'{people}', '{rate}', '{final_genre}')")
      
      conn.commit()
  conn.close()

url5 = 'https://api.themoviedb.org/3/movie/now_playing?api_key=fcca119ad1cb6de2fb83bfb7df0c4a5e&language=ko-kr&page=5&region=kr'
def page5():
  r = requests.get(url5)
  movie_dict = r.json()
  conn = sqlite3.connect('db.sqlite3')
  for i in range(0, 5):
      id = i+81
      title = movie_dict['results'][i]['title']
      img_url = f"https://image.tmdb.org/t/p/w500{movie_dict['results'][i]['poster_path']}"
      story = movie_dict['results'][i]['overview']
      story = story.replace("'", "‘")
      people = movie_dict['results'][i]['popularity']
      rate = movie_dict['results'][i]['vote_average']
      genre = movie_dict['results'][i]['genre_ids']
      real_genre = []
      for j in range(len(genre)):
          for k in genres:
              if str(genre[j]) == k:
                    real_genre.append(genres[k])
      final_genre = ' '.join(real_genre)             
      c = conn.cursor()
      c.execute(f"INSERT INTO movies_movies VALUES ('{i+81}', '{title}', '{img_url}','{story}' ,'{people}', '{rate}', '{final_genre}')")
      
      conn.commit()
  conn.close()


page1()
time.sleep(2)
page2()
time.sleep(1.5)
page3()
time.sleep(1.5)
page4()
time.sleep(1.5)
page5()




