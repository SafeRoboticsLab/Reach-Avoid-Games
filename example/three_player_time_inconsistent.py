import os

cmd = "python3 run.py                                       \
        --env_type t_intersection                           \
        --no_players 3                                      \
        --player_types car car ped                          \
        --init_states                                       \
            7.5 0.0 1.563 0.0 5.0                           \
            3.75 40.0 -1.563 0.0 10.0                       \
            -2.0 30.0 0.0 2.0                               \
        --draw_roads --draw_human --draw_cars               \
        "

os.system(cmd)