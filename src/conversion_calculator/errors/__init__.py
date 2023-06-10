class CrossWalkNotFound(Exception):
    def __init__(self, message):
        super(CrossWalkNotFound, self).__init__(message)