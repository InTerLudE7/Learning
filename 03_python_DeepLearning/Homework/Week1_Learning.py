import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# Set seed
torch.manual_seed(0)
np.random.seed(0)

# True function m(x)
def m(x):
    relu = nn.ReLU()
    return relu(2 * relu(x) - 4 * relu(x - 0.5))

# Nested m(m(m(x)))
def m3(x):
    return m(m(m(x)))

# Generate 1000 data points
x_train = torch.linspace(-0.5, 1.5, 1000).unsqueeze(1)
y_train = m3(x_train)

# Model 1: Shallow structure
class ShallowNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(1, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.model(x)


# Model 2: Deep structured
class DeepStructuredNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.block1 = nn.Sequential(
            nn.Linear(1, 2),
            nn.ReLU(),
            nn.Linear(2, 1),
            nn.ReLU()
        )
        self.block2 = nn.Sequential(
            nn.Linear(1, 2),
            nn.ReLU(),
            nn.Linear(2, 1),
            nn.ReLU()
        )
        self.block3 = nn.Sequential(
            nn.Linear(1, 2),
            nn.ReLU(),
            nn.Linear(2, 1),
            nn.ReLU()
        )

    def _make_block(self):
        return nn.Sequential(
            nn.Linear(8, 8),
            nn.ReLU(),
            nn.Linear(8, 8),
            nn.ReLU()
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return x

# Training function
def train(model, x, y, epochs=10000, lr=0.001):
    criterion = nn.MSELoss()
    # criterion = nn.SmoothL1Loss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    losses = []
    for epoch in range(epochs):
        optimizer.zero_grad()
        output = model(x)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
    return model, losses


# weights initialization
def init_weights_he(m):
    if isinstance(m, nn.Linear):
        nn.init.kaiming_normal_(m.weight, nonlinearity='relu')
        if m.bias is not None:
            nn.init.zeros_(m.bias)
            
# 初始化并训练 ShallowNet
shallow_model = ShallowNet()
shallow_model.apply(init_weights_he)
shallow_model, shallow_losses = train(shallow_model, x_train, y_train)

# 初始化并训练 DeepStructuredNet
deep_model = DeepStructuredNet()
deep_model.apply(init_weights_he)
deep_model, deep_losses = train(deep_model, x_train, y_train)

# # Train both models
# shallow_model, shallow_losses = train(ShallowNet(), x_train, y_train)
# deep_model, deep_losses = train(DeepStructuredNet(), x_train, y_train)


# Predict
with torch.no_grad():
    x_plot = x_train.squeeze().numpy()
    y_true = y_train.squeeze().numpy()
    y_shallow = shallow_model(x_train).squeeze().numpy()
    y_deep = deep_model(x_train).squeeze().numpy()
# Plot Losses
plt.figure(figsize=(10, 4))
plt.plot(shallow_losses, label='ShallowNet Loss')
plt.plot(deep_losses, label='DeepStructuredNet Loss')
# plt.yscale('log')  # 可选：对数尺度查看收敛趋势
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.title("Training Loss Comparison")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot Learning Results
plt.figure(figsize=(10, 5))
plt.plot(x_plot, y_true, label='True $m^{(3)}(x)$', color='black', linewidth=2)
plt.plot(x_plot, y_shallow, label='ShallowNet', linestyle='--')
plt.plot(x_plot, y_deep, label='DeepStructuredNet', linestyle=':')
plt.title("Shallow vs DeepStructured Network on $m^{(3)}(x)$")
plt.xlabel("x")
plt.ylabel("Output")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
