# L05 Chihuahua or Muffin with CNN

## Problem Statement

Can a convolutional neural network distinguish visually similar Chihuahua and muffin images more accurately than the multilayer perceptron I used in L04? In this project, I preserve spatial image structure with convolutional layers and compare the two approaches.

## Approach

1. I loaded the same staged Chihuahua/muffin dataset used in L04: 120 training images and 30 validation images.
2. I resized each RGB image to 64 by 64 pixels.
3. I augmented the training data with random horizontal flips and rotations.
4. I normalized the image channels with ImageNet statistics.
5. I built three convolutional blocks with 32, 64, and 128 filters, ReLU activations, and max pooling.
6. I used a 512-unit fully connected layer, dropout, and a two-class output layer.
7. I trained with cross-entropy loss and Adam at a learning rate of 0.001 for ten epochs.
8. I ran a controlled comparison between learning rates of 0.001 and 0.0005 with matched starting conditions.

## Results

| Metric | Result |
| --- | ---: |
| Final training accuracy | 94.17% |
| Final validation accuracy | 96.67% |
| Correct validation predictions | 29 of 30 |
| L04 multilayer-perceptron validation accuracy | 86.67% |

In my saved run, the CNN improved validation accuracy by 10 percentage points over my L04 model. In the separate seeded learning-rate comparison, both tested rates reached 93.33%, so that small experiment did not establish that either rate was better.

![CNN validation predictions](results/validation_predictions.png)

## Limitations

- I used only 120 training images and 30 validation images.
- I used one validation split and did not preserve a separate holdout test set.
- A one-image change moves validation accuracy by 3.33 percentage points.
- Data augmentation improves variety but does not replace collecting additional independent images.
- I treat the reported score as the result of this saved classroom run, not as a general benchmark.

## Key Findings

- I found that convolutional layers retained spatial patterns that the flattened L04 input discarded.
- I observed a 10-point validation improvement in the saved CNN run.
- I learned that reproducible controlled comparisons require matched seeds and starting weights.
- I found that equivalent results in the learning-rate comparison were inconclusive rather than evidence that the rates are universally interchangeable.

## Technologies Used

- Python
- PyTorch and TorchVision
- NumPy
- Matplotlib
- tqdm
- Google Colab/Jupyter

## Dataset and Attribution

I used the staged Chihuahua/muffin image dataset from [patitimoner/workshop-chihuahua-vs-muffin](https://github.com/patitimoner/workshop-chihuahua-vs-muffin). I do not duplicate the data in this portfolio; the first notebook cell clones the source repository.

I credit the workshop structure and source material to the original repository. I completed and executed the CNN workflow, added a controlled learning-rate comparison, interpreted the saved results, and wrote the accompanying report.

## How to Run

1. Start a fresh Google Colab runtime.
2. Open [`L05_Chihuahua_or_Muffin_with_CNN.ipynb`](L05_Chihuahua_or_Muffin_with_CNN.ipynb).
3. Select **Runtime > Run all**.
4. The first cell clones the credited workshop repository and changes into its directory.

For local execution, install [`requirements.txt`](requirements.txt), ensure Git is available, and run the notebook from a directory where it can clone the workshop repository.

## Files

- [`L05_Chihuahua_or_Muffin_with_CNN.ipynb`](L05_Chihuahua_or_Muffin_with_CNN.ipynb) - executed source notebook
- [`results/validation_predictions.png`](results/validation_predictions.png) - all saved validation predictions
- [`report/L05_Chihuahua_or_Muffin_with_CNN_Report.pdf`](report/L05_Chihuahua_or_Muffin_with_CNN_Report.pdf) - full project report
- [`requirements.txt`](requirements.txt) - Python dependencies

[Return to the ITAI 1378 overview](../../)
