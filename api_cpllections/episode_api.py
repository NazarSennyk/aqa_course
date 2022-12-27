from utilities.api.BaseAPI import BaseAPI


class EpisodeAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__url_episode = 'api/episode'

    def get_episode_id(self, episode_id: int):
        return self.get(f'{self.__url_episode}/{episode_id}')
