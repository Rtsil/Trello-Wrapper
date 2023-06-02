import abc
import requests
import json


class Get:

    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    def get_all_boards(self):
        """
        Get all boards related to the user
        Returns:
            Json containing all the boards data
        """
        url = f"https://api.trello.com/1/members/me/boards"
        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )
        if response.status_code != 200:
            raise Exception(response.content)
        return response.json()

    def get_boards_ids(self):
        """
        Get Boards Ids
        Returns:

        """
        url = f"https://api.trello.com/1/members/me/boards"
        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )
        if response.status_code != 200:
            raise Exception(response.content)
        return {board["name"]: board["id"] for board in response.json()}

    def get_memberships_of_board(self, id: str):
        """
        Get information about the memberships users have to the board.
        Args:
            id: (string) The ID of the board => Pattern: ^[0-9a-fA-F]{24}$

        Returns:

        """
        url = f"https://api.trello.com/1/boards/{id}/memberships"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return json.loads(response.text)

    def get_board(self, id: str):
        """
        Get a specific board
        Args:
            id: (string) The ID of the board => Pattern: ^[0-9a-fA-F]{24}$

        Returns:

        """
        url = f"https://api.trello.com/1/boards/{id}"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response.json()

    def get_actions(self, id: str):
        """
        Get actions from a board
        Args:
            id: (string) The ID of the board => Pattern: ^[0-9a-fA-F]{24}$

        Returns:

        """
        url = f"https://api.trello.com/1/boards/{id}/actions"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response.json()

    def get_cards(self, id: str):
        """
        Get cards on a board
        Args:
            id: (string) The ID of the board => Pattern: ^[0-9a-fA-F]{24}$

        Returns:

        """
        url = f"https://api.trello.com/1/boards/{id}/cards"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response.json()

    def get_checklist(self, id: str):
        url = f"https://api.trello.com/1/boards/{id}/checklists"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response.json()

    def get_filtered_cards(self, id, filter):
        """
        get filtered cards on a board
        Args:
            id: Boards Id
            filter: (string) Valid Values: all, closed, none, open, visible.

        Returns:

        """
        url = f"https://api.trello.com/1/boards/{id}/cards/{filter}"

        headers = {
            "Accept": "application/json"
        }
        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response.json()

    def get_customFields(self, id):
        """
        Get custom Fields from a board
        Args:
            id: id of the board

        Returns:

        """
        url = f"https://api.trello.com/1/boards/{id}/customFields"

        headers = {
            "Accept": "application/json"
        }
        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response.json()

    def get_labels(self, id):
        """
        Get labels on board
        Args:
            id: id of board

        Returns:

        """
        url = f"https://api.trello.com/1/boards/{id}/labels"


        headers = {
            "Accept": "application/json"
        }
        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response.json()

    def get_lists(self, id):
        """
        Get lists from a board
        Args:
            id: id of board

        Returns:

        """
        url = f"https://api.trello.com/1/boards/{id}/lists"

        headers = {
            "Accept": "application/json"
        }
        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response.json()

    def get_filtered_lists(self, id, filter):
        """
        Args:
            id: Boards Id
            filter: (string) Valid Values: all, closed, none, open, visible.

        Returns:

        """
        url = f"https://api.trello.com/1/boards/{id}/lists/{filter}"

        headers = {
            "Accept": "application/json"
        }
        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response.json()

    def get_members(self, id):
        """
        Get members of a board
        Args:
            id: board_id
        Returns:

        """
        url = f"https://api.trello.com/1/boards/{id}/members"


        headers = {
            "Accept": "application/json"
        }
        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response.json()

    def get_enabled_powerUps(self, id):
        """
        Get the enabled Power-Ups on a board
        Args:
            id: id of the board

        Returns:

        """
        url = f"https://api.trello.com/1/boards/{id}/boardPlugins"
        headers = {
            "Accept": "application/json"
        }
        query = {
            'key': self.api_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        return response.json()