import time
import mcvol

if __name__ == '__main__':
    num_points = 10**6   # Number of points to sample
    p = 2
    n_dim = 3

    # start_time = time.time()
    # volume_estimate_fast = mcvol.mc_volume_fast(num_points, p)
    # end_time = time.time()
    # inline_time = end_time - start_time

    start_time = time.time()
    volume_estimate = mcvol.mc_volume(num_points, p, n_dim)
    end_time = time.time()
    fun_time = end_time - start_time

    print(f"Volume = {volume_estimate}")
    print(f"Inline: {fun_time} seconds.")
    print(f"Function: {fun_time} seconds.")
