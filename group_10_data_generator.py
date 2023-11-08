#Group: Brandon, Shane, Ming, Alley
import random
import matplotlib.pyplot as plt

# Created a class (Game scoring generator)
class GameScoringGenerator:

#constructor with lots of default values and must not be a limit to the number of values that you can get from your generator
    def __init__(self, amp=200, freq=0.1, num_sessions=50): 
        self.amplitude = amp
        self.frequency = freq
        self.num_sessions = num_sessions

# private method that will generate random values in the range 0-1
    def _generate_random_value(self): 
        return random.uniform(0, 1)

# public property that will use the above member to return a value in your preferred range, y = mX + c
    @property
    def random_score(self):
        xmin = 0
        xmax = 1000
        m = xmax - xmin
        c = xmin
        x = self._generate_random_value()
        return m * x + c

# Matplotlib library to display score data values
    def generate_score_data(self):
        sessions = list(range(1, self.num_sessions + 1))
        scores = [self.random_score for _ in range(self.num_sessions)]
        return sessions, scores

    def plot_score_data(self, num_sessions):
        sessions, scores = self.generate_score_data()

        plt.figure(figsize=(10, 5))
        plt.plot(sessions, scores, marker='o', linestyle='-', color='b')
        plt.title('Random Game Scoring Data')
        plt.xlabel('Session')
        plt.ylabel('Score')
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    score_generator = GameScoringGenerator(amp=300, freq=0.15, num_sessions=20)
    num_sessions = 50
    score_generator.plot_score_data(num_sessions)