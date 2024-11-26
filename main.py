from db_manager import create_barcode_entry, read_barcodes, update_barcodes, delete_barcodes
from barcode_manager import generate_barcode

def main_menu():
    # print("\nMain Menu:")
    print("1. Create Barcode")
    print("2. View Barcodes")
    print("3. Update Barcode")
    print("4. Delete Barcode")
    print("5. Exit")
    option = input("Choose an option: ")

    if option == "1":
        product_name = input("Enter product name: ")
        code = input("Enter barcode code: ")
        file_path = generate_barcode(code)
        create_barcode_entry({"product_name": product_name, "code": code, "file_path": file_path})
        print("Barcode created and saved!")

    elif option =="2":
        barcodes = read_barcodes()
        for barcode in barcodes:
            print(barcode)

    elif option == "3":
        code = input("Enter barcode code to update: ")
        new_name = input("Enter new product name: ")
        update_barcodes({"code": code}, {"product_name": new_name})
        print("Barcode updated!")

    elif option == "4":
        code = input("Enter barcode code to delete: ")
        delete_barcodes({"code": code})
        print("Barcode deleted!")

    elif option == "5":
        print("Exiting...")
        exit()

    else:
        print("Invalid choice")

if __name__ == "__main__":
    while True:
        main_menu()
