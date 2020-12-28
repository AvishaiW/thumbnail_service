class InputsError(Exception):
    """
    If inputs received are flawed, use this Error class
    """
    def __init__(self, message):
        super().__init__(message)