import tkinter as tk
from tkinter import messagebox
import re

def submit_data():
    name = name_entry.get()
    course = course_entry.get()
    semester = semester_entry.get()
    form_no = form_no_entry.get()
    contact_no = contact_no_entry.get()
    email_id = email_id_entry.get()
    address = address_entry.get("1.0", tk.END).strip()

    if not name or not course or not semester or not form_no or not contact_no or not email_id or not address:
        messagebox.showerror("Error", "All fields are required.")
        return

    # In a real application, you would process and save this data.
    messagebox.showinfo("Success", f"Data Submitted!\nName: {name}\nCourse: {course}\nSemester: {semester}\nForm No.: {form_no}\nContact No.: {contact_no}\nEmail id: {email_id}\nAddress:\n{address}")

    # Clear the entry fields
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    semester_entry.delete(0, tk.END)
    form_no_entry.delete(0, tk.END)
    contact_no_entry.delete(0, tk.END)
    email_id_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.configure(bg="lightgreen")

# Title Label
title_label = tk.Label(root, text="Sultan's Form", font=("Arial", 16), bg="lightgreen")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels and Entry Fields
labels = ["Name", "Course", "Semester", "Form No.", "Contact No.", "Email id", "Address"]
entries = {}

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=f"{label_text}:", bg="lightgreen")
    label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")
    if label_text == "Address":
        entry = tk.Text(root, height=3, width=30)
    else:
        entry = tk.Entry(root, width=30)
    entry.grid(row=i + 1, column=1, padx=10, pady=5, sticky="ew")
    key = label_text.lower().replace(" ", "_")
    key = re.sub(r'[^a-z0-9_]', '', key)
    entries[key] = entry

# Access the entry widgets using the dictionary
name_entry = entries["name"]
course_entry = entries["course"]
semester_entry = entries["semester"]
form_no_entry = entries["form_no"]
contact_no_entry = entries["contact_no"]
email_id_entry = entries["email_id"]
address_entry = entries["address"]

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_data, bg="red", fg="white")
submit_button.grid(row=len(labels) + 1, column=0, columnspan=2, pady=20)

# Configure column weights to make the entry fields expand
root.grid_columnconfigure(1, weight=1)

# Start the Tkinter event loop
root.mainloop()