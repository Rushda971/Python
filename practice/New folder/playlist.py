#iterator or iteration
#playing song from playlist
class song:
    def __init__(self,playlist):
        self.playlist=playlist

    def print(self):
        print(self.playlist)

playlist=["song1","song2","song3","song4"]
music=iter(playlist)
for x in music:
    print(x)
    
#taking pizza orders until done(while loop)
#warehouse scanner(set iteration to avoid duplicate)
#password retry system(allows you to enter password 3 times and then goes in loop)
    
