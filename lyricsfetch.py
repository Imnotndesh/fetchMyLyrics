import azapi
import time
action = 0
API = azapi.AZlyrics('google', accuracy=0.5)

class application():
    def lyfetchByBoth(self,artist,track):
        API.artist = artist
        API.title = track
        API.getLyrics(save=True, ext='lrc')
        print(f"{API.lyrics}\n")
        print(f"{API.title} by {API.artist}")
    
    def lyfetchByTrack(self,track):
        API.title = track
        API.getLyrics(save=True, ext='lrc')
        print(f"{API.lyrics}\n")
        print(f"{API.title} by {API.artist}")  

    def lyfetchByArtistName(self,artist):
        API.artist = artist
        songs = API.getSongs()
        songList = []
        count = 1
        print(f"{artist} songs include: \n")
        for song in songs:
            songList.append(song)
            print(f"{count}: {song}")
            count=count+1
        songNum=int(input("Enter song number: ")) - 1
        print(f"You picked {songList[songNum]}")
        songSelect= songList[songNum]
        API.title = songSelect
        API.getLyrics(save=True, ext='lrc')
        print(f"{API.lyrics}\n")
        print(f"{API.title} by {API.artist}")         
        
    def Welcome(self):
        action=int(input('''
        What would you want to do?
            1. Search by artist name and track
            2. Search by track name only (not acccurate)
            3. Search by artist catalog
            4. Quit
        '''))

        while action != 4:
            if action == 1:
                artist=input("Enter artist name: ")
                track =input("Enter track name: ")
                self.lyfetchByBoth(artist,track)
                self.Welcome()

            elif action == 2:
                track = input("Enter track name: ")
                self.lyfetchByTrack(track)
                self.Welcome()

            else:
                artist = input("Enter artist name: ")
                self.lyfetchByArtistName(artist)
                self.Welcome()

        else:
            print("Thank you for using Lyrics Fetcher by Brian")
            quit()


main = application()
print("Welcome to the lyrics fetcher (powered by azapi)..")
main.Welcome()