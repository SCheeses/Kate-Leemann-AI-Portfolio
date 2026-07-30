# Computer Vision - ITAI 1378

## Course Overview

In ITAI 1378, I developed the foundations needed to represent, process, classify, and evaluate visual data. I organize this folder with the assignment names shown in my gradebook so each artifact is easy to identify.

## Assignment Map

| Assignment | Portfolio artifact |
| --- | --- |
| A01 ITAI 1378 Colab and other Tools Practice Run | [Workflow reflection](Supplemental-Work/A01_ITAI_1378_Colab_and_Other_Tools_Practice_Run.pdf) |
| A02 "Image Processing Adventure Quest" | [Image-format design assignment](Supplemental-Work/A02_Image_Processing_Adventure_Quest.pdf) |
| L01 Exploring Real-World Applications of Computer Vision | [Medical image analysis](Supplemental-Work/L01_Exploring_Real-World_Applications_of_Computer_Vision.pdf) |
| L02: Image Processing Fundamentals | [Executed project](Projects/L02-Image-Processing-Fundamentals/) |
| L03 Using Classic ML in Computer Vision | [Executed project](Projects/L03-Using-Classic-ML-in-Computer-Vision/) |
| L04 Chihuahua or Muffin | [Executed project](Projects/L04-Chihuahua-or-Muffin/) |
| L05 Chihuahua or Muffin with CNN | [Executed project](Projects/L05-Chihuahua-or-Muffin-with-CNN/) |
| Midterm: Final Project Proposal | [LabRack Vision QA proposal](Capstone-Concept/Midterm-Final-Project-Proposal/) |
| Course Portfolio | This repository |

## Learning Progression

1. **Context and responsible use** - I researched medical image analysis, benefits, validation gaps, and human oversight.
2. **Digital image formats** - I compared RAW, JPEG, PNG, BMP, TIFF, HEIF, and AVIF through a visual design assignment.
3. **Image processing** - I implemented channel analysis, grayscale conversion, point operations, convolution, histogram enhancement, and geometric transforms.
4. **Classical classification** - I trained a linear SVM on a three-class CIFAR-10 subset and analyzed its confusion matrix.
5. **Neural networks** - I built and trained a PyTorch multilayer perceptron for the Chihuahua-versus-muffin task.
6. **Convolutional neural networks** - I replaced flattened pixels with learned spatial features and compared the CNN with my earlier model.
7. **Applied project design** - My teammate and I proposed a privacy-conscious laboratory rack inspection assistant using object detection and instance segmentation.

## Completed Projects

### [L02: Image Processing Fundamentals](Projects/L02-Image-Processing-Fundamentals/)

I used this executed OpenCV notebook to explore image matrices, color channels, convolution kernels, histogram methods, geometric transforms, and three original quantitative experiments.

### [L03 Using Classic ML in Computer Vision](Projects/L03-Using-Classic-ML-in-Computer-Vision/)

I built a classical machine-learning workflow using 15,000 training images and 3,000 test images from the cat, dog, and ship classes. My model achieved 54.7% test accuracy and exposed the limitations of flattened grayscale pixels.

### [L04 Chihuahua or Muffin](Projects/L04-Chihuahua-or-Muffin/)

I trained a PyTorch multilayer perceptron on 120 images and evaluated it on 30 validation images. My saved run reached 86.67% validation accuracy while demonstrating why a convolutional architecture would be a stronger next step.

### [L05 Chihuahua or Muffin with CNN](Projects/L05-Chihuahua-or-Muffin-with-CNN/)

I built a three-block convolutional neural network with data augmentation and compared it with my L04 multilayer perceptron. My saved run reached 96.67% validation accuracy, or 29 correct predictions out of 30.

## Capstone Concept

### [Midterm: Final Project Proposal](Capstone-Concept/Midterm-Final-Project-Proposal/)

My teammate and I developed this midterm proposal for a YOLO11/YOLO11-seg assistant that would detect staged laboratory rack components and produce a human-reviewable QA summary. I present this folder as a proposal, not as a claim of completed implementation.

## Supplemental Work

In the [Supplemental Work](Supplemental-Work/) folder, I include research, technical reflection, and visual communication assignments that provide context for my completed notebooks.

[Return to the main portfolio](../)
