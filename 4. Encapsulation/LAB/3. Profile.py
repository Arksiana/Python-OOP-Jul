class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        count_upper = len([el for el in value if el.isupper()])
        count_dig = len([el for el in value if el.isdigit()])
        if len(value) < 8 or count_upper == 0 or count_dig == 0:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {len(self.__password) * "*"}'


profile_with_invalid_password = Profile('My_username', 'My-password')