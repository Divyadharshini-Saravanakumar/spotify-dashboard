#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install spotipy pandas')


# In[5]:


import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import time

# === YOUR SPOTIFY APP CREDENTIALS ===
client_id = "de3f00dfd59149349099805f365be57d"
client_secret = "c4e3306a05a94d0aaee1e2973b65f04b"

# === AUTHENTICATE WITH SPOTIFY ===
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# === LOAD YOUR DATASET ===
file_path = "spotify-2023.csv"  # Make sure the file is in the same directory or update the path
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# === FUNCTION TO FETCH COVER URL ===
def get_cover_url(track_name, artist_name):
    query = f"track:{track_name} artist:{artist_name}"
    try:
        results = sp.search(q=query, limit=1, type='track')
        items = results['tracks']['items']
        if items:
            return items[0]['album']['images'][0]['url']
    except Exception as e:
        print(f"Error for {track_name} by {artist_name}: {e}")
    return None

# === ADD COVER URL COLUMN ===
df['cover_url'] = df.apply(lambda row: get_cover_url(row['track_name'], row["artist(s)_name"]), axis=1)

# === SAVE UPDATED DATASET ===
df.to_csv("spotify_2023_with_covers.csv", index=False)
print("✅ Done! Saved as 'spotify_2023_with_covers.csv'")


# In[ ]:




