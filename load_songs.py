import pandas as pd

def get_songs_by_emotion(emotion, csv_file='songs.csv'):
    try:
        df = pd.read_csv(csv_file)
        filtered = df[df['emotion'].str.lower() == emotion.lower()]
        return filtered[['song_name', 'artist', 'url']].to_dict(orient='records')
    except Exception as e:
        print("Error loading songs:", e)
        return []
