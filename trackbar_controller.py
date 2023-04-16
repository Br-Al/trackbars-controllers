import cv2
import os

def save_image(event, x, y, flags, userdata):
    save_path = userdata['save_path']
    image_name = userdata['image_name']
    # check if the save path exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    if event == cv2.EVENT_LBUTTONDOWN:
        # get the image name
        file_name = image_name.split('.')[0]
        extension = image_name.split('.')[1]
        image_name = f'{file_name}{scaled_img.shape[0]}x{scaled_img.shape[1]}.{extension}'

        # Save the image
        cv2.imwrite(os.path.join(save_path, image_name), scaled_img)

        # Create a .csv file to save the image name, and the new image size
        with open(os.path.join(save_path, 'image_info.txt'), 'a') as f:
            f.write(f'{image_name},{scaled_img.shape[0]},{scaled_img.shape[1]} \n')

def scale_type_change(img, window_name, *args):
    global scale_type
    global scale_factor
    global scaled_img
    scale_type = args[0]

    scale_factor = 1 + args[0]/100.0 if scale_type == 1 else 1/(1 + args[0]/100.0)
    # if scale_factor is 0, set it to 1
    if scale_factor == 0: scale_factor = 1

    # Resize the image
    scaled_img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

    # Display the image
    cv2.imshow(window_name, scaled_img)

def scale_change(img, window_name, *args):
    global scale_factor
    global scale_type
    global scaled_img

    # get the scale factor from the trackbar
    scale_type = cv2.getTrackbarPos('Type: \n 0: Scale Up \n 1: Scale Down', 'Resize Image')
    
    scale_factor = 1 + args[0]/100.0 if scale_type == 1 else 1/(1 + args[0]/100.0)

    # if scale_factor is 0, set it to 1
    if scale_factor == 0: scale_factor = 1
    
    # Resize the image
    scaled_img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

    # Display the image
    cv2.imshow(window_name, scaled_img)