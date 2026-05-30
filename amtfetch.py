#!/usr/bin/env python3
"""
AMTFetch - Anime GIF Edition (Terminal)
Animated ASCII art with precise system specifications
"""

import os
import sys
import platform
import subprocess
import random
import time
import threading
import psutil
import GPUtil
from datetime import datetime
from pathlib import Path
import json

# Try to import for better Windows support
try:
    import wmi
    WMI_AVAILABLE = True
except ImportError:
    WMI_AVAILABLE = False

# Color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    @staticmethod
    def random():
        colors = [Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.BLUE, Colors.MAGENTA, Colors.CYAN]
        return random.choice(colors)

class AnimatedAnimeASCII:
    """Animated ASCII art sequences"""
    
    ANIMATIONS = {
        "naruto_run": {
            "name": "Naruto Running",
            "frames": [
                [
                    "    🍥      ",
                    "    |\\     ",
                    "    | \\    ",
                    "   /   \\   ",
                    "  /     \\  ",
                    " /       \\ ",
                    "Believe it! "
                ],
                [
                    "     🍥     ",
                    "     |\\    ",
                    "     | \\   ",
                    "    /   \\  ",
                    "   /     \\ ",
                    "  /       \\",
                    "  Dattebayo! "
                ],
                [
                    "      🍥    ",
                    "      |\\   ",
                    "      | \\  ",
                    "     /   \\ ",
                    "    /     \\",
                    "   /       \\",
                    "   Rasengan! "
                ]
            ]
        },
        
        "pikachu_dance": {
            "name": "Pikachu Dancing",
            "frames": [
                [
                    "   ╭━━━━╮   ",
                    "   ┃•  •┃   ",
                    "   ┃  > ┃   ",
                    "   ╰━━━╯    ",
                    "  /     \\   ",
                    " Pika Pika! "
                ],
                [
                    "   ╭━━━━╮   ",
                    "   ┃•  •┃   ",
                    "   ┃  < ┃   ",
                    "   ╰━━━╯    ",
                    "  \\     /   ",
                    "  Chu Pika! "
                ]
            ]
        },
        
        "goku_charging": {
            "name": "Goku Charging",
            "frames": [
                [
                    "    _____    ",
                    "   /     \\   ",
                    "  | () () |  ",
                    "   \\  ^  /   ",
                    "    |||||    ",
                    "   KAME...   "
                ],
                [
                    "    _____    ",
                    "   /     \\   ",
                    "  | () () |  ",
                    "   \\  ^  /   ",
                    "   ⚡|||||⚡  ",
                    "   HAME...   "
                ],
                [
                    "    _____    ",
                    "   /     \\   ",
                    "  | () () |  ",
                    "   \\  ^  /   ",
                    "  ⚡⚡|||⚡⚡ ",
                    "   HAAAAA!   "
                ]
            ]
        },
        
        "levi_cleaning": {
            "name": "Levi Cleaning",
            "frames": [
                [
                    "   ______    ",
                    "  /      \\   ",
                    " |  o  o |   ",
                    " |   >   |   ",
                    " |  ___  |   ",
                    " | /   \\ |   ",
                    " *cleaning*  "
                ],
                [
                    "   ______    ",
                    "  /      \\   ",
                    " |  o  o |   ",
                    " |   >   |   ",
                    " |  ███  |   ",
                    " | /   \\ |   ",
                    " *swish swish*"
                ]
            ]
        },
        
        "gojo_dancing": {
            "name": "Gojo Dancing",
            "frames": [
                [
                    "   /‾‾‾‾\\    ",
                    "  |  ● ● |   ",
                    "  |   →  |   ",
                    "  |  ‾‾‾ |   ",
                    "  | /   \\|   ",
                    "  'Nah, I'd win'"
                ],
                [
                    "   /‾‾‾‾\\    ",
                    "  |  ● ● |   ",
                    "  |   ←  |   ",
                    "  |  ‾‾‾ |   ",
                    "  |/     \\   ",
                    "  Domain Expansion!"
                ]
            ]
        }
    }
    
    @classmethod
    def get_random(cls):
        """Get random animation"""
        return random.choice(list(cls.ANIMATIONS.keys()))

class PreciseSystemInfo:
    """Get exact system specifications"""
    
    @staticmethod
    def get_cpu_exact():
        """Get detailed CPU information"""
        cpu_info = {}
        
        if platform.system() == "Windows":
            if WMI_AVAILABLE:
                c = wmi.WMI()
                for processor in c.Win32_Processor():
                    cpu_info['name'] = processor.Name.strip()
                    cpu_info['cores'] = processor.NumberOfCores
                    cpu_info['threads'] = processor.NumberOfLogicalProcessors
                    cpu_info['max_clock'] = f"{processor.MaxClockSpeed} MHz"
                    cpu_info['architecture'] = processor.Architecture
            else:
                cpu_info['name'] = platform.processor()
                cpu_info['cores'] = psutil.cpu_count(logical=False)
                cpu_info['threads'] = psutil.cpu_count(logical=True)
        else:
            # Linux/macOS
            cpu_info['name'] = subprocess.getoutput("lscpu | grep 'Model name' | cut -d':' -f2 | xargs")
            cpu_info['cores'] = psutil.cpu_count(logical=False)
            cpu_info['threads'] = psutil.cpu_count(logical=True)
            cpu_info['max_clock'] = f"{psutil.cpu_freq().max:.0f} MHz" if psutil.cpu_freq() else "N/A"
        
        return cpu_info
    
    @staticmethod
    def get_gpu_exact():
        """Get detailed GPU information"""
        gpus = []
        
        try:
            # Try GPUtil first
            gpu_list = GPUtil.getGPUs()
            for gpu in gpu_list:
                gpus.append({
                    'name': gpu.name,
                    'memory': f"{gpu.memoryTotal} MB",
                    'driver': gpu.driver,
                    'load': f"{gpu.load*100:.1f}%"
                })
        except:
            # Fallback methods
            if platform.system() == "Windows":
                if WMI_AVAILABLE:
                    c = wmi.WMI()
                    for gpu in c.Win32_VideoController():
                        gpus.append({
                            'name': gpu.Name,
                            'memory': f"{int(gpu.AdapterRAM)/1024**3:.1f} GB" if gpu.AdapterRAM else "N/A",
                            'driver': gpu.DriverVersion
                        })
            elif platform.system() == "Linux":
                gpu_info = subprocess.getoutput("lspci | grep -E 'VGA|3D' | cut -d':' -f3 | xargs")
                if gpu_info:
                    gpus.append({'name': gpu_info, 'memory': 'N/A', 'driver': 'N/A'})
            elif platform.system() == "Darwin":
                gpu_info = subprocess.getoutput("system_profiler SPDisplaysDataType | grep 'Chipset Model' | head -1 | cut -d':' -f2 | xargs")
                gpus.append({'name': gpu_info, 'memory': 'N/A', 'driver': 'N/A'})
        
        return gpus
    
    @staticmethod
    def get_ram_exact():
        """Get exact RAM information"""
        memory = psutil.virtual_memory()
        return {
            'total': f"{memory.total / (1024**3):.2f} GB",
            'available': f"{memory.available / (1024**3):.2f} GB",
            'used': f"{memory.used / (1024**3):.2f} GB",
            'percentage': f"{memory.percent}%"
        }
    
    @staticmethod
    def get_disk_exact():
        """Get detailed disk information"""
        disks = []
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disks.append({
                    'device': partition.device,
                    'mount': partition.mountpoint,
                    'total': f"{usage.total / (1024**3):.2f} GB",
                    'used': f"{usage.used / (1024**3):.2f} GB",
                    'free': f"{usage.free / (1024**3):.2f} GB",
                    'percent': f"{usage.percent}%"
                })
            except:
                pass
        return disks
    
    @staticmethod
    def get_network_exact():
        """Get network information"""
        network = psutil.net_if_addrs()
        interfaces = {}
        for interface, addrs in network.items():
            for addr in addrs:
                if addr.family == 2:  # IPv4
                    interfaces[interface] = addr.address
        return interfaces
    
    @staticmethod
    def get_battery_exact():
        """Get battery information (if available)"""
        if hasattr(psutil, "sensors_battery"):
            battery = psutil.sensors_battery()
            if battery:
                return {
                    'percent': f"{battery.percent}%",
                    'plugged': "Yes" if battery.power_plugged else "No",
                    'time_left': f"{battery.secsleft // 3600}h {(battery.secsleft % 3600) // 60}m" if battery.secsleft != -1 else "N/A"
                }
        return None
    
    @staticmethod
    def get_temperature():
        """Get system temperatures"""
        temps = {}
        if hasattr(psutil, "sensors_temperatures"):
            for name, entries in psutil.sensors_temperatures().items():
                for entry in entries:
                    temps[name] = f"{entry.current}°C"
        return temps
    
    @staticmethod
    def get_os_exact():
        """Get exact OS information"""
        os_info = {}
        
        if platform.system() == "Windows":
            os_info['name'] = platform.system()
            os_info['version'] = platform.version()
            os_info['release'] = platform.release()
            if WMI_AVAILABLE:
                c = wmi.WMI()
                for os in c.Win32_OperatingSystem():
                    os_info['build'] = os.BuildNumber
                    os_info['service_pack'] = os.ServicePackMajorVersion
        elif platform.system() == "Linux":
            os_info['name'] = platform.system()
            os_info['release'] = platform.release()
            try:
                with open("/etc/os-release", "r") as f:
                    for line in f:
                        if line.startswith("PRETTY_NAME="):
                            os_info['pretty_name'] = line.split("=")[1].strip().strip('"')
            except:
                pass
        elif platform.system() == "Darwin":
            os_info['name'] = "macOS"
            os_info['version'] = subprocess.getoutput("sw_vers -productVersion")
        
        return os_info

