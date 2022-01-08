# Swap-Image-Colors
A python script with interface to change colors of an image

<img src="https://user-images.githubusercontent.com/60852205/148651631-0d8d850f-f98f-43b3-93ae-2a041a7e273a.png" width=200><img src="https://user-images.githubusercontent.com/60852205/148651452-ec15703f-5487-4907-8caf-5712bfbbf36b.png" width=200><img src="https://user-images.githubusercontent.com/60852205/148651453-7284343f-fd6a-41b6-be45-150c8931cede.png" width=200><img src="https://user-images.githubusercontent.com/60852205/148651455-0674ff23-b492-4e22-b758-a042a5b5fb69.png" width=200>


## Requirements

Python 3+, PySimpleGUI and drawerFunctions, a collection of PIL and Numpy functions to manipulate images, you can find it [here](https://github.com/DeusAres/drawerFunctions)

## Usage

Start the script with **swapColors.pyw**

Files should be named this way: imgName_hexcode_(as many hexcode you need).extension
imgName is an identifier of the image and hexcode without # represent the color that you want to replace

![image](https://user-images.githubusercontent.com/60852205/148649791-7bc5a34b-08a9-4a19-9b07-a35944ef4c8a.png)![image](https://user-images.githubusercontent.com/60852205/148649836-27de489f-1afe-475d-a75e-bf1c4c4947d4.png)![image](https://user-images.githubusercontent.com/60852205/148649846-31b2c2b9-8462-4ff1-98ae-1e0a84d8963c.png)

## Colors

This field supports inputs with or without # as a string, even in a pythonic list
Examples: ffffff, 000000 | #ffffff, 000000 | ['ffffff', '000000'] | ['#ffffff', '#000000']

The input field of Colors will become, in order, the swapping colors of the image
The first hexcode of your file will be replaced with the first in the Colors inputs, and so on

![image](https://user-images.githubusercontent.com/60852205/148649742-bde364b3-b831-4b00-9d31-36c14ce381b9.png)

You can also activate the Randomize checkbox to unlock another way of replacing colors
![image](https://user-images.githubusercontent.com/60852205/148651205-80bef479-0971-4799-b977-eeae656940f5.png)

Every time New colors is pressed, a new set of colors is generated with a visual palette.
The Shake button instead, will shuffle the order of the palette

Background is purely for PNGs images with transparency in it
If no Background is needed type None, or if you need it you can place a color

## Starting and Saving

Once done preparations the Start button generates a new image, and show a preview of it.
If satisfied of the result, you can press Save. The new image will be saved in the same folder where you started the script with this formula:
imgName_newHexcode_newHexcode...(you get it).png

With the checkbox **☐ Open at end**, explorer will open with your new image selected.

## Future improvements (Maybe)

The current way to generate colors is purely randomic but in the visual world even colors follow rules
One day I'll implement a way to generate colors based on rules (Complementary, Triadic, Analogous, Monochromatic)

Possibly resolve bugs and handle incorrect inputs (99% sure if you try to swap a color that's not in the image will crash)





