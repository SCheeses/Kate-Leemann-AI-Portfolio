# LabRack Vision QA

**Status: Midterm proposal / implementation in progress**

## Our Project Team

- Roderick Taylor
- Kate Leemann

## Problem Statement

Laboratory staff may need to confirm that tubes are present, capped, arranged correctly, and not visibly out of place before a rack moves through a workflow. We propose LabRack Vision QA as a visual assistant that analyzes photos of staged sample racks and produces an annotated image plus a short, human-reviewable QA summary.

We designed this as an educational workflow-assistance concept, not as a diagnostic system, and we do not plan to use real patient data.

## Proposed Approach

1. Photograph a staged rack containing empty tubes, fake labels, and no protected health information.
2. Use pretrained YOLO11 object detection and YOLO11-seg instance segmentation.
3. Detect core classes such as racks, tubes, caps, and empty positions.
4. Apply rule-based checks for tube count, possible empty positions, and visible cap issues.
5. Produce an annotated image and a concise review summary.

## Intended Dataset

- 200-250 staged images for initial development
- 100-150 images for training and validation
- 50-100 independent holdout images
- Fake or blurred label text only
- No patient identifiers, real sample IDs, or clinical decision-making

The dataset has not been committed because collection and labeling are planned work.

## Target Metrics

- At least 0.75 mAP50 on a holdout set for the core classes
- Under three seconds per image in Colab or local Jupyter
- Clear annotated output and QA summary suitable for human review

We present these as design targets, not as completed results.

## Proposed Technologies

- Python
- Ultralytics YOLO11 and YOLO11-seg
- OpenCV
- Google Colab/Jupyter
- Roboflow or Label Studio

## Risks and Safeguards

- If our dataset is too small, we will narrow version 1 to rack, tube, and cap detection.
- If segmentation struggles with transparent or reflective tubes, we will use bounding boxes for version 1.
- We will use staged images only, with fake labels and no patient information.
- We will require human review and will not present the output as clinically validated.

## Artifact

- [LabRack Vision QA proposal](LabRack_Vision_QA_Proposal.pdf)

[Return to the ITAI 1378 overview](../../)
