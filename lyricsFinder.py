import http.client
import json
from tkinter.messagebox import RETRY

def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

print("Welcome to song lyrics search (Powered by Genius) \n")

print("Please enter the name of the artist: \n")
artistFirstName = input()

print("Please enter the last name of the artist: \n")
artistLastName = input()

print("Please enter the name of the song: \n")
song = input()

conn = http.client.HTTPSConnection("genius-song-lyrics1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "0d2c926864msh1bbce36628c20f8p183728jsn27ae298d4ecc",
    'X-RapidAPI-Host': "genius-song-lyrics1.p.rapidapi.com"
    }

conn.request("GET", "/search?q="+artistFirstName+"%20"+artistLastName+"&per_page=10&page=1", headers=headers)

res = conn.getresponse()
dataJson = json.loads(res.read().decode())
highlights = dataJson["response"]["hits"]

obtainedList = []

for highlight in highlights:
  id = highlight["result"]["id"]
  fullTitle = highlight["result"]["full_title"]
  y = { "id": id, "fullTitle": fullTitle}
  obtainedList.append(y)

i = 0
songFound = []

for item in obtainedList:
    songTitle = str(obtainedList[i]["fullTitle"])
    if str(song) in songTitle:
        print("Song Found")
        songFound.append(obtainedList[i]) 
    i = i + 1

id = 0
for songId in songFound:
    id = songId["id"]

id = str(id)

if id != 0:
    headers = {
    'X-RapidAPI-Key': "0d2c926864msh1bbce36628c20f8p183728jsn27ae298d4ecc",
    'X-RapidAPI-Host': "genius-song-lyrics1.p.rapidapi.com"
    }
    conn.request("GET", "/songs/"+id+"/lyrics", headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
else:
    print("Song Not Found")



# class number_object(object):
#     def __init__(self, number):
#         self.number = number

# object_0 =  number_object(0)
# object_1 =  number_object(1)
# object_2 =  number_object(2)


# object_list = [object_0, object_1, object_2]

# for obj in object_list:
#      print(obj.number)

# for highlight in dataJson["response"]["hits"]["highlights"]: P
#     print(highlight["id"])
#     print(highlight["full_title"])

#data = data.decode("utf-8")
#print(type(data))
#print(json.loads(data))
#data = json.loads(data)

#Artist.
#IDofSong.
#Lyrics