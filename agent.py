import torch
import random
from collections import deque
from game_ai import GameAI
from modules.model import LinearQnet, QTrainer
from modules.helper import plot


MAX_MEMORY = 100_000
BATCH_SIZE = 1000


class Agent:

    def __init__(self):
        self.n_games = 0

        self.lr = 0.001
        self.gamma = 0.9
        self.epsilon = 0

        self.model = LinearQnet(495, 4000, 1157)
        self.trainer = QTrainer(self.model, self.lr, self.gamma)
        self.memory = deque(maxlen=MAX_MEMORY)

    @staticmethod
    def get_state(game):
        return game.get_state()

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        self.epsilon = 80 - self.n_games
        final_move = [0] * 1157
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 1156)
            print("random selected action:")
        else:
            state_ = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state_)
            move = torch.argmax(prediction).item()
            print("model selected action:")

        final_move[move] = 1
        return final_move


def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = GameAI()

    while True:
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)

        reward, done, score = game.play_step(final_move)

        state_new = agent.get_state(game)

        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()

            print(f"Game {agent.n_games}, Score {score}, Record {record}")

            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)


if __name__ == '__main__':
    train()


