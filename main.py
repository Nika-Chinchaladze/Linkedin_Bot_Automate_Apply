from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Linkedin_Class import LinkedinJob

HD_FONT = ("Helvetica", 15, "bold")
LB_FONT = ("Helvetica", 12, "bold")
EN_FONT = ("Helvetica", 13, "normal")
LOCATIONS = ("European Union", "United States", "Asia", "South America")


class LinkedInBotApplication:
    def __init__(self, window):
        self.window = window
        self.window.title("LinkedIn Bot")
        self.window.geometry("400x620")
        self.window.configure(bg="khaki")
        # extra variables:
        self.entered_job = StringVar()
        self.entered_location = StringVar()
        self.entered_login = StringVar()
        self.entered_password = StringVar()
        self.entered_phone = StringVar()

        # interface:
        self.header = Label(self.window, text="Automate Job Apply", font=HD_FONT, justify='center', bd=1, bg="khaki",
                            highlightthickness=1, relief=RIDGE)
        self.header.place(x=5, y=5, width=390, height=40)

        used_image = Image.open("IMG/link.png")
        used_photo = ImageTk.PhotoImage(used_image)
        self.image_label = Label(self.window, image=used_photo, bd=1, highlightthickness=1, relief=RIDGE)
        self.image_label.image = used_photo
        self.image_label.place(x=5, y=50, width=390, height=245)

        self.answer = Label(self.window, text="", font=LB_FONT, justify="center", bd=1, bg="khaki",
                            highlightthickness=1, relief=RIDGE)
        self.answer.place(x=5, y=300, width=390, height=50)

        self.central = Frame(self.window, bd=1, highlightthickness=1, relief=RIDGE, bg="khaki")
        self.central.place(x=5, y=355, width=390, height=255)

        self.job_title = Label(self.central, text="Job Title", font=LB_FONT, justify="left", bd=1,
                               highlightthickness=1, relief=RIDGE)
        self.job_title.place(x=5, y=5, width=150, height=30)

        self.job_entry = Entry(self.central, font=EN_FONT, justify="center", bd=1, highlightthickness=1, relief=RIDGE,
                               textvariable=self.entered_job, fg="maroon")
        self.job_entry.place(x=160, y=5, width=220, height=31)

        self.location = Label(self.central, text="Choose Location", font=LB_FONT, justify="left", bd=1,
                              highlightthickness=1, relief=RIDGE)
        self.location.place(x=5, y=40, width=150, height=30)

        self.loc_entry = ttk.Combobox(self.central, font=EN_FONT, justify="center", textvariable=self.entered_location)
        self.loc_entry["values"] = LOCATIONS
        self.loc_entry.current(0)
        self.loc_entry.place(x=160, y=40, width=220, height=30)

        self.username = Label(self.central, text="Username", font=LB_FONT, justify="left", bd=1,
                              highlightthickness=1, relief=RIDGE)
        self.username.place(x=5, y=75, width=150, height=30)

        self.name_entry = Entry(self.central, font=EN_FONT, justify="center", bd=1, highlightthickness=1, relief=RIDGE,
                                textvariable=self.entered_login, fg="maroon")
        # self.name_entry.insert(0, "chincho2022chincho@gmail.com")
        self.name_entry.place(x=160, y=75, width=220, height=31)

        self.password = Label(self.central, text="Password", font=LB_FONT, justify="left", bd=1,
                              highlightthickness=1, relief=RIDGE)
        self.password.place(x=5, y=110, width=150, height=30)

        self.code_entry = Entry(self.central, font=EN_FONT, justify="center", bd=1, highlightthickness=1, relief=RIDGE,
                                textvariable=self.entered_password, fg="maroon", show="*")
        # self.code_entry.insert(0, "ILoveLinkedIn")
        self.code_entry.place(x=160, y=110, width=220, height=31)

        self.phone = Label(self.central, text="Phone Number", font=LB_FONT, justify="left", bd=1,
                           highlightthickness=1, relief=RIDGE)
        self.phone.place(x=5, y=145, width=150, height=30)

        self.phone_entry = Entry(self.central, font=EN_FONT, justify="center", bd=1, highlightthickness=1, relief=RIDGE,
                                 textvariable=self.entered_phone, fg="maroon")
        self.phone_entry.place(x=160, y=145, width=220, height=31)

        self.apply_button = Button(self.central, text="Apply Jobs", font=LB_FONT, justify="center", bd=1,
                                   highlightthickness=1, relief=RIDGE, bg="navy", fg="light cyan",
                                   command=self.apply_method)
        self.apply_button.place(x=5, y=180, width=375, height=30)

        self.close_button = Button(self.central, text="Close Application", font=LB_FONT, justify="center", bd=1,
                                   highlightthickness=1, relief=RIDGE, bg="light coral", command=self.close_method)
        self.close_button.place(x=5, y=215, width=375, height=30)

    # ================================== FUNCTIONALITY ====================================== #
    def close_method(self):
        self.window.destroy()

    def apply_method(self):
        bot_tool = LinkedinJob()
        bot_tool.into_linkedin(username=self.entered_login.get(), password=self.entered_password.get())
        bot_tool.find_jobs(job_title=self.entered_job.get(), location=self.entered_location.get())
        app_number = bot_tool.apply_jobs(phone=self.entered_phone.get())
        self.answer.config(text=f"{app_number} - Application Has Been Sent, Successfully!", bg="pale green")


def launch_app():
    app = Tk()
    LinkedInBotApplication(app)
    app.mainloop()


if __name__ == "__main__":
    launch_app()
