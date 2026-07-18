import argparse
import sys
import time
from rich.live import Live
from rich.panel import Panel


from ui.display import make_layout, print_banner, get_footer_panel
from core.monitor import get_system_usage
from core.log_watcher import follow_log

def main() -> None:
    parser = argparse.ArgumentParser(description="NetGuard V2 - Professional Live System & Log Auditor")
    parser.add_argument("-w", "--watch", type=str, required=True, help="Path to the log file to monitor live.")
    args = parser.parse_args()

    
    layout = make_layout()

   
    layout["header"].update(Panel(print_banner(), border_style="red"))
    layout["footer"].update(get_footer_panel())
    
    log_generator = follow_log(args.watch)
    log_buffer = ["[bold green]System Engine: Active and auditing infrastructure...[/bold green]"]

  
    with Live(layout, refresh_per_second=4, screen=True):
        try:
            while True:
               
                cpu, ram, disk = get_system_usage()
                
               
                cpu_color = "green" if cpu < 70 else "yellow" if cpu < 90 else "red"
                ram_color = "green" if ram < 70 else "yellow" if ram < 90 else "red"
                
                layout["system"].update(Panel(
                    f"\n [bold white]💻 INFRASTRUCTURE RESOURCES[/bold white]\n\n"
                    f"  • [white]CPU Load:[/white]      [{cpu_color}][bold]{cpu}%[/bold][/{cpu_color}]\n"
                    f"  • [white]RAM Usage:[/white]     [{ram_color}][bold]{ram}%[/bold][/{ram_color}]\n"
                    f"  • [white]Disk Space:[/white]    [bold cyan]{disk}%[/bold cyan]\n\n"
                    f" [gray]Press Ctrl+C to safely terminate.[/gray]",
                    title="⚡ Real-time Monitor", border_style="cyan"
                ))

                
                new_line = next(log_generator)
                if new_line:
                    log_buffer.append(new_line)
                
                
                logs_display = "\n".join(log_buffer[-14:])
                layout["logs"].update(Panel(logs_display, title="🔍 Security Events Stream", border_style="red"))
                
                time.sleep(0.1)

        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == "__main__":
    main()