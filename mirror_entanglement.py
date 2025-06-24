import matplotlib.pyplot as plt
import numpy as np

class Particle:
    def __init__(self, name):
        self.name = name
        self.state = None  # Vector [x, y]

    def measure(self, value):
        self.state = value
        print(f"{self.name} measured: {self.state}")

class MirrorEntanglement:
    def __init__(self):
        self.A = Particle("Particle A")
        self.B = Particle("Particle B (Mirror)")

    def measure_A(self, value):
        self.A.measure(value)
        self.B.measure(self.reflect(value))

    def reflect(self, value):
        return [-value[0], -value[1]]  # Vector mirror

    def plot(self):
        fig, ax = plt.subplots()
        ax.quiver(0, 0, self.A.state[0], self.A.state[1], color='b', label='Particle A',
                  angles='xy', scale_units='xy', scale=1)
        ax.quiver(0, 0, self.B.state[0], self.B.state[1], color='r', label='Particle B (Mirror)',
                  angles='xy', scale_units='xy', scale=1)
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.legend()
        ax.grid(True)
        plt.title("🪞 Quantum Mirror Entanglement")
        plt.show()

if __name__ == "__main__":
    system = MirrorEntanglement()
    system.measure_A([1, 0])  # Example: measure "Right"
    system.plot()
