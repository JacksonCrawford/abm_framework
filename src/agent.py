class Agent():
    def __init__(self, x, y):
        self.position = [x, y]
        self.contents = dict()
        self.contents["value"] = 1

    def get_contents(self):
        return self.contents
    
    def get_contents_at(self, key):
        return self.contents[key]

    def set_contents(self, key, value):
        self.contents[key] = value

    def add_content(self, key, increase):
        self.contents[key] += increase

    def set_pos(self, new_x, new_y):
        self.position = [new_x, new_y];

    def move_left(self):
        self.position[0] -= 1

    def move_right(self):
        self.position[0] += 1
    
    def move_down(self):
        self.position[1] -= 1
    
    def move_up(self):
        self.position[1] += 1
