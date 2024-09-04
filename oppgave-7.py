from lib import parseFloat

def kineticEnergy(mass, velocity):
    return 0.5*mass*velocity**2

mass = parseFloat("Masse i kg: ")
velocity = parseFloat("Hastighet i m/s: ")

print(f"Kinetisk energi = {kineticEnergy(mass, velocity)}")