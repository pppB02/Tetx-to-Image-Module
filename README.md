# TextToImage Module
## Overview
The TextToImage module allows you to convert text strings into images by encoding the text as binary data and mapping this data to pixel colors in an image.
This can be useful for steganography, data visualization, or creative projects where text needs to be represented visually in a unique way.

## Features
- Convert Text to Binary: Convert any text string into its binary representation.
- Generate Images: Create images from the binary data, where each pixel color corresponds to a specific binary value.
- Customizable Image Sizes and Colors: The image size and colors used to represent the binary values can be customized.
  
## Requirements
You can install the required dependencies using pip:
```
pip install Pillow
```
## Usage
### Example
Here's a basic example of how to use the TextToImage class to convert a text string into an image.
```
from TextToImageModule import TextToImage

# Initialize the converter
converter = TextToImage()

# Convert text to binary
binary_string = converter.text_to_binary("Hello, World!")

# Generate the image data
image_data, image_name = converter.image_datas(binary_string, 0)

# Create and save the image
converter.create_image(image_data, image_name)
```
This will generate an image named encrypted_image_<width>x<height>_(0).png in the specified directory.

## Customization
You can customize the following parameters in the TextToImage class:
- IMAGE_SIZE: Set the size of the image in pixels, e.g., (width, height).
- FIRST_COLOR, SECOND_COLOR, THIRD_COLOR: Define the RGB color values associated with specific binary codes (e.g., 01, 10, 11).
- 
## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure that your code follows the existing style and includes appropriate tests.

## License
Not interested. Use it wherever you want

## Contact
For questions, issues, or suggestions, feel free to open an issue on GitHub or contact the project maintainer.
