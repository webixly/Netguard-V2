from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.layout import Layout

console = Console()

def print_banner() -> None:
    """Prints a compact, cyber-style dashboard header."""
    
    return "[bold red]🛡️  NETGUARD V2[/bold red] [white] | Professional Security & Infrastructure Auditor[/white]"

def make_layout() -> Layout:
    """Creates an advanced, professional TUI layout with a dedicated signature footer."""
    layout = Layout()
    
   
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body", ratio=1),
        Layout(name="footer", size=3)
    )
    
   
    layout["body"].split_row(
        Layout(name="system", ratio=1),
        Layout(name="logs", ratio=2)
    )
    return layout

def get_footer_panel() -> Panel:
    """Creates a professional footer with your signature and status."""
    
    signature = "[bold white]Developed by:[/bold white] [bold cyan]Ayman (webixly)[/bold cyan] [gray]| Blue Team Engineering[/gray]"
    status_info = "[bold green]● CORE ENGINE ACTIVE[/bold green] [gray]| Version: 2.0.0[/gray]"
    
    
    footer_text = f"{signature}   ▲   {status_info}"
    return Panel(Align.center(footer_text), border_style="bright_black", title="System Status")