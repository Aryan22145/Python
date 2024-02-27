import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random


class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        self.patient_name_var = tk.StringVar()
        self.patient_age_var = tk.StringVar()
        self.patient_gender_var = tk.StringVar()
        self.patient_address_var = tk.StringVar()

        self.patient_list = []

        self.create_widgets()

    def create_widgets(self):
        label_font = ("Gill Sans MT", 18)
        tk.Label(self.root, text="Patient Name:", font=label_font, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10,
                                                                                      sticky="e")
        tk.Label(self.root, text="Age:", font=label_font, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10,
                                                                             sticky="e")
        tk.Label(self.root, text="Gender:", font=label_font, bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10,
                                                                                sticky="e")
        tk.Label(self.root, text="Address:", font=label_font, bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10,

                                                                                 sticky="e")
        tk.Entry(self.root, textvariable=self.patient_name_var, bg="white", fg="black").grid(row=0, column=1, padx=10,
                                                                                             pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.patient_age_var, bg="white", fg="black").grid(row=1, column=1, padx=10,
                                                                                            pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.patient_gender_var, bg="white", fg="black").grid(row=2, column=1, padx=10,
                                                                                               pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.patient_address_var, bg="white", fg="black").grid(row=3, column=1,
                                                                                                padx=10, pady=10,
                                                                                                sticky="w")

        tk.Button(self.root, text="Register Patient", command=self.register_patient, bg="#4CAF50", fg="white").grid(
            row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Display Patients", command=self.display_patients, bg="#007BFF", fg="white").grid(
            row=5, column=0, columnspan=2, pady=10)

    def register_patient(self):
        name = self.patient_name_var.get()
        age = self.patient_age_var.get()
        gender = self.patient_gender_var.get()
        address = self.patient_address_var.get()

        doctor = random.choice(["Dr. Smith", "Dr. Johnson", "Dr. Williams", "Dr. Brown", "Dr. Carlson", "Dr. Micheal", "Dr. Mikkel", "Dr. Monica", "Dr. Sarah", "Dr.Christopher"])

        if name and age and gender and address:
            patient_info = f"Doctor: {doctor}, Name: {name}, Age: {age}, Gender: {gender}, Address: {address}"
            self.patient_list.append(patient_info)
            messagebox.showinfo("Success", f"Patient registered successfully!\nAssigned to {doctor}")
            self.clear_entry_fields()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def display_patients(self):
        if not self.patient_list:
            messagebox.showinfo("Information", "No patients registered.")
        else:
            display_window = tk.Toplevel(self.root)
            display_window.title("Registered Patients")
            display_window.geometry("600x300")

            tree = ttk.Treeview(display_window)
            tree["columns"] = ("Doctor", "Name", "Age", "Gender", "Address")
            tree.heading("#0", text="ID", anchor="center")
            tree.heading("Doctor", text="Doctor", anchor="center")
            tree.heading("Name", text="Name", anchor="center")
            tree.heading("Age", text="Age", anchor="center")
            tree.heading("Gender", text="Gender", anchor="center")
            tree.heading("Address", text="Address", anchor="center")

            for i, patient_info in enumerate(self.patient_list, 1):
                info_list = patient_info.split(", ")
                tree.insert("", i, text=str(i), values=(
                info_list[0][7:], info_list[1][6:], info_list[2][5:], info_list[3][8:], info_list[4][9:]))

            tree.pack()

    def clear_entry_fields(self):
        self.patient_name_var.set("")
        self.patient_age_var.set("")
        self.patient_gender_var.set("")
        self.patient_address_var.set()


if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()
