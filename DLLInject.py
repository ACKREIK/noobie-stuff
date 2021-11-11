import sys
from ctypes import *

PAGE_READWRITE = 0x04
PAGE_EXECUTE_READWRITE = 0x00000040

DELETE          = 0x00010000
READ_CONTROL    = 0x00020000
WRITE_DAC       = 0x00040000
WRITE_OWNER     = 0x00080000
SYNCHRONIZE     = 0x00100000
PROCESS_ALL_ACCESS = ( DELETE |
                       READ_CONTROL |
                       WRITE_DAC |
                       WRITE_OWNER |
                       SYNCHRONIZE |
                       0xFFF # If < WinXP/WinServer2003 - 0xFFFF otherwhise
                     )

VIRTUAL_MEM = ( 0x1000 | 0x2000 )

KERNEL32 = windll.kernel32

def dllinject(dll_path, pid):
    """ Inject a DLL into target process.

    :param dll_path: path to dll
    :param pid: target process id
    """
    dll_len = len(dll_path)

    h_process = KERNEL32.OpenProcess(PROCESS_ALL_ACCESS, False, int(pid))
    if not h_process:
        # No handler to PID
        return False

    # Allocate space and write DLL path into it
    dll_address = KERNEL32.VirtualAllocEx(
            h_process, 
            0, 
            dll_len, 
            VIRTUAL_MEM, 
            PAGE_READWRITE)

    w = c_int(0)

    KERNEL32.WriteProcessMemory(
            h_process, 
            dll_address, 
            dll_path, 
            dll_len, 
            byref(w))

    # Where is LoadLibraryA?
    h_kernel32 = KERNEL32.GetModuleHandleA('kernel32.dll')
    h_loadlib = KERNEL32.GetProcAddress(h_kernel32, 'LoadLibraryA')

    # Create thread
    t_id = c_ulong(0)
    if not KERNEL32.CreateRemoteThread(
            h_process, 
            None, 
            0, 
            h_loadlib, 
            dll_address, 
            0, 
            byref(t_id)):
        # Cannot start a thread
        return False
    print(t_id)
    return True

def codeinject(shellcode, pid):
    """ Inject code into target process.

    :param shellcode: shellcode to inject
    :param pid: target process id
    """
    shellcode_len = len(shellcode)

    h_process = KERNEL32.OpenProcess(PROCESS_ALL_ACCESS, False, int(pid))
    if not h_process:
        # No handler to PID
        print('No handler to PID')
        return False

    shellcode_address = KERNEL32.VirtualAllocEx(
            h_process, 
            0, 
            shellcode_len, 
            VIRTUAL_MEM, 
            PAGE_EXECUTE_READWRITE)

    w = c_int(0)

    KERNEL32.WriteProcessMemory(
            h_process, 
            shellcode_address, 
            shellcode, 
            shellcode_len, 
            byref(w))

    t_id = c_ulong(0)
    if not KERNEL32.CreateRemoteThread(
            h_process, 
            None, 
            0, 
            shellcode_address, 
            None, 
            0, 
            byref(t_id)):
        # Cannot start thread
        return False

    return True



import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is the function called when the button is clicked
def loadscript():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')



root = Tk()

# This is the section of code which creates the main window
root.geometry('841x526')
root.configure(background='#76EEC6')
root.title('TestSploit')


# This is the section of code which creates a button
Button(root, text='Load Script', bg='#458B74', font=('arial', 12, 'normal'), command=loadscript).place(x=15, y=484)


# This is the section of code which creates a button
Button(root, text='Inject', bg='#458B74', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=145, y=484)


root.mainloop()
