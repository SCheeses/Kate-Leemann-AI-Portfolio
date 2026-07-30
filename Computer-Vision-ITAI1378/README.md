# Computer Vision - ITAI 1378

## Course Overview

In ITAI 1378, I developed the foundations needed to represent, process, classify, and evaluate visual data. In this folder, I show my progression from individual pixels and hand-designed filters to a classical support vector machine, a small neural network, and a proposed object-detection quality-assurance system.

## Learning Progression

1. **Context and responsible use** - I researched medical image analysis, benefits, validation gaps, and human oversight.
2. **Digital image formats** - I compared RAW, JPEG, PNG, BMP, TIFF, HEIF, and AVIF through a visual design assignment.
3. **Image processing** - I implemented channel analysis, grayscale conversion, point operations, convolution, histogram enhancement, and geometric transforms.
4. **Classical classification** - I trained a linear SVM on a three-class CIFAR-10 subset and analyzed its confusion matrix.
5. **Neural networks** - I built and trained a PyTorch multilayer perceptron for the Chihuahua-versus-muffin task.
6. **Applied project design** - My teammate and I proposed a privacy-conscious laboratory rack inspection assistant using object detection and instance segmentation.

## Completed Projects

### [Image Processing Fundamentals](Projects/01-Image-Processing-Fundamentals/)

I used this executed OpenCV notebook to explore image matrices, color channels, convolution kernels, histogram methods, geometric transforms, and three original quantitative experiments.

### [CIFAR-10 SVM Classifier](Projects/02-CIFAR10-SVM-Classifier/)

I built a classical machine-learning workflow using 15,000 training images and 3,000 test images from the cat, dog, and ship classes. My model achieved 54.7% test accuracy and exposed the limitations of flattened grayscale pixels.

### [Chihuahua or Muffin Neural Network](Projects/03-Chihuahua-Muffin-Neural-Network/)

I trained a PyTorch multilayer perceptron on 120 images and evaluated it on 30 validation images. My saved run reached 86.67% validation accuracy while demonstrating why a convolutional architecture would be a stronger next step.

## Capstone Concept

### [LabRack Vision QA](Capstone-Concept/LabRack-Vision-QA/)

My teammate and I developed this midterm proposal for a YOLO11/YOLO11-seg assistant that would detect staged laboratory rack components and produce a human-reviewable QA summary. I present this folder as a proposal, not as a claim of completed implementation.

## Supplemental Work

In the [Supplemental Work](Supplemental-Work/) folder, I include research, technical reflection, and visual communication assignments that provide context for my completed notebooks.

[Return to the main portfolio](../)
