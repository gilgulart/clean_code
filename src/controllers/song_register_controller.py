class SongRegisterController:
    def insert(self, new_song_informations: dict) -> dict:
        try:
        # Principio da responsabilidade única
            self.__verify_if_song_already_registered()
            self.__verify_songs_infos()
            self.__insert_song()
            return  self.__format_response()
        
        except Exception as exception:
            return self.__format_error_response(exception)           
               
    def __verify_if_song_already_registered(new_song_informations: dict) -> None:
        # Interação com Models
        pass
    
    def __verify_songs_infos(new_song_informations: dict) -> None:
        if len(new_song_informations['title']) > 100:
            raise Exception('Título de música com mais de 100 caracteres')
        
        year = int(new_song_informations[year])
        if year > 2026:
            raise Exception('Ano inválido')
        
    def __insert_song() -> None:
        # Interação com Models

        pass
    
    def __format_response(new_songs_informations: dict) -> None:
        return {
            'success': True,
            'count': 1,
            'attributes': {
                'title': new_songs_informations['title']
            }
        }
        
    def __format_error_response(self, err: Exception) -> dict:
        return {
            'success': False,
            'error': str(err)
        }