class AMTFetchAnime:
    def __init__(self):
        self.os_name = platform.system()
        self.precise = PreciseSystemInfo()
        self.animation_name = AnimatedAnimeASCII.get_random()
        self.animation = AnimatedAnimeASCII.ANIMATIONS[self.animation_name]
        self.current_frame = 0
        self.animating = False
        self.color = Colors.random()
        
    def animate(self):
        """Animation thread"""
        self.animating = True
        while self.animating:
            # Clear current line and print frame
            frame = self.animation['frames'][self.current_frame]
            sys.stdout.write('\r' + ' ' * 40 + '\r')  # Clear line
            for line in frame:
                sys.stdout.write(f"\r{self.color}{line}{Colors.RESET}\n")
            sys.stdout.flush()
            
            # Move cursor back up for next frame
            for _ in range(len(frame)):
                sys.stdout.write('\033[F')
            
            self.current_frame = (self.current_frame + 1) % len(self.animation['frames'])
            time.sleep(0.3)
    
    def get_all_info(self):
        """Collect all system information"""
        info = {
            'os': self.precise.get_os_exact(),
            'cpu': self.precise.get_cpu_exact(),
            'gpu': self.precise.get_gpu_exact(),
            'ram': self.precise.get_ram_exact(),
            'disks': self.precise.get_disk_exact(),
            'network': self.precise.get_network_exact(),
            'battery': self.precise.get_battery_exact(),
            'temperatures': self.precise.get_temperature(),
            'hostname': platform.node(),
            'username': os.environ.get('USER', os.environ.get('USERNAME', 'user')),
            'python_version': platform.python_version(),
            'uptime': time.time() - psutil.boot_time()
        }
        return info
    
    def display(self):
        """Display animated anime with exact specs"""
        info = self.get_all_info()
        
        # Start animation in background
        animation_thread = threading.Thread(target=self.animate, daemon=True)
        animation_thread.start()
        
        time.sleep(0.5)  # Let animation start
        
        # Display system information
        print(f"\n{self.color}{'='*70}{Colors.RESET}")
        print(f"{self.color}🎬 AMTFetch - Anime GIF Edition 🎬{Colors.RESET}")
        print(f"{self.color}{'='*70}{Colors.RESET}\n")
        
        print(f"{Colors.CYAN}📊 EXACT SYSTEM SPECIFICATIONS{Colors.RESET}")
        print(f"{Colors.DIM}{'-'*50}{Colors.RESET}")
        
        # OS Information
        print(f"{Colors.GREEN}🖥️  OPERATING SYSTEM:{Colors.RESET}")
        print(f"   Name: {info['os'].get('pretty_name', info['os'].get('name', 'N/A'))}")
        print(f"   Version: {info['os'].get('version', info['os'].get('release', 'N/A'))}")
        print(f"   Build: {info['os'].get('build', 'N/A')}")
        
        # CPU Information
        print(f"\n{Colors.GREEN}⚡ CPU:{Colors.RESET}")
        print(f"   Model: {info['cpu'].get('name', 'N/A')}")
        print(f"   Cores: {info['cpu'].get('cores', 'N/A')} (Physical)")
        print(f"   Threads: {info['cpu'].get('threads', 'N/A')} (Logical)")
        print(f"   Max Clock: {info['cpu'].get('max_clock', 'N/A')}")
        
        # GPU Information
        print(f"\n{Colors.GREEN}🎮 GPU:{Colors.RESET}")
        for i, gpu in enumerate(info['gpu'], 1):
            print(f"   GPU {i}: {gpu.get('name', 'N/A')}")
            print(f"      Memory: {gpu.get('memory', 'N/A')}")
            if gpu.get('driver') != 'N/A':
                print(f"      Driver: {gpu.get('driver')}")
        
        # RAM Information
        print(f"\n{Colors.GREEN}🧠 RAM:{Colors.RESET}")
        print(f"   Total: {info['ram']['total']}")
        print(f"   Used: {info['ram']['used']} ({info['ram']['percentage']})")
        print(f"   Available: {info['ram']['available']}")
        
        # Disk Information
        print(f"\n{Colors.GREEN}💾 DISK DRIVES:{Colors.RESET}")
        for disk in info['disks']:
            print(f"   {disk['device']} ({disk['mount']})")
            print(f"      Total: {disk['total']} | Used: {disk['used']} ({disk['percent']}) | Free: {disk['free']}")
        
        # Network Information
        print(f"\n{Colors.GREEN}🌐 NETWORK:{Colors.RESET}")
        for interface, ip in info['network'].items():
            if not interface.startswith(('lo', 'Loopback')):
                print(f"   {interface}: {ip}")
        
        # Battery Information
        if info['battery']:
            print(f"\n{Colors.GREEN}🔋 BATTERY:{Colors.RESET}")
            print(f"   Charge: {info['battery']['percent']}")
            print(f"   Plugged In: {info['battery']['plugged']}")
            print(f"   Time Left: {info['battery']['time_left']}")
        
        # Temperature Information
        if info['temperatures']:
            print(f"\n{Colors.GREEN}🌡️  TEMPERATURES:{Colors.RESET}")
            for sensor, temp in info['temperatures'].items():
                print(f"   {sensor}: {temp}")
        
        # System Info
        print(f"\n{Colors.GREEN}📱 SYSTEM INFO:{Colors.RESET}")
        print(f"   Hostname: {info['hostname']}")
        print(f"   Username: {info['username']}")
        print(f"   Python Version: {info['python_version']}")
        print(f"   Uptime: {int(info['uptime'] // 3600)}h {int((info['uptime'] % 3600) // 60)}m")
        
        print(f"\n{self.color}{'─'*70}{Colors.RESET}")
        print(f"{Colors.MAGENTA}✨ Current Anime: {self.animation['name']}{Colors.RESET}")
        print(f"{Colors.DIM}🎲 Press Ctrl+C to stop animation{Colors.RESET}")
        
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.animating = False
            print(f"\n\n{self.color}✨ Sayonara! ✨{Colors.RESET}\n")

def install_requirements():
    """Install required packages"""
    requirements = [
        'psutil',
        'GPUtil',
        'wmi; platform_system=="Windows"'
    ]
    
    print("📦 Installing required packages...")
    for req in requirements:
        if ';' in req:
            if eval(req.split(';')[1]):
                subprocess.check_call([sys.executable, "-m", "pip", "install", req.split(';')[0]])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", req])

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--install-deps":
        install_requirements()
    else:
        try:
            fetcher = AMTFetchAnime()
            fetcher.display()
        except KeyboardInterrupt:
            print("\n\n✨ Goodbye! ✨")
        except Exception as e:
            print(f"Error: {e}")
            print("Run 'python amtfetch.py --install-deps' to install dependencies")