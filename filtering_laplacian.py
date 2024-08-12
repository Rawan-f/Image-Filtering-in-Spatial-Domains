from google.colab import files
uploaded = files.upload()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to apply padding to the image
def pad_image(image, size):
    padding = size // 2
    padded_image = cv2.copyMakeBorder(image, padding, padding, padding, padding, cv2.BORDER_CONSTANT)
    return padded_image

# Function to implement the filtering operation
def apply_filter(image, kernel):
    # Initialize an output image with zeros
    filtered_image = np.zeros_like(image)
    # Get the size of the kernel
    filter_size = kernel.shape[0]
    # Calculate the padding size
    padding = filter_size // 2
    # Apply padding to the image
    padded_image = pad_image(image, filter_size)

    # Iterate over each pixel location in the padded image
    for i in range(padding, padded_image.shape[0] - padding):
        for j in range(padding, padded_image.shape[1] - padding):
            # Extract the window of the image with the same size as the kernel
            window = padded_image[i-padding:i+padding+1, j-padding:j+padding+1]
            # Perform element-wise multiplication between the window and the kernel, and compute the sum
            filtered_image[i-padding, j-padding] = np.sum(window * kernel)

    return filtered_image

# Read the color image
image = cv2.imread('original image.jpg')

# Convert the color image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the Laplacian filter
laplacian_filter = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]])

# Define the padding size
filter_size = laplacian_filter.shape[0]

# Apply padding to the grayscale image
padded_gray_image = pad_image(gray_image, filter_size)

# Apply the Laplacian filter to the padded grayscale image
filtered_image = apply_filter(gray_image, laplacian_filter)

# Display the original image, grayscale image, Laplacian filter, and filtered image
plt.figure(figsize=(12, 8))

# Original Color Image
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Color Image')
plt.axis('off')

# Grayscale Image
plt.subplot(2, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Laplacian Filter
plt.subplot(2, 3, 4)
plt.imshow(laplacian_filter, cmap='gray', interpolation='none')
plt.title('Laplacian Filter')
plt.axis('off')

# Filtered Image
plt.subplot(2, 3, 5)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.show()