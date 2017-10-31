# Ship class


class Ship:
    def __init__(self, size, head, orientation):
        self.size = size
        self.head = head
        self.orientation = orientation
        self.status = [1 for i in range(0, self.size)]  # 1 for unhit, 0 for a hit
