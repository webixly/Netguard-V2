from rich.panel import Panel
from rich.align import Align
from rich.layout import Layout

def print_banner() -> str:
    """توليد شعار ASCII احترافي ومميز لـ NetGuard V2"""
    ascii_art = (
        "[bold red]"
        "███████╗ ███████╗ ████████╗ ██████╗  ██╗   ██╗  █████╗  ██████╗  ██████╗ \n"
        "██╔════╝ ██╔════╝ ╚══██╔══╝ ██╔══██╗ ██║   ██║ ██╔══██╗ ██╔══██╗ ██╔══██╗\n"
        "███████╗ █████╗      ██║    ██████╔╝ ██║   ██║ ███████║ ██████╔╝ ██║  ██║\n"
        "╚════██║ ██╔══╝      ██║    ██╔═══╝  ██║   ██║ ██╔══██║ ██╔══██╗ ██║  ██║\n"
        "███████║ ███████╗    ██║    ██║      ╚██████╔╝ ██║  ██║ ██║  ██║ ██████╔╝\n"
        "╚══════╝ ╚══════╝    ╚═╝    ╚═╝       ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═════╝ \n"
        "[/bold red]"
        "[bold white]                  INFRASTRUCTURE SECURITY DASHBOARD V2.0[/bold white]"
    )
    return ascii_art

def make_layout() -> Layout:
    """إنشاء تقسيم شاشة احترافي لاستيعاب العدادات العلوية وشريط الحالة السفلي"""
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=8),
        Layout(name="counters", size=3),
        Layout(name="body", ratio=1),
        Layout(name="footer", size=7)
    )
    layout["body"].split_row(
        Layout(name="system", ratio=1),
        Layout(name="logs", ratio=2)
    )
    return layout
