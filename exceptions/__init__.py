class UserNotOwner(Exception):
    """
    Thrown when a user is attempting something, but is not an owner of the guild.
    """

    def __init__(self, message="User is not an owner of the guild!"):
        self.message = message
        super().__init__(self.message)
