class CrossWalkNotFound(Exception):
    def __init__(
        self, message="No crosswalk found for source column to target column."
    ):
        super(CrossWalkNotFound, self).__init__(message)


class MultipleCrossWalksFound(Exception):
    def __init__(
        self, message="Multiple crosswalks found for source column to target column."
    ):
        super(MultipleCrossWalksFound, self).__init__(message)
