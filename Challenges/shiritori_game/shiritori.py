class Shiritori:

    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, given_word):
        if self.game_over or given_word in self.words:
            return "game over"
        if len(self.words) < 1:
            self.words.append(given_word)
            return self.words
        else:
            prev = self.words[-1][-1]
            current = given_word[0]
            if prev != current:
                self.game_over = True
                return "game over"
            else:
                self.words.append(given_word)
                return self.words

    def restart(self):
        self.game_over = False
        self.words = []
        return "game restarted"


