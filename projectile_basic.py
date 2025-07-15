import math, time 
import physipy 
g = 9.81

def simulate_projectile_basic(v0: float, theta_deg: float,
                              dt: float, t_max: float):
    theta = math.radians(theta_deg)
    vx0 = v0 * math.cos(theta)
    vy0 = v0 * math.sin(theta)

    mx = Mechanics(initial_velocity=vx0, acceleration=0)
    my = Mechanics(initial_velocity=vy0, acceleration=-g)

    t_vals, x_vals, y_vals = [], [], []
    x, y, vy = 0.0, 0.0, vy0
    t_start = time.time()

    t = 0.0
    while t <= t_max and y >= 0:
        t_vals.append(t)
        x_vals.append(x)
        y_vals.append(y)

        x += mx.initial_velocity * dt          # mx.displacement() would redo v*dt each loop
        my.initial_velocity = vy               # update current vy
        my.time = dt
        Δy, vy = my.uniform_accelerated_motion()
        y += Δy

        # advance time
        t += dt

    latency_s = time.time() - t_start
    return t_vals, x_vals, y_vals, latency_s
