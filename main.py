import tkinter as tk
from PIL import ImageTk
import qrcode
import os
import appdirs

def generate_qr_code():
    input_data = input_entry.get()
    
    # generate qr.code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(input_data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # convert to imageTK
    tk_image = ImageTk.PhotoImage(qr_image)
    
    # show qr.code
    qr_image_label.configure(image=tk_image)
    qr_image_label.image = tk_image

    # save image if checkbox is checked
    if save_checkbox_var.get():
        app_data_dir = appdirs.user_data_dir(appname="QRCodeGenerator", appauthor="kyndadumb")
        os.makedirs(app_data_dir, exist_ok=True)
        image_path = os.path.join(app_data_dir, "qr_code.png")
        qr_image.save(image_path)
        print("QR-Code wurde gespeichert:", image_path)


# params for tk window
window = tk.Tk()
window.title("QR-Code Generator")
window.geometry("500x400")

# input-box
input_label = tk.Label(window, text="Input:")
input_label.pack()
input_entry = tk.Entry(window, width=50)
input_entry.pack()

# button: start qr-code generation
generate_button = tk.Button(window, text="Generate QR-Code", command=generate_qr_code)
generate_button.pack()

# checkbox: save qr code image
save_checkbox_var = tk.IntVar()
save_checkbox = tk.Checkbutton(window, text="Save QR-Code as picture", variable=save_checkbox_var)
save_checkbox.pack()

# label for image
qr_image_label = tk.Label(window)
qr_image_label.pack()

# open tk window
window.mainloop()
