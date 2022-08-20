from configparser import MAX_INTERPOLATION_DEPTH
import http.client
import json

print("Welcome to song lyrics search (Powered by Genius) \n")

print("Please enter the name of the artist: \n")
artistFirstName = input()

print("Please enter the last name of the artist: \n")
artistLastName = input()

print("Please enter the name of the song: \n")
song = input()

print("Searching artist... \n")
# Future improvement, add a timer so it prints every second until we get a reply.
# Add logic in case artist not found, also improve one line imput artist, instead of first and last name.

conn = http.client.HTTPSConnection("genius-song-lyrics1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "0d2c926864msh1bbce36628c20f8p183728jsn27ae298d4ecc",
    'X-RapidAPI-Host': "genius-song-lyrics1.p.rapidapi.com"
}

conn.request("GET", "/search?q="+artistFirstName+"%20" +
             artistLastName+"&per_page=10&page=1", headers=headers)

res = conn.getresponse()
print("Artist found!")
dataJson = json.loads(res.read().decode())
highlights = dataJson["response"]["hits"]

obtainedList = []

for highlight in highlights:
    id = highlight["result"]["id"]
    fullTitle = highlight["result"]["full_title"]
    y = {"id": id, "fullTitle": fullTitle}
    obtainedList.append(y)

i = 0
songFound = []

for item in obtainedList:
    songTitle = str(obtainedList[i]["fullTitle"])
    if str(song) in songTitle:
        print("Song found!")
        songFound.append(obtainedList[i])
    i = i + 1

id = 0
for songId in songFound:
    id = songId["id"]

id = str(id)

print("Searching lyrics now for you... Thank you for the patience ;) \n")
# Future improvement, add a timer so it prints every second until we get a reply.
# Add different types of replies to make it more interactive.

if id != 0:
    try:
        headers = {
            'X-RapidAPI-Key': "0d2c926864msh1bbce36628c20f8p183728jsn27ae298d4ecc",
            'X-RapidAPI-Host': "genius-song-lyrics1.p.rapidapi.com"
        }
        conn.request("GET", "/songs/"+id+"/lyrics", headers=headers)
        res = conn.getresponse()
        dataJson = json.loads(res.read().decode())
        print(dataJson["response"]["lyrics"]["lyrics"]["body"]["plain"])
    except:  # This is the correct syntax
        print("Unfortunately lyrics are not in our records at the time, please feel free to test another Artist and Song :)")
    # Add a possibility to re run the program again if user would like or exit.
else:
    print("The artist's song was not found, please feel free to test another Artist and Song :)")


# Good Test: Alan / Walker / Faded.
# Bad Test: Post / Malone / Circles.
# Bad Test: Post / Malone / Hello > But unexpected output.
# https://rapidapi.com/Glavier/api/genius-song-lyrics1/
