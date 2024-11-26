# Handles barcode generation
import barcode
from barcode.writer import ImageWriter
import os

def generate_barcode(code, save_path = "barcodes/", barcode_type = "code128"):
    """
    Generates a barcode image and saves it to the specified path.

    Args:
        code (str): The data to encode in the barcode.
        save_path (str): The path to save the barcode image. 

    Returns:
        str: The full path to the saved barcode image.
    """

    try:
        # to validate the input code
        if not code or not code.isdigit():
            raise ValueError("Invalid barcode data. Only number strings are allowed")
        
        # Ensure the save directrory exists
        os.makedirs(save_path, exist_ok = True)

        # to generate the barcode
        barcode_class = barcode.get_barcode_class("code128")
        barcode_instance = barcode_class(code, writer = ImageWriter())
        file_path = os.path.join(save_path, f"{code}.png")
        barcode_instance.save(file_path)
        return file_path

    except ValueError as ve:
        print(f"Barcode error: {ve}")
        return None

    except OSError as os_error:
        print(f"System error: Unable to create or access the directory. {os_error}")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    
if __name__ == "__main__":
    try:
        code = "12345678"
        save_path = "my_barcodes"
        file_path = generate_barcode(code, save_path)

        if file_path:
            print(f"Barcode successfully generated and saved to: {file_path}")
        else:
            print("Failed to generate barcode image.")
    except KeyboardInterrupt:
        print("\nOperation interrupted by user. Exiting.")

    try:
        code = "13976537484746"
        save_path = "my_barcodes"
        file_path = generate_barcode(code, save_path)

        if file_path:
            print(f"Barcode successfully generated and saved to: {file_path}")
        else:
            print("Failed to generate barcode image.")
    except KeyboardInterrupt:
        print("\nOperation interrupted by user. Exiting.")

