from tkinter import *
import random
from tkinter import filedialog as fd
import string
from tkinter.ttk import Button, Entry
__version__ = 'Version: 1.0'

icon = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAFbklEQVR42qVWC2yTVRQ+t93W5x6lLYWNritlawbDDRxghqDBRINRMbzCGzbKhkJ4+UAZiTEBFJVnAGEsDAeWyUsFIgGBxCGIQHDIlOBeDEwMa0u7rf37/31dz3+7VkoGGL3pSXvvufd893znnHtK4MljEMq7KENQdD1rTpTfUD5BaX7cYfKI9VQUE0ojyqtjxow9tmbdOtDp9KKOOp0OsnrVKnr+fP0EnB9HKUBpR+n+NwAlUqnULpPJNBzHjcd530mTp3y9Zes2pqT4wUNk6ZLF9MjhQxNxqUOpVJ4UBMEdDodn4Pzi4wAm6PX6uh27dsskRALz5sz0UQpk+VtvK0vLbAkba/ZUw6YNn3GEAN1b+6UqQiPwZkW54HB0TEP1t70BlOj0+rP77QflOWYzFXUtLS2AgFSanEJ8Ph44nodgMESJhBCVQk5lyVLivu8Ci8XC9t9ua4NZM6byTodjHM5/ehAgFWm5UbPvgKlo2PAeJoCEIxHw8wIVAkESEIIgBAMQCARpIBgiuEaREpLZTw8D+ulpzFbDL9do6ezpd1A3VIxJDKBAoVBe+Hz3ntSCpwrZQpJUCqFwGNAQGg1Fv6MA+B2bB9lcq0mHvIFGdq7x1+vwxoKybr+fGy1OEyhSqdWnqr+wq61WK0UAIhoQem4sGsJbQTAUoj4/TwRBXA+SKGCQGjMNJCz4wDZ3htfn9b4UCzbpyfN8FKlKpdp/5MRplcmYRYOi0QcAPO77cPXyJUbf8OJRhBIpdXm64gChcIRYc7Jg5uRXfDhm4b4wyk0RoKpoeLFNizmea82Hsvk2SE9VxSnwcTycO/M9rF/zgYfn/QdFBLlcMXXl6g8zrAVF4HJ3xqnqb9DDpfoz0HTrJricDmi4drVaBLiwvXpfick8kAUqO9MAspRkFlgRpKm5lZbNnITG+RGob4lVt1wuv1xVe1DTxQXwMgGKcSJyeQrkmo3MTntbKyyyzb4oAtzaW/dNblpGBjuZPygHMAuZB17OD1/V1cGWT9dWoWrhQzWzc+k7leX5hcXopZ95AHjOaslmyi6PB+ZNe72JAVTtO5yXlp7BKnRovgWkEgnzoNvHgd1up9s3ftwrwKIV71UUDBsJnJ9nHogRNRszmZ3OTg+Uz578B6Poo807SwYYTcy1wXlmUCsVPRQF4GrDDbqsfK5HEBIosshk8isbdtRoQJoUTQQEkCZJoL9ey+z8ebcd3l+2kFFUlV9QuEDTR0tNZgspnb8ATFmGaHFh8DqcbnrixHFSvX2jOyAILMgpMtlU26IVGUXFz2C6BlgWiQAKhQx+rj9D29taWIXfbLy+OyFN5QrlfryV8vnRIzDnI9CTptDhckNL621obLjGrj+kcBho+vSJ7okVHBZfipRA5fIKjvdzCWkaLzQEOLVi9Vr1qOKnqTk7M6EOeD6AweRYoUUiFHWhhEITaXE57sHGNZVeBEgoNPZUoNsXKpatSjMNFB0idHBeDumr1fxTyb28RTEA8Xf0Fcem0NpMd21e1410JjwVqRKJ5Eb58srsbPOguEumrH5gzDJAOBTp9S0Sk8CLmSbOY+NOazNUbV57JxKJJDx2jCJ1WvrZ0sUr5Vq9gbnsvPcXaHU6ahyQRTCzQCIh7LnGtBRTmLruu0knPiE6Q/84RTXb1vPers4XHqYo3nDUqWl1k+YslBEcB6q3ekXXx774mmrEs+Nie5ixKz+eo/Wnj3EindNtS1SUUnKkdifv7e56ZMOJe0IkEntSUpImGAiwljm4aOTRl6fMSdj03aFa+L3hMmuZySkpJ0OhkBuj/8SWGRsJTd9ozj323PiJoFCpmQd+n5f8cPIovdvW9J+a/sPjf/1t+RsIZRn+UvJPYQAAAABJRU5ErkJggg=="
genbtn = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAADQUlEQVR42p2Te0hTYRjGn+Vx2Y4xs1yFqTlnmNtMTWx2ISMKKygoKQ0s6KIzywqJNOhCF7KoRVPSpAuSoFa0oKAsM0XFdd9ytqVbF6aka5Vzzk3dpe+cSgrqnw4c3u/A9/6+53nP83HwjydUMucxKak/P+t7dNplf9vH+bXIyt3Jb2huLk5OTKyJjIh4XqtS9depVJTH48HK9HT3utVrgj6YzUkvXr3MmC9LKbxxqdw2BsjYLuc3t7WpSXOMvrMT9sFBY5xYLKo4r4SbAHL27EaHXm+kaVokjBSiXdduSEmWyW5euWjj/JRbRprlV0tL4HQ60fr0CVKS58Ex5MKo2wPOuHFofaKGVCKFPzcAB48ehva1tpzYymUBqzKzFpvev2usV92CyzUMiqLYZjdpHvG4SfUCBDLkcoHL9cdWeTaihFGp92quNbGAnIL99N26+xrFieOiBMkcOMnGwEAabq/nB4S81q82+PlR6DDoUHzmtDFteVr8ZcUpB4fIf8hMWxobS5UpFOizfEEQfyIeNDzCmdJSwOdDXo4cC1MWEchXBAdPwqFjR9DZ1ekmfY0MwHfn+g1wKX8MDAzCOTyCaYJgrEhfh7AZYfEMwNxt1lRXVqHnk4XY8wcdyINrdAQ78nLAAm5X1xJ5fvjWb4dzyInQUAHWbFjPAnzkGAZQdaWS1F4yRC4BBJK/M4q8XXIWwARmoThmNlV87DhMpo8ICZkM9TM1LlRcBAPI3rINCfFz0dtnRVh4KE6eOoEuYxdjoYUd4uade+n6xgbNwcIikWDKdJIDBwQhU8DjjYfH64PdPoRPfRYETAiA1dqHc0qFcUnq0qSqUsWPHCxdu36xuae7sVx5gVVA0zwM2O2MfXgJwEsWPHoCATkQHjED+4sKiL3w1IZbtU1jQZKIJfID+4owPDIMw1s9xLESvHtvJhAfK1vX0Q5hVDQZIhfKkrMwGPS/BWnjZr7mtUYdJ42LMZlMJEQOY3T0LFGePJ89vaxcyXg28ng8UeRMITre6Axx0njZvepK29hlWpm5ia9t1xaLokQ1UwXTnre2tfSXKMsoRkH+7h3u+bIFQZbPliSjqStDIpYW1tVW2f64jf97nb8DYQt/cC2pvgMAAAAASUVORK5CYII="
clearbtn = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAArBJREFUeNqkk19I01EUx793zj9tOrc2nK7pXPNP5nDT5UTFylk0XVJEIUT0UEI+1EP0EIhUhA+9FAglFdVDQQWaEW2oGWhRGulkEToqTVamiC6nLt3/2/3lfAop8AcfzuH8u+d37rmEUoqNfPzWeh64ElwdDkJWHZw8fZdiv4HAUrTqizB8Too4PszhCJoDQTTx/uOQUpZ3h4PpO1kh87IPzWXVhwy/VtDM/0dyltVOC1puXTnJtWC90ShlSelG0y5D2/0Oeyi8fgdiFn+Gyb1jY+M3O98lwj8zg5r6iweTtGTqyeNX9slZNEUi6OI6iGUkM2SMNJZYnCAUF2fqyvQjdQVqm82KqiozOrv9qFR9wb5j52oDoas2luzj5sJng7mQIJQUxwtFAkGSVCRLz5ZL5EpZcCnAX5p0o9ooQIf1KUwmC2zdy6hSj8N04ISlu/3eAivQx2OVerwL8/5cY01Fmsag83lo6sSAk++dnYdAKcHP0e+oLVqE1dqGigoLno+kYdG1iFAIPAZizDri6rdTT3/vYF4ihUKYLERKthIxcbGYdnyFRJOKkNePPPEyHr50ICenBHVnLz8q17CboZhYu4WuQi1ZmXMPn88t1VaPDTvBpzxkFGTBO+cB9YUhVslxPN8DY0NdO4tvZb//hluZGMI2ZsELaBTE5Ril7sG3H/JKynWKLdszMeV0IeQPQqSUYf7TFNqePXhtSMe1oW+kL2Mz8PEHW7i1e1OnEKiEFOVaUsnm0pidU7onwhSNPhdzLLmrt2eAbd8l9wpeWEcI1n0CKinBbjXMR/Ix1Hn9ML19agc9qsd701aY5Ul/x3MdcMskZIgYXMgmzqZXoHCbFA3c/n92o8UxjV5mDzD8jGBUD5NokThGfBR+1Mb1GIkSZoSico0/PrLR5/xbgAEAmn8aHZdeMI4AAAAASUVORK5CYII="
savebtn = "R0lGODlhEAAQALMJAABdAA6fBhmqETW1GlLFKQBHAP//AABIAEy1Kf///wAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAkALAAAAAAQABAAAARHMMlJq70SAFyB2VxmECDnEUJ5nUKgdmM7gBrFBkOREZ+I4roEICDgaWLACWBA5CFzlQKz+INapERZ8HJABJKhw8AaShS2lggAOw=="

