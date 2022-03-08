import spotipy
from spotipy.oauth2 import SpotifyOAuth
#counter for playlist tracks
x = 0
scope = 'playlist-modify-public'
username = 'anthony052001'

#generates an oAuth token for username with the scopes required
token = SpotifyOAuth(scope=scope, username=username)

spotifyObj = spotipy.Spotify(auth_manager=token)

#playlist attributes
playlist_name = input("Enter Playlist Name")
playlist_desc = input("Enter a playlist desc")

#playlist fields
spotifyObj.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_desc)

#takes user input and uses user imput for an array list_of_songs
user_input = input("Welcome to 20Q20Songs! Please Input a seed song:")
list_of_songs = []

#individual track searching and playlist appending
while x < 5:
    result = spotifyObj.search(q=user_input)

    list_of_songs.append(result['tracks']['items'][0]['uri'])
    #this will need to pull random questions, rn just adds the same song
    user_input = input("Do you want a song that's danceable? Y/N:")
    x += 1


print("Enjoy your playlist!")

#prePlaylist that gens while playlist is being made
prePlaylist = spotifyObj.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

#not sure why this has a crossthrough but this is necessary for the playlist to be made, its the spotipy api wrapper call
spotifyObj.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=list_of_songs)
