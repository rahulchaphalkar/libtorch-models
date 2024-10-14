# Adapted from tch-rs examples/jit
import torch
import torchvision
from torchvision.models import ResNet18_Weights

model = torchvision.models.resnet18(weights=ResNet18_Weights.DEFAULT)
model.eval()
example = torch.rand(1, 3, 224, 224)
traced_script_module = torch.jit.trace(model, example)
traced_script_module.save("../jit-compiled-models/resnet18.pt")
