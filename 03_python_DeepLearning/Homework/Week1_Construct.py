import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

# Define base function m(x)
class M(nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = nn.ReLU()

    def forward(self, x):
        z1 = self.relu(x)
        z2 = self.relu(x - 0.5)
        return self.relu(2 * z1 - 4 * z2)

# Compose m(m(m(x)))
class M3(nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = M()
        self.m2 = M()
        self.m3 = M()

    def forward(self, x):
        return self.m3(self.m2(self.m1(x)))

# Instantiate model
model = M3()

# Evaluate on a range of x
x_np = np.linspace(-0.5, 1.5, 500)
x_tensor = torch.tensor(x_np, dtype=torch.float32)
y_tensor = model(x_tensor)
y_np = y_tensor.detach().numpy()

# Plot
plt.figure(figsize=(8, 4))
plt.plot(x_np, y_np, label=r'$m^{(3)}(x)$', color='blue')
plt.xlabel("x")
plt.ylabel("m(m(m(x)))")
plt.title("Nested ReLU Representation of $m^{(3)}(x)$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
