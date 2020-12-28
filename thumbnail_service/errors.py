class FormatError(Exception):
    def __init__(self, message):
        super().__init__(message)


class InputsError(Exception):
    def __init__(self, message):
        super().__init__(message)