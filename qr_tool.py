'''
Einfaches QR Tool zur Anzeige und zum Speichern des QR Code
https://github.com/wolli112/qr_tool

MIT License

Copyright (c) 2024 wolli112

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
__version__ = '0.3'
__author__ = 'wolli112'

import tkinter as tk
import qrcode
from PIL import ImageTk
from tkinter import filedialog

# VARIABLEBN
# Globale Variable für das QR-Code-Bild
img = None

# FUNKTIONEN
# Generierung des QR Codes
def qr_erstellen():
    global img  # Deklariere img als eine globale Variable
    data = input_field.get()
    
    # Erstellen einer QR-Code-Instanz
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Daten zum QR-Code hinzufügen
    qr.add_data(data)
    qr.make(fit=True)

    # Erstellen eines Bild aus dem QR-Code
    img = qr.make_image(fill='black', back_color='white')
    
    # Optional - Automatische Speichern des QR Code im Programmordner
    #img.save("qr_code.png")

    # Konvertieren des PIL-Bild in ein tkinter-Bild
    img_tk = ImageTk.PhotoImage(img)

    # Zeigt das Bild in einem Label im Hauptfenster an
    qr_code_label.config(image=img_tk)
    qr_code_label.image = img_tk

    # Zeiget den "Speichern" Button an
    save_button.grid(row=5, column=0, columnspan=2, pady=5)

# Speichern des QR Code über ein Explorer Fenster
def speichern():
    if img:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], parent=root)
        if file_path:
            img.save(file_path)
        
        # Optional - Falls man möchte das das Fenster nach dem Speichern automatisch geschlossen wird
        #root.quit()
        #root.destroy()

# Funktion um das Fenster in der Mitte des Bildschirm anzuzeigen
def zentriere_fenster(fenster):
    
    # Bildschirmgröße ermitteln
    bildschirm_breite = fenster.winfo_screenwidth()
    bildschirm_hoehe = fenster.winfo_screenheight()

    # x- und y-Koordinaten für die Mitte des Bildschirms berechnen
    x = (bildschirm_breite - fenster.winfo_reqwidth()) // 2
    y = (bildschirm_hoehe - fenster.winfo_reqheight()) // 4

    # Fensterposition setzen
    root.geometry(f'+{x}+{y}')
   
# HAUPTPROGRAMM
# Erstellen des Hauptfenster
root = tk.Tk()
root.title("Einfaches QR Tool by wolli112")

# Erstellen der Texte
textlabel = tk.Label(root, font=("Arial", 14), text="Tool zum Erstellen von QR Codes")
textlabel.grid(row=0, column=0, columnspan=2, pady=5)

# Erstellen des Eingabefeldes
input_text = tk.Label(root, font=("Arial", 13), text="Daten eingeben:")
input_text.grid(row=1, column=0, columnspan=1, pady=5)
input_field = tk.Entry(root, font=("Arial", 13))
input_field.grid(row=1, column=1, columnspan=1, pady=5)

# Erstellen des "Generieren" Button
submit_button = tk.Button(root, text="Generieren", font=("Arial", 13), command=qr_erstellen)
submit_button.grid(row=3, column=0, columnspan=2, pady=5)

# Feld zum Anzeigen des QR Code
qr_code_label = tk.Label(root)
qr_code_label.grid(row=4, column=0, columnspan=2, pady=5)

# Erstellen des "Speichern" Button (anfangs versteckt)
save_button = tk.Button(root, text="Speichern", font=("Arial", 13), command=speichern)

# Hauptfenster in der Mitte positionieren
zentriere_fenster(root)

# Aktualisieren das Hauptfenster, um die Größe an den Inhalt anzupassen
root.update_idletasks()

# Hauptschleife fürs Fenster
root.mainloop()

