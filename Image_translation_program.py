import tkinter as tk
from PIL import Image
import pytesseract
from googletrans import Translator

def translate(image_path,input_lang,output_lang,tesseract_path):
    
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    image=Image.open(image_path)
    result = pytesseract.image_to_string(image)
    try:
        translator=Translator()
        print(translator.translate(text=result,src=input_lang, dest=output_lang))         
    except NameError:
        print("Name Error: Make sure you use a 'String' for the input_lang and output_lang")
    
def create_ui():    
    root = tk.Tk()
    root.title("Image Translation")

    #image path
    image_path = tk.Label(root, text = "Image Path:")
    image_path.grid(row=0, column=0)

    image_path_entry = tk.Entry(root)
    image_path_entry.grid(row=0, column=1)

    #input lang
    input_lang = tk.Label(root, text = "Image Language:")
    input_lang.grid(row=1, column=0)

    input_lang_entry = tk.Entry(root)
    input_lang_entry.grid(row=1, column=1)

    #output lang
    output_lang = tk.Label(root, text = "Output Language:")
    output_lang.grid(row=2, column=0)

    output_lang_entry = tk.Entry(root)
    output_lang_entry.grid(row=2, column=1)

    #tesseract Path
    tesseract_path = tk.Label(root, text = "Tesseract Path:")
    tesseract_path.grid(row=3, column=0)

    tesseract_path_entry = tk.Entry(root)
    tesseract_path_entry.grid(row=3, column=1)

    #button
    generate_button = tk.Button(root, text="Generate", command=lambda: translate(
        image_path_entry.get(),
        input_lang_entry.get().lower(),
        output_lang_entry.get().lower(),
        tesseract_path_entry.get()
    ))
    generate_button.grid(row=4, column=1)

    root.mainloop()
    
create_ui()
