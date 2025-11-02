#!/bin/bash

# Lab 4 - Conda Environment Setup Script

echo "=========================================="
echo "Setting up Conda Environment for Lab 4"
echo "=========================================="

# Environment name
ENV_NAME="cv_lab4"

# Check if conda is installed
if ! command -v conda &> /dev/null
then
    echo "Error: Conda is not installed or not in PATH"
    echo "Please install Anaconda or Miniconda first"
    exit 1
fi

# Check if environment already exists
if conda env list | grep -q "^${ENV_NAME} "; then
    echo "Environment '${ENV_NAME}' already exists."
    read -p "Do you want to remove and recreate it? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Removing existing environment..."
        conda env remove -n ${ENV_NAME} -y
    else
        echo "Skipping environment creation."
        echo "To activate existing environment, run: conda activate ${ENV_NAME}"
        exit 0
    fi
fi

# Create new conda environment
echo ""
echo "Creating new conda environment: ${ENV_NAME}"
conda create -n ${ENV_NAME} python=3.9 -y

# Activate environment
echo ""
echo "Activating environment..."
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate ${ENV_NAME}

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

# Verify installation
echo ""
echo "Verifying installation..."
python -c "import cv2, numpy, sklearn, matplotlib, seaborn, tqdm; print('✓ All packages installed successfully!')"

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "To use the environment:"
echo "  1. Activate: conda activate ${ENV_NAME}"
echo "  2. Run notebook: jupyter notebook lab4.ipynb"
echo "  3. Deactivate when done: conda deactivate"
echo ""
