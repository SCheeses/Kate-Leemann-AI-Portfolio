"""Extract selected PNG outputs from the portfolio notebooks.

The notebooks remain the source of truth. This utility makes important saved
outputs independently viewable in each project's results directory.
"""

from __future__ import annotations

import base64
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXTRACTIONS = {
    "Computer-Vision-ITAI1378/Projects/01-Image-Processing-Fundamentals/Image_Processing_Fundamentals.ipynb": {
        (15, 0): "results/convolution_filters.png",
        (29, 0): "results/personal_experiments.png",
        (31, 0): "results/processing_summary.png",
    },
    "Computer-Vision-ITAI1378/Projects/02-CIFAR10-SVM-Classifier/CIFAR10_SVM_Classifier.ipynb": {
        (12, 0): "results/original_samples.png",
        (12, 1): "results/grayscale_samples.png",
        (12, 2): "results/flattened_samples.png",
        (13, 0): "results/confusion_matrix.png",
        (13, 1): "results/sample_predictions.png",
    },
    "Computer-Vision-ITAI1378/Projects/03-Chihuahua-Muffin-Neural-Network/Chihuahua_Muffin_Classifier.ipynb": {
        (23, 0): "results/dataset_samples.png",
        (45, 0): "results/validation_predictions.png",
    },
}


def png_outputs(cell: dict) -> list[bytes]:
    images: list[bytes] = []
    for output in cell.get("outputs", []):
        image_data = output.get("data", {}).get("image/png")
        if image_data is None:
            continue
        encoded = "".join(image_data) if isinstance(image_data, list) else image_data
        images.append(base64.b64decode(encoded))
    return images


def main() -> None:
    written = 0
    for notebook_rel, selections in EXTRACTIONS.items():
        notebook_path = ROOT / notebook_rel
        notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
        cache: dict[int, list[bytes]] = {}

        for (cell_index, image_index), output_rel in selections.items():
            if cell_index not in cache:
                cache[cell_index] = png_outputs(notebook["cells"][cell_index])
            images = cache[cell_index]
            if image_index >= len(images):
                raise IndexError(
                    f"{notebook_rel}: cell {cell_index} has no PNG output "
                    f"at index {image_index}"
                )

            output_path = notebook_path.parent / output_rel
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(images[image_index])
            print(f"Wrote {output_path.relative_to(ROOT)}")
            written += 1

    print(f"Extracted {written} result images.")


if __name__ == "__main__":
    main()
