from random import shuffle
from random import random
from functools import reduce

class Track:
    def __init__(self, title, artiste, album, duration, genre, year):
        self.title = title
        self.artiste = artiste
        self.album = album
        self.duration = duration
        self.genre = genre
        self.year = year
        

def load_tracks(path):
    
    f = open(path, 'r')
    t_list = []
    
    for track in f.readlines():
        deets = track.split(",")

        t_list.append(Track(deets[0],deets[1], deets[2], deets[3], deets[4],deets[5]))
        
    return t_list
        
# t_list = load_tracks('./tracks.txt')
# print(t_list[2].duration)

    

class Playlist:
#   add tracks to queue
#  displaying tracks froma file
#  load tracks form text file

    def __init__(self):
        self.playlist = []
        
#     def load_tracks(self,path):
#     
#         f = open(path, 'r')
#     
#         
#         for track in f.readlines():
#             deets = track.split(",")
#             t_list.append(Track(deets[0],deets[1], deets[1], deets[2], deets[3],deets[4],deets[5]))
#         
#             return t_list
    

        
#     def __filename(self):
        
        

    def load(self, path):
        self.playlist = load_tracks(path)
    
    
    def show_tracks(self):
        
        for num, track in enumerate(self.playlist):
            print(f"{num + 1}. {track.title}")
        
    
    def add_track(self, title, artiste, album, duration, genre, year):
        
        self.playlist.append(Track(title, artiste, album, duration, genre, year))
    
    def remove_track(self, pos):
        self.playlist.pop(pos-1)
    
    def save_playlist(self, filename):
        
        try:
            new = open(filename + ".txt", 'x')
        except FileExistsError:
            print("Playlist already exists, choose another name")
        
        else:
            for track in self.playlist:
                new.write(f"{track.title}, {track.artiste} {track.album} {track.duration} {track.genre}, {track.year}, \n")
            new.close()
            
    
    def shuffle_playlist(self):
        shuffle(self.playlist)
    
    def count_tracks(self):
        print(f"There are {len(self.playlist)} in the playlist")
        
    def total_duration(self):
        total = 0
        for track in self.playlist:
            duration = track.duration.split(":")
            seconds = int(duration[0]) * 60 + int(duration[1])
            total += seconds
        
        
        print(f"The total duration of this playlist is {total//60} minutes, {total%60}seconds")         
            
        
    def reset(self):
        self.playlist = []
        
    def is_empty(self):
        
        return "Playlist is empty" if len(self.playlist) == 0 else "Playlist is not empty"
    
play = Playlist()

play.load("./tracks.txt")

play.show_tracks()



# play.add_track("Bohemian Rhapsody")

play.show_tracks()

play.remove_track(4)

play.show_tracks()
play.total_duration()
play.shuffle_playlist()
print(play.is_empty())

play.show_tracks()
play.count_tracks()
play.save_playlist("north")
play.reset()

print(play.is_empty())