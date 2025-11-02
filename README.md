# Lab 4: Bag of Visual Words (BoVW) for Image Classification

## Overview
Implementation of Bag of Visual Words technique for image classification using the UC Merced Land Use Dataset.

## Requirements
- Python 3.8 or higher
- Conda (recommended) or pip

## Setup Instructions

### Option 1: Using Conda (Recommended)

1. **Create a new conda environment:**
```bash
conda create -n cv_lab4 python=3.9
```

2. **Activate the environment:**
```bash
conda activate cv_lab4
```

3. **Install dependencies:**
```bash
# Install conda packages
conda install -c conda-forge numpy opencv scikit-learn matplotlib seaborn tqdm jupyter notebook

# Or use pip within conda environment
pip install -r requirements.txt
```

### Option 2: Using pip only

```bash
pip install -r requirements.txt
```

## Running the Lab

1. **Ensure dataset is in place:**
   - Dataset should be in `./Images/` directory
   - Structure: `./Images/[class_name]/[image_files].tif`

2. **Start Jupyter Notebook:**
```bash
jupyter notebook
```

3. **Open and run `lab4.ipynb`:**
   - Open `lab4.ipynb` in the browser
   - Run cells sequentially (Shift+Enter or Cell > Run All)

## Quick Test Commands

### Test with Conda Environment
```bash
# Create and activate environment
conda create -n cv_lab4 python=3.9 -y
conda activate cv_lab4

# Install dependencies
pip install -r requirements.txt

# Run notebook (non-interactive)
jupyter nbconvert --to notebook --execute lab4.ipynb --output lab4_executed.ipynb

# Or start interactive session
jupyter notebook lab4.ipynb
```

### Test Installation
```bash
# Activate environment
conda activate cv_lab4

# Test imports
python -c "import cv2, numpy, sklearn, matplotlib, seaborn, tqdm; print('All packages imported successfully!')"
```

## Project Structure
```
cv_lab4/
├── Images/              # Dataset directory (UC Merced)
│   ├── agricultural/
│   ├── airplane/
│   └── ...
├── lab4.ipynb          # Main implementation notebook
├── notebook.ipynb      # Reference notebook
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Pipeline Steps
1. Data Loading and Preprocessing
2. Dataset Splitting (80/20)
3. SIFT Feature Extraction
4. Visual Vocabulary Building (K-means)
5. Quantization and Histogram Creation
6. Normalization (L1/L2)
7. SVM Classifier Training
8. Prediction and Evaluation
9. Confusion Matrix Visualization

## Key Parameters
- **K (Visual Words)**: 100 (configurable in notebook)
- **Normalization**: L2 (changeable to L1)
- **Classifier**: SVM with RBF kernel
- **Train/Test Split**: 80/20

## Expected Results
- Classification accuracy: ~70-85% (depends on K and parameters)
- Confusion matrix showing per-class performance
- Detailed classification report

## Troubleshooting

### OpenCV SIFT not found
If you get an error about SIFT not being available:
```bash
pip install opencv-contrib-python
```

### Memory Issues
If running out of memory during K-means:
- Reduce K value (e.g., K=50)
- Use smaller image size in preprocessing
- Limit SIFT descriptors for clustering

## Author
ESI Sidi Bel Abbes - Computer Vision Lab 4
