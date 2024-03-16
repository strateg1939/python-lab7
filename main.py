from app.io.input import get_text_input_from_console, get_text_from_file
from app.io.output import output_text_to_console, output_text_to_file


def main():
    text_console = get_text_input_from_console()
    text_file = get_text_from_file("data/test.txt")
    output_text_to_console(text_file)
    output_text_to_file(text_console, "data/output.txt")


if __name__ == '__main__':
    main()