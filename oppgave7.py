from lib import parseFloat

def kineticEnergy(mass: float, velocity: float) -> float:
    return 0.5*mass*velocity**2

mass: float = parseFloat("Masse i kg: ")
velocity: float = parseFloat("Hastighet i m/s: ")

print(f"Kinetisk energi = {kineticEnergy(mass, velocity)}")