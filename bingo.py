import random



class Card():

    def __init__(self):
        self.boxes = []

    def check_figure(self, id_guess, id_figure):
        if id_guess == id_figure:
            return 0
        else:
            return 1
    def fill_boxes(self, diff):
        j = 0
        if diff == 'easy':
            max_range = 10
            min_range = 0
        else:
            max_range = 10
            min_range = 0
        while j < 9:
            ran = random.randint(min_range, max_range)
            if not ran in self.boxes:
                self.boxes.append(ran)
                j += 1

