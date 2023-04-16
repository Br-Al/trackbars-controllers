import cv2
import argparse
from functools import partial
from trackbar_controller import scale_change, scale_type_change, save_image


def main():
    # Create arguments parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, default='data/images/ai.png', help='Path to the image')
    parser.add_argument('--save_path', type=str, default='data/images/scaled_images/', help='Path to save the scaled image')
    parser.add_argument('--window_name', type=str, default='Resize Image', help='Name of the window to display the image')

    # Parse the arguments
    args = parser.parse_args()
    max_scale = 100
    scale_factor = 1
    scale_type = 0
    max_scale_type = 1
    trackbar_value = 'Scale'
    trackbar_type = 'Type: \n 0: Scale Up \n 1: Scale Down'

    # Load an image
    try:
        img = cv2.imread(args.image, cv2.IMREAD_COLOR)
    except FileNotFoundError as e:
        print('File not found ', e)
        exit()

    # Create a window to display results
    cv2.namedWindow(args.window_name, cv2.WINDOW_AUTOSIZE)

    # Create Trackbar to choose type of scaling
    cv2.createTrackbar(trackbar_type, args.window_name, scale_type, max_scale_type, partial(scale_type_change, img, args.window_name))

    # Create Trackbar to choose scaling factor
    cv2.createTrackbar(trackbar_value, args.window_name, scale_factor, max_scale, partial(scale_change, img, args.window_name))

    # Create a save image mouse callback
    userdata = {'save_path': args.save_path, 'image_name': args.image.split('/')[-1]}
    cv2.setMouseCallback(args.window_name, save_image, userdata)

    cv2.imshow(args.window_name, img)

    while True:
        c = cv2.waitKey(20)
        if c == 27:
            break
    
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()