from phi.jax import flow
import matplotlib.pyplot as plt
from tqdm import tqdm

N_TIME_STEPS = 150

def main():
    velocity = flow.StaggeredGrid(
        values=(0.0, 0.0),
        extrapolation=0.0,
        x=64,
        y=64,
        bounds=flow.Box(x=100, y=100),
    )
    smoke = flow.CenteredGrid(
        values=0.0,
        extrapolation=flow.extrapolation.BOUNDARY,
        x=200,
        y=200,
        bounds=flow.Box(x=100, y=100),
    )
    inflow = 0.2 * flow.CenteredGrid(
        values=flow.SoftGeometryMask(
            flow.Sphere(
                x=40,
                y=9.5,
                radius=5,
            )
        ),
        extrapolation=0.0,
        bounds=smoke.bounds,
        resolution=smoke.resolution,
    )

    @flow.math.jit_compile
    def step(velocity_prev, smoke_prev, dt=1.0):
        smoke_next = flow.advect.mac_cormack(smoke_prev, velocity_prev, dt) + inflow
        buoyancy_force = smoke_next * (0.0, 0.1) @ velocity
        velocity_tent = flow.advect.semi_lagrangian(velocity_prev, velocity_prev, dt) + buoyancy_force * dt
        velocity_next, pressure = flow.fluid.make_incompressible(velocity_tent)
        return velocity_next, smoke_next
    
    plt.style.use("dark_background")
    
    for _ in tqdm(range(N_TIME_STEPS)):
        velocity, smoke = step(velocity, smoke)
        smoke_values_extracted = smoke.values.numpy("y,x")
        plt.imshow(smoke_values_extracted, origin="lower")
        plt.draw()
        plt.pause(0.01)
        plt.clf()
        

if __name__ == "__main__":
    main()