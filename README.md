
# Dog Breed Identifier

## Project Description
This project utilizes pre-trained convolutional neural networks (CNNs) to classify images of dogs and identify their breeds. The primary objectives are:
1. To accurately distinguish between dog and non-dog images.
2. To classify the breeds of the identified dogs.

The project employs popular CNN architectures such as VGG, AlexNet, and ResNet to achieve high accuracy and efficiency in image classification.

## Table of Contents
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)
- [Additional Resources](#additional-resources)

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/bhaveshasasik/dog_image_classifier.git
   ```

2. Navigate to the project directory:
   ```bash
   cd dog_image_classifier
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To classify images, run the following command:

```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

### Parameters:
- `--dir`: Specify the directory containing the pet images (e.g., `pet_images/`).
- `--arch`: Choose the CNN architecture to use (options: `vgg`, `alexnet`, `resnet`).
- `--dogfile`: Specify the file containing the list of valid dog breeds (e.g., `dognames.txt`).

## Results
The project achieved the following results for dog breed classification:

### **VGG Model**
- Accuracy in breed classification: **93.3%**
- Correctly classified dog images: **100%**
- Correctly classified non-dog images: **100%**

### **AlexNet Model**
- Accuracy in breed classification: **80.0%**
- Correctly classified dog images: **100%**
- Correctly classified non-dog images: **100%**

### **ResNet Model**
- Accuracy in breed classification: **90.0%**
- Correctly classified dog images: **100%**
- Correctly classified non-dog images: **90%**

## License
This project is licensed under the [MIT License](LICENSE).

## Contact Information
For questions or feedback, feel free to reach out:
- **Email**: bhaveshasasik@gmail.com
- **GitHub**: [Bhavesha Sasikumar](https://github.com/bhaveshasasik)

