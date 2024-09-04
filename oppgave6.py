def kineticEnergy(mass: float, velocity: float) -> float:
    return 0.5*mass*velocity**2

mass = 5
velocity = 100

print(f"Kinetisk energi = {kineticEnergy(mass, velocity)}")