#!/usr/bin/env python
# coding: utf-8

# In[3]:


from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load and display the original image
image_path = r"C:\Users\DELL\OneDrive\Desktop\GATE\nature.jpg"
image = Image.open(image_path)
if image.mode != 'RGB':
    image = image.convert('RGB')
    
print("Original image loaded successfully.")
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')
plt.show()

# Encryption function
def encrypt_image(image, key):
    print("Encrypting the image...")
    encrypted_image = image.copy()
    pixels = encrypted_image.load()
    
    for i in range(encrypted_image.size[0]):  # width
        for j in range(encrypted_image.size[1]):  # height
            r, g, b = pixels[i, j]
            encrypted_pixel = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
            pixels[i, j] = encrypted_pixel
            if i == 0 and j == 0:  # Print the first pixel's transformation for debugging
                print(f"Original Pixel: {(r, g, b)}, Encrypted Pixel: {encrypted_pixel}")
    
    print("Image encrypted.")
    return encrypted_image

# Decryption function
def decrypt_image(encrypted_image, key):
    print("Decrypting the image...")
    decrypted_image = encrypted_image.copy()
    pixels = decrypted_image.load()
    
    for i in range(decrypted_image.size[0]):  # width
        for j in range(decrypted_image.size[1]):  # height
            r, g, b = pixels[i, j]
            decrypted_pixel = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
            pixels[i, j] = decrypted_pixel
            if i == 0 and j == 0:  # Print the first pixel's transformation for debugging
                print(f"Encrypted Pixel: {(r, g, b)}, Decrypted Pixel: {decrypted_pixel}")
    
    print("Image decrypted.")
    return decrypted_image

# Pixel swapping function
def swap_pixels(image, key):
    print("Swapping pixels...")
    width, height = image.size
    pixels = np.array(image)
    print(f"Image dimensions: {width}x{height}")
    print(f"Pixel array shape: {pixels.shape}")
    
    indices = np.arange(width * height)
    np.random.seed(key)
    np.random.shuffle(indices)
    
    shuffled_pixels = np.zeros_like(pixels)
    
    for idx, new_idx in enumerate(indices):
        x, y = divmod(new_idx, width)
        if x >= width or y >= height:
            print(f"Skipping index out of bounds: x={x}, y={y}")
            continue
        print(f"Swapping pixel at ({idx // width}, {idx % width}) to ({y}, {x})")
        shuffled_pixels[y, x] = pixels[idx // width, idx % width]
    
    print("Pixels swapped.")
    return Image.fromarray(shuffled_pixels)

# Pixel unswapping function
def unswap_pixels(shuffled_image, key):
    print("Unswapping pixels...")
    width, height = shuffled_image.size
    shuffled_pixels = np.array(shuffled_image)
    
    indices = np.arange(width * height)
    np.random.seed(key)
    np.random.shuffle(indices)
    
    unshuffled_pixels = np.zeros_like(shuffled_pixels)
    
    for idx, new_idx in enumerate(indices):
        x, y = divmod(new_idx, width)
        if x >= width or y >= height:
            print(f"Skipping index out of bounds: x={x}, y={y}")
            continue
        print(f"Unswapping pixel from ({y}, {x}) to ({idx // width}, {idx % width})")
        unshuffled_pixels[idx // width, idx % width] = shuffled_pixels[y, x]
    
    print("Pixels unswapped.")
    return Image.fromarray(unshuffled_pixels)

# Define the encryption key
key = 34

# Encrypt the image
encrypted_image = encrypt_image(image, key)
plt.imshow(encrypted_image)
plt.title('Encrypted Image')
plt.axis('off')
plt.show()

# Swap the pixels
swapped_image = swap_pixels(encrypted_image, key)
plt.imshow(swapped_image)
plt.title('Encrypted & Swapped Image')
plt.axis('off')
plt.show()

# Unswap the pixels
unswapped_image = unswap_pixels(swapped_image, key)
plt.imshow(unswapped_image)
plt.title('Unswapped Image')
plt.axis('off')
plt.show()

# Decrypt the image
decrypted_image = decrypt_image(unswapped_image, key)
plt.imshow(decrypted_image)
plt.title('Decrypted Image')
plt.axis('off')
plt.show()

