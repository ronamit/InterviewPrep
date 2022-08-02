# input: scenario at time t
# output: feature vector x - R^d

# m = minimal distance of AV to obstacle (m >= 0) (meter)

# if m < 0.5
#   x[0] = -1 / m
# elif 0.5 <= m < 2
#   x[0] = -2 + 2*(m - 0.5)
# else: (m >= 2)
# x[0] = 1

import numpy as np


def compute_reward(state, action):

    obstacles_pos_traj = state.obstacles_pos  # np array [2 X n_obstacles X time_steps] x,y
    ego_pos_traj = action.ego_pos_traj  # np array [2 X time_steps] x,y

    time_horizon = 5  # sec
    sample_freq = 20  # sec
    time_steps = time_horizon * sample_freq
    d = time_steps
    x = np.zeros(d)
    for i in range(time_steps):
        ego_pos = ego_pos_traj[:, i]  # np array [2] x,y
        obstacles_pos = obstacles_pos_traj[:, :, i]   # np array [2 X n_obstacles] x,y
        m = np.min(np.norm(ego_pos - obstacles_pos))
        if m < 0.5:
            x[i] = -1 / m
        elif 0.5 <= m < 2:
            x[i] = -2 + 2 * (m - 0.5)
        else:  # (m >= 2)
            x[i] = 1
    return x
