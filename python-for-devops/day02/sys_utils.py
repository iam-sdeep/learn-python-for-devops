#Blueprint  /template
import os

class Utilities:

    def show_disk_space(self):
        print(os.system("df -h"))

    def show_ram(self):
        print(os.system("free -h"))

    def show_system_details(self):
        print(os.uname().sysname)


machine_a = Utilities()  # object 1
machine_a.show_disk_space()

machine_b = Utilities()  # object 2
#machine_b.show_ram()
machine_b.show_system_details()