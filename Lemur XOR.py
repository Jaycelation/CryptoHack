from PIL import Image
import numpy as np

image1 = Image.open("flag.png")
image2 = Image.open("lemur.png")

arr1 = np.array(image1)
arr2 = np.array(image2)

if arr1.shape != arr2.shape:
    raise ValueError("Hai ảnh phải có cùng kích thước để thực hiện phép XOR.")

result_arr = np.bitwise_xor(arr1, arr2)
result_image = Image.fromarray(result_arr)
result_image.save("result.png")
result_image.show()