import requests
import time
import re
import os
import pandas as pd

def grab_poster(dwnldd_img_dir, title, poster_path, label='genre'):

    if not os.path.exists(dwnldd_img_dir):
        os.makedirs(dwnldd_img_dir)
    
    if not os.path.exists(dwnldd_img_dir+'/'+label):
        os.makedirs(dwnldd_img_dir+'/'+label)

    imgUrl = 'http://image.tmdb.org/t/p/w185' + poster_path

    local_filename = re.sub(r'\W+', ' ', title).lower().strip().replace(" ", "-") + '.jpg'

    try:
        session = requests.Session()
        r = session.get(imgUrl, stream=True, verify=False)
        with open(dwnldd_img_dir+'/'+label+'/'+local_filename, 'wb') as file:
            for chunk in r.iter_content(chunk_size=1024):
                file.write(chunk)
    
    except:
        print('problem downloading', title, label, poster_path, imgUrl)

    time.sleep(1)


movies = pd.read_csv('C:/Users/dgall/datascience/rec_poster/movies_metadata.csv', low_memory=False, nrows=10)

movies.dropna()

for index, row in movies.iterrows():
    grab_poster(
        'images_movies_genres',
        str(row['title']),
        # str(row['genre']),
        row['poster_path']
    )