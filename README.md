# Image Filtering in Spatial Domains

## Overview

This project demonstrates image filtering techniques using spatial domain methods with Python. The code applies two types of filters to grayscale images: a Gaussian filter for smoothing and a Laplacian filter for edge detection. The project is designed to help understand the basic principles of image filtering and convolution in the spatial domain.

## Project Structure

- `filtering_gaussian.py`: Contains code to apply a Gaussian filter to an image.
- `filtering_laplacian.py`: Contains code to apply a Laplacian filter to an image.
- `original_image.jpg`: Sample image used for filtering.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib

You can install the required packages using pip:

```bash
pip install opencv-python-headless numpy matplotlib
```

## Usage

### 1. Gaussian Filtering

The Gaussian filter is used for smoothing images and reducing noise. The code for applying the Gaussian filter is found in `filtering_gaussian.py`. 

**How to Run:**

1. Ensure `original_image.jpg` is in the same directory as the script.
2. Run the script using Python:

    ```bash
    python filtering_gaussian.py
    ```

**What the Code Does:**

- Reads the color image and converts it to grayscale.
- Defines a 5x5 Gaussian filter with a specified sigma value.
- Applies padding to the grayscale image.
- Filters the image using the Gaussian filter.
- Displays the original image, grayscale image, Gaussian filter, and filtered image.

### 2. Laplacian Filtering

The Laplacian filter is used for edge detection by highlighting areas of rapid intensity change. The code for applying the Laplacian filter is found in `filtering_laplacian.py`.

**How to Run:**

1. Ensure `original_image.jpg` is in the same directory as the script.
2. Run the script using Python:

    ```bash
    python filtering_laplacian.py
    ```

**What the Code Does:**

- Reads the color image and converts it to grayscale.
- Defines a Laplacian filter.
- Applies padding to the grayscale image.
- Filters the image using the Laplacian filter.
- Displays the original image, grayscale image, Laplacian filter, and filtered image.

## Code Details

### `pad_image(image, size)`

Applies padding to an image to handle border effects during convolution.

**Parameters:**
- `image`: The input image to be padded.
- `size`: The size of the kernel used for filtering.

**Returns:**
- Padded image.

### `apply_filter(image, kernel)`

Applies a specified filter kernel to the image using convolution.

**Parameters:**
- `image`: The grayscale image to be filtered.
- `kernel`: The filter kernel (e.g., Gaussian or Laplacian).

**Returns:**
- Filtered image.
