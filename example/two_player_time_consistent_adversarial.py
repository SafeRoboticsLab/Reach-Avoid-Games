import os
import numpy as np

cmd = "python3 run.py                                       \
        --env_type t_intersection                           \
        --no_players 2                                      \
        --player_types car car                              \
        --init_states                                       \
            7.5 15.0 {} 0.0 5.0                             \
            3.75 32.0 {} 0.0 7.0                            \
        --draw_roads                                        \
        --alpha_scaling trust_region                        \
        --trust_region_type constant_margin                 \
        --eps_state 0.5 --eps_control 0.3                   \
        --boundary_only                                     \
        --hallucinated                                      \
        --initial_margin 1.0                                \
        --t_horizon 3                                       \
        --time_consistency                                  \
        --t_react 10                                        \
        --plot --log --store_freq 1                         \
        ".format(np.pi/2.0, -np.pi/2.0)

# --draw_roads --draw_human --draw_cars

os.system(cmd)