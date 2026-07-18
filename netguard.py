import argparse
import sys
import time
from rich.live import Live
from rich.panel import Panel
from rich.columns import Columns
import os
from ui.display import make_layout, print_banner
from core.monitor import get_system_usage
from core.log_watcher import follow_log, stats, DISCORD_WEBHOOK_URL

def main() -> None:
    parser = argparse.ArgumentParser(description="NetGuard V2 - Professional SOC Dashboard")
    parser.add_argument("-w", "--watch", type=str, required=True, help="Path to the log file.")
    args = parser.parse_args()

    layout = make_layout()
    start_time = time.time()

    layout["header"].update(Panel(print_banner(), border_style="red", padding=(0, 2)))
    
    log_generator = follow_log(args.watch)
    log_buffer = ["[bold green]● SOC Core Engine Active: Auditing live infrastructure events...[/bold green]"]

    with Live(layout, refresh_per_second=4, screen=True):
        try:
            while True:
                c = stats["counters"]
                counters_text = (
                    f"[bold red]Brute Force:[/] {c['Brute Force']:<8} "
                    f"[bold magenta]SQLi:[/] {c['SQLi']:<8} "
                    f"[bold purple]XSS:[/] {c['XSS']:<8} "
                    f"[bold yellow]Recon:[/] {c['Recon']:<8} "
                    f"[bold blue]DoS:[/] {c['DoS']}"
                )
                layout["counters"].update(Panel(counters_text, title="📊 Live Threat Indicators", border_style="bright_black"))

                # 2. جلب موارد السيرفر وتحديث القائمة الجانبية (System Summary)
                cpu, ram, disk = get_system_usage()
                cpu_color = "green" if cpu < 70 else "yellow" if cpu < 90 else "red"
                ram_color = "green" if ram < 70 else "yellow" if ram < 90 else "red"
                webhook_status = "[bold green]Connected[/]" if DISCORD_WEBHOOK_URL else "[bold yellow]Disabled[/]"

                summary_text = (
                    f"\n [bold white]📋 SYSTEM SUMMARY[/bold white]\n\n"
                    f"  • Threats Today : [bold red]{stats['threats_today']}[/]\n"
                    f"  • Critical      : [bold black on red] {stats['critical']} [/]\n"
                    f"  • Warnings      : [bold yellow]{stats['high'] + stats['medium']}[/]\n"
                    f"  • Info          : [bold blue]{stats['info']}[/]\n\n"
                    f"  • CPU           : [{cpu_color}][bold]{cpu}%[/bold][/{cpu_color}]\n"
                    f"  • RAM           : [{ram_color}][bold]{ram}%[/bold][/{ram_color}]\n"
                    f"  • Disk          : [bold cyan]{disk}%[/bold cyan]\n\n"
                    f"  • Watching      : [bold yellow]{os.path.basename(args.watch)}[/]\n"
                    f"  • Webhook       : {webhook_status}"
                )
                layout["system"].update(Panel(summary_text, title="⚡ Metrics Overview", border_style="cyan"))

                new_line = next(log_generator)
                if new_line:
                    log_buffer.append(new_line)
                
                logs_display = "\n".join(log_buffer[-12:])
                layout["logs"].update(Panel(logs_display, title="🔍 Real-Time Threat Feed", border_style="red"))

                uptime_secs = int(time.time() - start_time)
                uptime_str = time.strftime('%H:%M:%S', time.gmtime(uptime_secs))
                
                footer_text = (
                    f" Status:  [bold green]Monitoring[/bold green]          "
                    f"Log:     [bold yellow]{os.path.basename(args.watch)}[/bold yellow]          "
                    f"Alerts:  [bold red]{stats['threats_today']}[/bold red]\n"
                    f" Webhook: {webhook_status}           "
                    f"Uptime:  [bold cyan]{uptime_str}[/bold cyan]\n"
                    f"──────────────────────────────────────────────────────────────────────────────────\n"
                    f" [bold white]Press Ctrl+C to safely exit | NetGuard Blue Team System Core[/]"
                )
                layout["footer"].update(Panel(footer_text, title="⚙️ System Status Operations", border_style="bright_black"))

                time.sleep(0.1)

        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == "__main__":
    main()