root = Tk()
root.resizable(width=False, height=False)
root.title("Password generator  " + str(__version__))
root.geometry("532x320+300+300")
calculated_text = Text(root, height=14, width=50)

chars = string.ascii_letters + string.digits + string.punctuation
x = 0

def erase():
    calculated_text.delete('1.0', END)
    global x
    x = 0

def passw():
    for n in range(int(number_entry.get())):
        password = ''
        global x
        x += 1
        for i in range(int(length_entry.get())):
            password += random.choice(chars)
        if x >= 1:
            calculated_text.insert(END, "Password" + '  ' + str(x) + ': ' + password + "\n")

def savepass():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("All files", "*.*")), defaultextension='')
    try:
        f = open(file_name, 'w')
        s = calculated_text.get(1.0, END)
        f.write(s)
        f.close()
    except FileNotFoundError:
        pass

img = PhotoImage(data=icon)
gen = PhotoImage(data=genbtn)
clear = PhotoImage(data=clearbtn)
store = PhotoImage(data=savebtn)

display_button = Button(text=" Generate ", image=gen, compound="left", command=passw)
erase_button = Button(text="    Clear  ", image=clear, compound="left", command=erase)
save = Button(text="     Save  ", image=store, compound="left", command=savepass)

number_entry = Entry(width=10, justify=CENTER)
length_entry = Entry(width=10, justify=CENTER)
number_entry.insert(0, "8")
length_entry.insert(0, "25")

number_label = Label(text="      Number of passwords")
length_label = Label(text="      Password length")
number_label.grid(row=0, column=0, sticky="w")
length_label.grid(row=1, column=0, sticky="w")
number_entry.grid(row=0, column=1, padx=1, pady=5)
length_entry.grid(row=1, column=1, padx=1, pady=5)

display_button.grid(row=3, column=0, padx=30, pady=5, sticky="e")
erase_button.grid(row=3, column=1, padx=30, pady=5, sticky="e")
save.grid(row=3, column=2, padx=30, pady=5, sticky="w")

scrollb = Scrollbar(root, command=calculated_text.yview)
scrollb.grid(row=4, column=3, sticky='nsew')
calculated_text.grid(row=4, column=0, sticky='nsew', columnspan=3)
calculated_text.configure(yscrollcommand=scrollb.set)
root.tk.call('wm', 'iconphoto', root._w, img)
root.mainloop()