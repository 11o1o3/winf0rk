def rgb_color_text(text, r, g, b):
    """
    Formats text with the specified RGB foreground color for terminal output.
    :param text: The text to color.
    :param r: Red component (0-255).
    :param g: Green component (0-255).
    :param b: Blue component (0-255).
    :return: Colored text string.
    """
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def rgb_bg_text(text, r, g, b):
    """
    Formats text with the specified RGB background color for terminal output.
    :param text: The text to color.
    :param r: Red component (0-255).
    :param g: Green component (0-255).
    :param b: Blue component (0-255).
    :return: Colored text string.
    """
    return f"\033[48;2;{r};{g};{b}m{text}\033[0m"


def rgb_text(text, fg_r, fg_g, fg_b, bg_r, bg_g, bg_b):
    """
    Formats text with both foreground and background RGB colors for terminal output.
    :param text: The text to color.
    :param fg_r: Red component for foreground (0-255).
    :param fg_g: Green component for foreground (0-255).
    :param fg_b: Blue component for foreground (0-255).
    :param bg_r: Red component for background (0-255).
    :param bg_g: Green component for background (0-255).
    :param bg_b: Blue component for background (0-255).
    :return: Colored text string.
    """
    return f"\033[38;2;{fg_r};{fg_g};{fg_b}m\033[48;2;{bg_r};{bg_g};{bg_b}m{text}\033[0m"


from PIL import Image


def show_image_in_console(image_path, max_width=80):
    """
    Displays an image in the terminal using ANSI escape codes with colored upper-half blocks.

    :param image_path: Path to the image file.
    :param max_width: Maximum width of the displayed image in terminal characters (default: 80).
    """

    RESET = "\033[0m"  # ANSI escape code to reset colors and formatting

    def rgb_to_ansi_fg(r, g, b):
        """
        Converts RGB values to an ANSI escape code for foreground color.
        :param r: Red component (0-255).
        :param g: Green component (0-255).
        :param b: Blue component (0-255).
        :return: ANSI escape code string for setting foreground color.
        """
        return f"\033[38;2;{r};{g};{b}m"


    def rgb_to_ansi_bg(r, g, b):
        """
        Converts RGB values to an ANSI escape code for background color.
        :param r: Red component (0-255).
        :param g: Green component (0-255).
        :param b: Blue component (0-255).
        :return: ANSI escape code string for setting background color.
        """
        return f"\033[48;2;{r};{g};{b}m"

    img = Image.open(image_path).convert('RGB')

    width, height = img.size
    aspect_ratio = height / width
    new_width = min(max_width, width)
    new_height = int(aspect_ratio * new_width * 0.5)
    img = img.resize((new_width, new_height * 2))

    for y in range(0, img.height, 2):
        line = ""
        for x in range(img.width):
            top = img.getpixel((x, y))
            if y + 1 < img.height:
                bottom = img.getpixel((x, y + 1))
            else:
                bottom = (0, 0, 0)
            fg = rgb_to_ansi_fg(*top)
            bg = rgb_to_ansi_bg(*bottom)
            line += f"{fg}{bg}▀"
        line += RESET
        print(line)
