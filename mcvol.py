from random import uniform as urand

def mc_volume(num_points: int, p: int = 2, dim: int = 3) -> float:
    """
    Compute the approximate volume of an n-dimensional sphere via monte carlo
    using embedded function call

    Parameters:
    num_points: number of iterations
    p: as in p-norm
    dim: dimension of geometry

    Output:
    float: approximate volume of unit sphere
    """
    inside_count = 0
    cube_vol = 2**dim
    for _ in range(num_points):
        if sphere_sample(p, dim):
            inside_count += 1
    volume_estimate = (inside_count / num_points) * cube_vol
    return volume_estimate

def sphere_sample(p, dim):
    rand_norm = sum(urand(-1,1)**p for _ in range(dim))**(1/p)
    return rand_norm < 1

def mc_volume_fast(num_points, p, dim = 3):
    """
    Compute the approximate volume of an n-dimensional sphere via monte carlo
    using inline sampling code
    """
    inside_count = 0
    cube_vol = 2**dim
    for _ in range(num_points):
        rand_norm = sum(urand(-1,1)**p for _ in range(dim))**(1/p)
        if rand_norm < 1:
            inside_count += 1
    volume_estimate = (inside_count / num_points) * cube_vol
    return volume_estimate

