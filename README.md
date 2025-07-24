# htic
Image Processing Notes

Pixel Basics
      
      A pixel holds intensity values.

      8-bit image: values range from 0–255

      Float image: values typically range from 0–1

Grayscale vs Color
      
      Grayscale: 1 value per pixel

      Color: Usually 3+ values (based on channels)
      
Channels

      Each channel is a 2D matrix (same size as the image)

    RGB → 3 channels: Red, Green, Blue

    RGBA → 4 channels: Red, Green, Blue, Alpha (transparency)

Operations can be done:

Per channel

After combining channels

Colormap (cmap)

    cmap='gray':
    0 → black
    
    255 → white
    
    Values in between → shades of gray
    
    Default colormap ('viridis'):
    0 → dark blue
    
    255 → yellow
    
    In between → green, teal, etc.

Image Filtering
Goals
    
    Noise Reduction – remove unwanted intensity variation
    
    Feature Extraction – highlight edges, corners, textures

Bilateral Filter
    
    Edge-preserving smoothing
    
    Smooths the image while keeping edges sharp
    
    Useful before edge detection

Low-Pass Filter (LPF)

    Effect: Blurs or smooths image
    
    Purpose: Removes high-frequency content (noise, edges)
    
    Kernel: Positive values only
    
    How: Multiply kernel with pixel neighborhood, take the average
    
    Looks like a softened or sandpapered image

High-Pass Filter (HPF)

    Effect: Sharpens, enhances edges
    
    Purpose: Removes low-frequency content (smooth areas)
    
    Kernel: Includes negative values
    
    How: Multiply kernel with pixel neighborhood, subtract, then average
    
    Looks like a pencil sketch or outlined image

Sobel Filter (Type of HPF)

    Gradient-based edge detector
    
    Uses two directions:
    
    X-axis (vertical): left to right
    
    Y-axis (horizontal): top to bottom
    
    Detects intensity change direction
    
    Flipping the kernel changes edge direction
    
    Inverting does nothing (kernel is symmetric)

Gaussian Filter (Type of LPF)

    Weighted averaging using a Gaussian kernel
    
    Smooths image while reducing noise

Resize vs Crop

Resize

    Scales the entire image
    
    Everything is visible, just:
    
    Smaller (blurry)
    
    Or larger (possibly distorted)

Crop

    Cuts out a region of interest
    
    Loses parts of the original image
    
    Resolution stays the same
