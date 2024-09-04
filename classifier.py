import ast
from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.models as models
from torch import __version__
import torch

resnet18 = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
alexnet = models.alexnet(weights=models.AlexNet_Weights.IMAGENET1K_V1)
vgg16 = models.vgg16(weights=models.VGG16_Weights.IMAGENET1K_V1)

models_dict = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

with open('imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

def classifier(img_path, model_name):
    img_pil = Image.open(img_path)

    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    img_tensor = preprocess(img_pil)
    
    img_tensor.unsqueeze_(0)
    
    pytorch_ver = __version__.split('.')
    
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        img_tensor.requires_grad_(False)
    else:
        data = Variable(img_tensor, volatile=True)

    model = models_dict[model_name]

    model.eval()
    
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        output = model(img_tensor)
    else:
        output = model(data)

    _, pred_idx = torch.max(output, 1)
    
    return imagenet_classes_dict[pred_idx.item()]
