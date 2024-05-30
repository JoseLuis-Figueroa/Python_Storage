# Dictionaries playlist

playlist = {
    'title': 'Europe journey',
	'author': 'John steele',
	'songs':[
	    {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
		{'title': 'song2', 'artist': ['blue', 'red'], 'duration': 5.5},
		{'title': 'song12', 'artist': ['Katty'], 'duration': 2.2}
	]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
	
print(total_length)