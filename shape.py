import cv2
import os

def apply_morphological_operations(image_path, output_folder,threshold_value):
    # 读取图片
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 定义形态学操作的核
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    
    

    _, img = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
    img = 255 - img
    cv2.imwrite(os.path.join(output_folder, 'origion.jpg'), img)

    # 腐蚀
    erosion = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite(os.path.join(output_folder, 'erosion.jpg'), erosion)

    # 膨胀
    dilation = cv2.dilate(img, kernel, iterations=1)
    cv2.imwrite(os.path.join(output_folder, 'dilation.jpg'), dilation)

    # 开运算
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imwrite(os.path.join(output_folder, 'opening.jpg'), opening)

    # 闭运算
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(os.path.join(output_folder, 'closing.jpg'), closing)

def process_images_in_folder(input_folder, output_folder,threshold_value):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 处理文件夹下的所有图片
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            apply_morphological_operations(image_path, output_folder,threshold_value)

if __name__ == "__main__":
    input_folder = "F:\Desktop\image"
    output_folder = "F:\Desktop\image1"
    threshold_value = 153
    process_images_in_folder(input_folder, output_folder,threshold_value)
