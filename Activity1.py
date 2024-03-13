import cv2
import numpy as np
from matplotlib import pyplot as plt

def display_with_wait(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def display_multiple_images(images, titles):
    for i, (image, title) in enumerate(zip(images, titles), start=1):
        plt.subplot(2, 2, i)
        plt.imshow(image, cmap='gray' if len(image.shape) == 2 else None)
        plt.title(title)
    plt.show()

# Activity 1: Open Image and display its properties
def activity_1(image_path):
    img = cv2.imread(image_path)

    # Display the image using different flags
    display_with_wait('Original', img)

    # Convert image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    display_with_wait('Grayscale', gray_img)

    # Get the image value of a pixel
    pixel_value = img[100, 100]
    print("Pixel value at (100, 100):", pixel_value)

    # Convert the image to black and white
    ret, bw_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
    display_with_wait('Black and White', bw_img)

# Activity 2: Use any image
def activity_2(image_path):
    img = cv2.imread(image_path)

    # Get the size of the image
    height, width, channels = img.shape
    print("Image size:", width, "x", height)

    # Get the value of a pixel in the image (R,G,B)
    b, g, r = img[100, 100]
    print("RGB value at (100, 100):", (r, g, b))

    # Show the 4 different edges of an image
    edges1 = cv2.Canny(img, 100, 200)
    edges2 = cv2.Canny(img, 50, 150)
    edges3 = cv2.Canny(img, 150, 250)
    edges4 = cv2.Canny(img, 200, 300)

    # Show the RGB colors of the same image separately
    b, g, r = cv2.split(img)
    display_multiple_images([b, g, r], ['Blue', 'Green', 'Red'])

# Activity 3: Image Histogram
def activity_3(image_path):
    img = cv2.imread(image_path)

    plt.figure()
    plt.subplot(2, 2, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(2, 2, 2), plt.hist(img.ravel(), 256, [0, 256]), plt.title('Histogram')

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.subplot(2, 2, 3), plt.imshow(cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)), plt.title('Grayscale Image')
    plt.subplot(2, 2, 4), plt.hist(gray_img.ravel(), 256, [0, 256]), plt.title('Histogram')
    plt.show()

# Activity 4: Image Properties
def activity_4(image_path):
    img = cv2.imread(image_path)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_img, 100, 200)

    plt.figure()
    plt.subplot(2, 2, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(2, 2, 2), plt.imshow(gray_img, cmap='gray'), plt.title('Grayscale Image')
    plt.subplot(2, 2, 3), plt.hist(gray_img.ravel(), 256, [0, 256]), plt.title('Histogram')
    plt.subplot(2, 2, 4), plt.imshow(edges, cmap='gray'), plt.title('Edges')
    plt.show()

# Activity 5:
def activity_5(image_path):
    img = cv2.imread(image_path)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_img, 100, 200)

    plt.figure()
    plt.subplot(2, 2, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(2, 2, 2), plt.imshow(edges, cmap='gray'), plt.title('Edges')
    plt.subplot(2, 2, 3), plt.imshow(gray_img, cmap='gray'), plt.title('Grayscale Image')
    plt.subplot(2, 2, 4), plt.hist(gray_img.ravel(), 256, [0, 256]), plt.title('Histogram')
    plt.show()

# Load image path
image_path = r"C:\Users\admin\Pictures\Saved Pictures\lisusu.jpg"

# Display menu
print("Menu:")
print("1. Activity 1")
print("2. Activity 2")
print("3. Activity 3")
print("4. Activity 4")
print("5. Activity 5")

# Prompt user for activity choice
activity_choice = input("Choose activity (1-5): ")

# Perform chosen activity
if activity_choice == '1':
    activity_1(image_path)
elif activity_choice == '2':
    activity_2(image_path)
elif activity_choice == '3':
    activity_3(image_path)
elif activity_choice == '4':
    activity_4(image_path)
elif activity_choice == '5':
    activity_5(image_path)
else:
    print("Invalid choice. Please choose a number between 1 and 5.")
