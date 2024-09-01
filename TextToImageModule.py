"""
TextToImageModule.py

This module provides functionality to convert text strings into images using binary encoding.
Each character in the text is converted into its binary representation, which is then used
to create an image. The image size and colors are customizable.

Classes:
- TextToImage: A class that encapsulates the text-to-image conversion logic, including
               methods for converting text to binary, generating images from binary data,
               and saving the images to a specified directory.

Dependencies:
- PIL (Pillow): Used for creating and manipulating images.
- pathlib: Used for handling file paths in a platform-independent way.
- os: Used for interacting with the operating system, such as creating directories.

:)
"""

import PIL.Image
from pathlib import Path
import os

class TextToImage:
    """
    The TextToImage class provides functionality to convert text into an image
    by encoding the text as binary data and mapping this data to pixel colors in an image.

    Methods:
        - create_image(binary_string, image_name, stop_event=False):
            Generates an image from a binary string and saves it with the given name.
            Optionally stops the process if stop_event is set to True.
        - image_datas(binary_string, imageIndex):
            Generates the binary data slice and image name for the specified image index.
        - text_to_binary(text):
            Converts a given text string into its binary representation.
    """

    def __init__(self, IMAGE_SIZE=(1920, 1080), SAVE_DIR=(Path.home() / "Downloads/Encrypted_images_folder"),
                 FIRST_COLOR=(255, 0, 0), SECOND_COLOR=(0, 255, 0), THIRD_COLOR=(0, 0, 255)):
        self.SAVE_DIR = SAVE_DIR
        self.IMAGE_SIZE = IMAGE_SIZE
        self.MAX_SIZE = (self.IMAGE_SIZE[0] * self.IMAGE_SIZE[1]) * 2
        self.FIRST_COLOR = FIRST_COLOR
        self.SECOND_COLOR = SECOND_COLOR
        self.THIRD_COLOR = THIRD_COLOR

    def create_image(self, binary_string, image_name, stop_event=False):
        """
           Creates an image from a binary string and saves it with the specified name.
           Each 2-bit string of the binary string corresponds to one pixel of the image.

           :param binary_string: (str) A binary string representing the image data, where
         			             "" indicates the black color (0,0,0) if the length of the binary_string is insufficient to fill the image,
                                 "00" indicates the white color (255, 255, 255), "01" indicates FIRST_COLOR,
                                 "10" indicates SECOND_COLOR, "11" indicates THIRD_COLOR.

           :param image_name: (str) The name of the image to save.
           :param stop_event: (bool, optional) If True, the image generation process stops.
                              Default value is False.

           :global IMAGE_SIZE: (tuple) Size of the image (width, height).
           :global FIRST_COLOR: (tuple) The RGB value corresponding to the "01" bits.
           :global SECOND_COLOR: (tuple) The RGB value corresponding to the "10" bits.
           :global THIRD_COLOR: (tuple) The RGB value corresponding to bit '11'.
           """
        if stop_event:
            return
        else:
            image = PIL.Image.new("RGB", self.IMAGE_SIZE)
            pixels = image.load()

            index = 0
            bit = 0
            for y in range(self.IMAGE_SIZE[1]):
                for x in range(self.IMAGE_SIZE[0]):
                    if binary_string[bit:bit + 2] == "00":
                        pixels[x, y] = (255, 255, 255)
                    elif binary_string[bit:bit + 2] == "01":
                        pixels[x, y] = self.FIRST_COLOR
                    elif binary_string[bit:bit + 2] == "10":
                        pixels[x, y] = self.SECOND_COLOR
                    elif binary_string[bit:bit + 2] == "11":
                        pixels[x, y] = self.THIRD_COLOR
                    else:
                        pass

                    bit += 2
                    index += 1
                    if index >= len(binary_string):
                        break
                if index >= len(binary_string):
                    break

            if not os.path.exists(self.SAVE_DIR):
                os.makedirs(self.SAVE_DIR)
            image.save(f"{self.SAVE_DIR}\\{image_name}.png")

    def image_datas(self, binary_string, imageIndex):
        """
          Generates the data for an image based on the binary string and the current image index.

          This function slices a portion of the binary string based on the image index and prepares the
          corresponding image name.

          :param binary_string: (str) The full binary string representing the data for all images.
          :param imageIndex: (int) The index of the current image being processed, typically
                                    used in a loop.

          :global IMAGE_SIZE: (tuple) The size of the image in pixels (width, height).
          :global MAX_SIZE: (int) The maximum number of bits that can be used per image.
                           Calculated as MAX_SIZE = IMAGE_SIZE[0] * IMAGE_SIZE[1] * 2, where 2 represents
                           the number of bits per pixel.

          :return:
              - forward_binary (str): A slice of the binary string corresponding to the current image,
                                      containing a maximum of MAX_SIZE bits.
              - image_name (str): The name of the image file, formatted as
                                  "encrypted_image_{width}x{height}_(index)".

          :example:
          :>>> import math
          :>>> imageNum = math.ceil(len(binary_string) / MAX_SIZE)
          :>>> for i in range(imageNum):
          :>>>     forward_binary, image_name = image_datas(binary_string, i)
        """

        image_name = f"encrypted_image_{self.IMAGE_SIZE[0]}x{self.IMAGE_SIZE[1]}_({imageIndex})"
        forward_binary = binary_string[
                         imageIndex * self.MAX_SIZE:(imageIndex * self.MAX_SIZE) + self.MAX_SIZE]
        return forward_binary, image_name

    def text_to_binary(self, text):
        """
         Converts a given text string into its binary representation.

        :param text: (str) The text string to be converted to binary code.

        :return:
            - binary_string (str): The binary representation of the input text,
                               where each character is represented by 8 bits.
        """
        binary_string = "".join(format(ord(x), "08b") for x in text)
        return binary_string
