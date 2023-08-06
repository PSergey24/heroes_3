from modules.settings import Settings, States


class Helper:

    def __init__(self):
        pass

    def is_correct_step(self, new_point, whom_attack):
        old_point = States.queue.current[0].position
        possible_ways = self.get_way(old_point[0], old_point[1], States.queue.current[0].speed)

        if whom_attack:
            if States.queue.current[0].team != whom_attack.team:
                return 'attack_straight'
        if States.fields[new_point[0]][new_point[1]].is_engaged is False and new_point in possible_ways:
            return 'moving'
        return False

    @staticmethod
    def get_way(pos_x, pos_y, speed):
        dp = {}

        def dfs(i, j, cur_speed):
            if i < 0 or i > Settings.n_rows - 1:
                return
            if j < 0 or j > Settings.n_columns - 1:
                return
            if cur_speed > speed:
                return
            if (i, j) in dp and cur_speed > dp[(i, j)]:
                return

            dp[(i, j)] = cur_speed

            if i % 2 == 0:
                dfs(i - 1, j - 1, cur_speed + 1)
                dfs(i + 1, j - 1, cur_speed + 1)
            else:
                dfs(i - 1, j + 1, cur_speed + 1)
                dfs(i + 1, j + 1, cur_speed + 1)

            dfs(i, j + 1, cur_speed + 1)
            dfs(i, j - 1, cur_speed + 1)
            dfs(i - 1, j, cur_speed + 1)
            dfs(i + 1, j, cur_speed + 1)

        dfs(pos_x, pos_y, 0)
        return list(dp.keys())
