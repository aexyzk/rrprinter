from PIL import Image
import pyautogui
import time

pyautogui.FAILSAFE = False

start_length = 660
start_height = 240
pixel_size = 4

times_before_save = 20
cur_times_before_save = 0

save_to_start = 50
cur_save = 0

last_hex = ''
unique_colors = {}

def print_pixel(_hex_color, _x, _y):
    global last_hex
    global cur_times_before_save
    global cur_save

    adjusted_x = (_x * pixel_size) + start_length + 1
    adjusted_y = (_y * pixel_size) + start_height + 1

    if last_hex != _hex_color:
        # change hex code (custom; input box; ctrl+a; type in hex code; done)
        time.sleep(.25)
        pyautogui.rightClick()
        time.sleep(3.5)
        pyautogui.click(1317, 848)
        time.sleep(.5)
        pyautogui.click(1352, 654)
        time.sleep(.5)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.5)
        pyautogui.typewrite(_hex_color)
        time.sleep(.5)
        pyautogui.click(1323, 754)
        time.sleep(.5)
        last_hex = _hex_color;
        cur_times_before_save = cur_times_before_save + 1;
       
    if cur_times_before_save > times_before_save:
        print("please save! then click enter when you are ready to continue. (again you will has a second to go back to rec room)")
        input()
        cur_times_before_save = 0
        time.sleep(1);

    # click the correct spot (click (_x, _y))
    pyautogui.click(adjusted_x, adjusted_y)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

def main():
    print("\n** make sure rr is full screen on a 1920x1080 monitor **")
    print("make sure you are focused on the canvas")
    print("once you click enter key you will have 1 second to get back to rec room then it will start printing")
    input()

    time.sleep(1)

    im = Image.open('img.png', 'r')
    width, height = im.size

    if im.mode != 'RGB':
        im = im.convert('RGB')

    for y in range(height):
        for x in range(width):
            r, g, b = im.getpixel((x, y))
            hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
            if hex_code not in unique_colors:
                unique_colors[hex_code] = []
            unique_colors[hex_code].append((x, y))

    for hex_code, pixel_list in unique_colors.items():
        for pixel in pixel_list:
            print_pixel(hex_code, pixel[0], pixel[1])

if __name__ == "__main__":
    main()
