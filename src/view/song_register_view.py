import subprocess
import platform

class SongRegisterView:
    def registry_song_initial(self) -> dict:
        self.__clear()
        
        print ('Implementar Nova Musica \n\n')
        
        title = input('Determine o nome da musica: ')
        artist = input('Determine o nome do artista: ')
        year = input('Determine o ano de publicação: ')
        
        new_song_informations = {
            'title': title, 'artist': artist, 'year': year
        }
        
        return new_song_informations
    
    
    def __clear(self):
        command = 'cls' if platform.system() == 'Windows' else 'clear'
        subprocess.run(command, shell=True)