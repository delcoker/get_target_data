class CModelTargetException(Exception):
    """Exception raised for errors for C-Model.

        Attributes:
            message -- explanation of the error
        """

    def __init__(self, message="Target model error", errors=None):
        self.message = message
        super().__init__(self.message)

        self.errors = errors
