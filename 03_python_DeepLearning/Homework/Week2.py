import torch

class Perceptron(torch.nn.Module):
    def __init__(self, input_size):
        super(Perceptron, self).__init__()
        self.weights = torch.nn.Parameter(torch.rand(input_size, 1),requires_grad=True)
        self.bias = torch.nn.Parameter(torch.rand(1), requires_grad=True)
        
    def forward(self, x):
        z = torch.matmul(x, self.weights) + self.bias
        return torch.sigmoid(z)

input_size = 2
model = Perceptron(input_size)

# Generate example input data
X = torch.tensor([[0.5, 0.5], [0.1, 0.9], [0.8, 0.2]], dtype=torch.float32)
outputs = model(X)
print("Model outputs:", outputs)
