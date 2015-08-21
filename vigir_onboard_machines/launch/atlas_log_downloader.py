#!/usr/bin/env python
 
import os
import traceback
import shelve
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.master = master
        master.protocol("WM_DELETE_WINDOW", self._delete_window)

        self.shelf = shelve.open('settings', protocol=0, writeback=True)
        
        self.ip_entry = self._make_entry("Robot IP Addr:", self.shelf.get('ip', "192.168.130.103"), 0)

        robot_interface_directory = os.getenv("ATLAS_ROBOT_INTERFACE", ".")
        self.dir_entry = self._make_entry("Directory:", self.shelf.get('dir', "."), 1)

        self.secs_entry = self._make_entry("Duration:", self.shelf.get('duration', "30"), 2)

        self.button = Button(self, text="Download Log", command=self.log)
        self.button.grid(row=3, columnspan=2, sticky=W+E+N+S, padx=5, pady=5)

    def _make_entry(self, label, default, row):
        lbl = Label(self, text=label)
        lbl.grid(row=row, sticky=W, padx=5, pady=5)

        entry = Entry(self)
        entry.insert(0, default)
        entry.grid(row=row, column=1, sticky=W+E+N+S, padx=5, pady=5)

        return entry


    def log(self):
        try:
            # try to find jef client
            robot_interface_directory = os.getenv("ATLAS_ROBOT_INTERFACE", ".")
            jef_path = os.path.join(robot_interface_directory, "tools", "jef-client")

            if(not os.path.isfile(jef_path)):
                jef_path = "./jef-client"

            if(not os.path.isfile(jef_path)):
                jef_path = "jef-client"

            secs = int(self.secs_entry.get())
            ip = self.ip_entry.get()
            path = "/home/vigir/Experiments/"

            if(not os.path.exists(path)):
                os.mkdir(path)
                
            print("logging {} seconds of data from {} to {}".format(secs, ip, path))
            os.system("{} -s {} -H {} -D {}".format(jef_path, secs, ip, path))
        except:
            traceback.print_exc()

    def _delete_window(self):
        self.shelf['ip'] = self.ip_entry.get()
        self.shelf['dir'] = self.dir_entry.get()
        self.shelf['duration'] = self.secs_entry.get()
        self.shelf.close()
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Atlas Log Downloader")
    app = App(master = root)
    app.mainloop()
