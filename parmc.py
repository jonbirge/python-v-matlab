import mcvol
import time
from multiprocessing import Pool

if __name__ == '__main__':
    num_points = 10**9   # Number of points to sample
    num_processes = 54   # Number of processes to run in parallel
    n_dim = 2
    p = 2

    start_time = time.time()

    with Pool(num_processes) as pool:
        results = pool.map(mcvol.mc_volume_fast, [num_points // num_processes] * num_processes)
    volume_estimate = sum(results) / num_processes
    
    end_time = time.time()

    print(f"Estimated {p}-norm volume of a {n_dim}-sphere: {volume_estimate}")
    print(f"Time taken: {end_time - start_time} seconds across {num_processes} cores.")
