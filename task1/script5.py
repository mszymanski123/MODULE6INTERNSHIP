import argparse
import platform
import psutil
import socket

def get_system_info(args):
    if args.d:
        print("Distro info:", platform.dist())

    if args.m:
        memory = psutil.virtual_memory()
        print("Memory Info:")
        print(f"Total: {memory.total} bytes")
        print(f"Used: {memory.used} bytes")
        print(f"Free: {memory.free} bytes")

    if args.c:
        cpu_info = {}
        cpu_info['model'] = platform.processor()
        cpu_info['core_numbers'] = psutil.cpu_count()
        cpu_info['speed'] = psutil.cpu_freq().current
        print("CPU Info:", cpu_info)

    if args.u:
        print("Current user:", psutil.users()[0].name)

    if args.l:
        print("System load average:", psutil.getloadavg())

    if args.i:
        print("IP Address:", socket.gethostbyname(socket.gethostname()))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get system information.")
    parser.add_argument("-d", action="store_true", help="Get distro info")
    parser.add_argument("-m", action="store_true", help="Get memory info")
    parser.add_argument("-c", action="store_true", help="Get CPU info")
    parser.add_argument("-u", action="store_true", help="Get current user")
    parser.add_argument("-l", action="store_true", help="Get system load average")
    parser.add_argument("-i", action="store_true", help="Get IP address")
    args = parser.parse_args()
    get_system_info(args)

