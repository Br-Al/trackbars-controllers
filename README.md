#  Get started with TrackBars as Controllers

This project is part of the OpenCV course Assegnments. The goal is to learn how to 
use mouse and trackbar to resize images with OpenCV.

The project create a GUI application which will let the user resize the input image and save the resized image and the new image size an a .txt file automatically.

Clone the repository `git clone https://github.com/Br-Al/trackbars-controllers.git`

# Usage

`
usage: main.py [-h] [--image IMAGE] [--save_path SAVE_PATH] [--window_name WINDOW_NAME]

options:
  -h, --help            show this help message and exit
  --image IMAGE         Path to the image
  --save_path SAVE_PATH
                        Path to save the scaled image
  --window_name WINDOW_NAME
                        Name of the window to display the image
`
# Install the requirements
Create a virtual env.
`python3 -m venv path/to/your/venv`
Activate the virtual env.
`path/to/your/venv/Scripts/activate.bat` or `source path/to/your/venv/bin/activate` for mac and linux users.

Run `pip install -r requirements.txt` to install all the packages in the requirements.txt file.

# Usage
`python main.py --help`

Run the application
`python main.py`