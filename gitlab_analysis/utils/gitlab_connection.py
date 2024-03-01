"""
File: gitlab_connection.py
Author: Steven "Kabbe" Karbjinsky
Description: ...

For more information, see: https://github.com/xKabbe/spark
"""
import gitlab
from dotenv import load_dotenv, dotenv_values
from gitlab.v4.objects import Project
from gitlab import Gitlab


class GitLabConnection:
    def __init__(self) -> None:
        load_dotenv()
        self._config = dotenv_values()

        self.url = self._config['gitlab.url']
        self.token = self._config['gitlab.token']
        self.project_id = self._config['gitlab.project_id']

        print(self.url)
        print(self.token)
        print(self.project_id)

        self._gl: Gitlab | None = None

    def connect(self, url: str | None = None, token: str | None = None) -> None:
        if url is None:
            url = self.url
        if token is None:
            token = self.token

        self._gl = gitlab.Gitlab(url=url, private_token=token)
        self._gl.auth()

    def provide_project(self, project_id: int | None = None) -> Project:
        if project_id is None:
            project_id = self.project_id

        return self._gl.projects.get(id=project_id)
