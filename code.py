import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ishaa\OneDrive\Desktop\OCR\Tesseract-OCR\tesseract"


images_array = []


num_images = int(input("Enter number of images: "))
for i in range (num_images):
    images_array.append(str(input("Enter image full path: ")))


for i in range (len(images_array)):
    img = cv2.imread(images_array[i])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dta = pytesseract.image_to_string(img, config = "--psm 6 --oem 3 -c tessedit_char_unblacklist=0123456789")
    dta_array = dta.split('\n')
    for j in range (len(dta_array)):
        #print("Line ", j+1)
        print(dta_array[j])
