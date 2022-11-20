from ctypes import *

class PROCESSENTRY32(Structure):
    _fields_ = [
        ("dwSize", c_uint32),
        ("cntUsage", c_uint32),
        ("th32ProcessID", c_uint32),
        ("th32DefaultHeapID", c_uint64),
        ("th32ModuleID", c_uint32),
        ("cntThreads", c_uint32),
        ("th32ParentProcessID", c_uint32),
        ("pcPriClassBase", c_uint32),
        ("dwFlags", c_uint32),
        ("szExeFile", c_char * 260)
    ]

class Process:

    @staticmethod
    def get_process_handle(proc_name):
        handle = 0
        entry = PROCESSENTRY32()
        snap = windll.kernel32.CreateToolhelp32Snapshot(0x00000002, 0)
        entry.dwSize = sizeof(PROCESSENTRY32)
        while windll.kernel32.Process32Next(snap, pointer(entry)):
            if entry.szExeFile == proc_name.encode("ascii", "ignore"):
                handle = windll.kernel32.OpenProcess(0x430, 0, entry.th32ProcessID)
                break
        windll.kernel32.CloseHandle(snap)
        return handle

    @staticmethod
    def sleep(ms):
        windll.kernel32.Sleep(ms)

    def __init__(self, proc_name):
        self.handle = Process.get_process_handle(proc_name)
        if self.handle == 0:
            raise Exception('Process ' + proc_name + ' not found!')
        else:
            print('Process found!')
    
    def is_running(self):
        buffer = c_uint32()
        windll.kernel32.GetExitCodeProcess(self.handle, pointer(buffer))
        return buffer.value == 0x103

    def get_ptr_addr(self, addy, offsets):
        address = self.r_int(addy)
        for offset in offsets:
            if offset != offsets[-1]:
                address = self.r_int((address + offset))
        address = address + offsets[-1]
        return address
    
    def w_int(self, addr, val):
        buffer = c_uint32(val)
        return windll.ntdll.NtWriteVirtualMemory(self.handle, addr, pointer(buffer), 4, 0) == 0
    
    def r_int(self, addr, len=4):
        buffer = c_uint32()
        windll.ntdll.NtReadVirtualMemory(self.handle, addr, pointer(buffer), len, 0)
        return buffer.value

    def w_float(self, addr, val):
        buffer = c_float(val)
        return windll.ntdll.NtWriteVirtualMemory(self.handle, addr, pointer(buffer), 4, 0) == 0
    
    def r_float(self, addr, len=4):
        buffer = c_float()
        windll.ntdll.NtReadVirtualMemory(self.handle, addr, pointer(buffer), len, 0)
        return buffer.value
    
    def w_bytes(self, addr, val, size):
        t_addr = cast(addr, c_char_p)
        return windll.kernel32.WriteProcessMemory(self.handle, t_addr, val, size, 0) == 0

    def r_bytes(self, addr, size):
        buffer = create_string_buffer(size)
        bytes_read = c_size_t()
        windll.kernel32.ReadProcessMemory(self.handle, c_void_p(addr), byref(buffer), size, byref(bytes_read))
        return buffer.raw