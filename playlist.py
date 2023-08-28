
class Playlist:
#     add tracks to queue
#  displaying tracks froma file
#  load tracks form text file
    def __init__(self):
        self.playlist = []

    def load(self, path):
        f = open(path, "r")
        self.playlist = f.readlines()
    
    
    def show_tracks(self):
        
        for num, track in enumerate(self.playlist):
            print(f"{num + 1}. {track}")
        
    
    def add_track(self, track):
        
        self.playlist.append(track)
    
    def remove_track(self, pos):
        self.playlist.pop(pos-1)
        
play = Playlist()

play.load("./tracks.txt")

play.show_tracks()

play.add_track("Bohemian Rhapsody")

play.show_tracks()

play.remove_track(4)

play.show_tracks()