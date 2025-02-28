class Request:
    """Handles elevator requests from a specific floor."""

    def __init__(self, floor):
        self.floor = floor  # The floor number where the request was made