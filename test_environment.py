#!/usr/bin/env python3
"""
Test script to verify all dependencies are installed correctly
for Lab 4: Bag of Visual Words
"""

import sys

def test_imports():
    """Test all required package imports"""
    print("Testing package imports...")
    print("-" * 50)
    
    packages = {
        'numpy': 'numpy',
        'opencv-python': 'cv2',
        'scikit-learn': 'sklearn',
        'matplotlib': 'matplotlib',
        'seaborn': 'seaborn',
        'tqdm': 'tqdm',
        'jupyter': 'jupyter',
    }
    
    failed = []
    
    for package_name, import_name in packages.items():
        try:
            module = __import__(import_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"✓ {package_name:20s} (version: {version})")
        except ImportError as e:
            print(f"✗ {package_name:20s} - FAILED")
            failed.append(package_name)
    
    print("-" * 50)
    
    if failed:
        print(f"\n❌ Failed to import: {', '.join(failed)}")
        print("Run: pip install -r requirements.txt")
        return False
    else:
        print("\n✓ All packages imported successfully!")
        return True

def test_opencv_sift():
    """Test if SIFT is available in OpenCV"""
    print("\nTesting OpenCV SIFT...")
    print("-" * 50)
    
    try:
        import cv2
        sift = cv2.SIFT_create()
        print("✓ SIFT is available")
        print(f"  OpenCV version: {cv2.__version__}")
        return True
    except Exception as e:
        print(f"✗ SIFT not available: {e}")
        print("  Install: pip install opencv-contrib-python")
        return False

def test_dataset():
    """Check if dataset directory exists"""
    import os
    
    print("\nChecking dataset...")
    print("-" * 50)
    
    dataset_path = "./Images"
    
    if not os.path.exists(dataset_path):
        print(f"✗ Dataset directory not found: {dataset_path}")
        print("  Please ensure UC Merced dataset is in ./Images/")
        return False
    
    classes = [d for d in os.listdir(dataset_path) 
               if os.path.isdir(os.path.join(dataset_path, d))]
    
    if len(classes) == 0:
        print(f"✗ No class directories found in {dataset_path}")
        return False
    
    print(f"✓ Dataset found: {len(classes)} classes")
    print(f"  Path: {os.path.abspath(dataset_path)}")
    return True

def main():
    """Run all tests"""
    print("=" * 50)
    print("Lab 4 - Environment Test")
    print("=" * 50)
    
    results = []
    
    # Test imports
    results.append(test_imports())
    
    # Test OpenCV SIFT
    results.append(test_opencv_sift())
    
    # Test dataset
    results.append(test_dataset())
    
    # Summary
    print("\n" + "=" * 50)
    if all(results):
        print("✓ All tests passed! Environment is ready.")
        print("=" * 50)
        print("\nTo start the lab:")
        print("  jupyter notebook lab4.ipynb")
        return 0
    else:
        print("✗ Some tests failed. Please fix the issues above.")
        print("=" * 50)
        return 1

if __name__ == "__main__":
    sys.exit(main())
