# Adapted from tch-rs examples/jit
import torch
import torchvision
from torchvision.models import SqueezeNet1_1_Weights

model = torchvision.models.squeezenet1_1(weights=SqueezeNet1_1_Weights.DEFAULT)
model.eval()
example = torch.rand(1, 3, 224, 224)
traced_script_module = torch.jit.trace(model, example)
traced_script_module.save("../jit-compiled-models/squeezenet1_1.pt")
