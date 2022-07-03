# Histogram Equalization
In this Github repo the methods of Histogram Equalization and Adaptive Histogram Equalization have been compared for improving the contrast of input images.

# Algorithms
### Histogram Equalization
1. Convert input image to grayscale and flatten image into 1D array
2. Get the count of per pixel value using user defined histogram function
3. Get the cumulative sum at each stage
4. Normalize each cumulative sum and round it off to nearest integer

### Adaptive Histogram Equalization
1. Convert input image to grayscale
2. Separate the image into n number of tiles 
3. Repeat all steps mentioned above in the histogram equalization algorithm for each tile 
4. Piece all the tiles back together
