class User:

    def __init__(self):
        self.__username = ""
        self.__password = ""
        self.__role = ""

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_role(self):
        return self.__role

    def set_username(self, username: str):
        self.__username = username

    def set_password(self, password: str):
        self.__password = password

    def set_role(self, role: str):
        self.__role = role

