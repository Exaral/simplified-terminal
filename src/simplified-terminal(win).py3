#!/usr/bin/env python3
import os
import subprocess
import time
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

subprocess.run(['cls'], shell=True)
print('© 2026 - Exaral. All rights reserved.')
print('')
console = Console()

def show_menu():
    table = Table(title="", style="bold green")
    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")
    table.add_row("1", "Create folder")
    table.add_row("2", "Install or remove program (winget)")
    table.add_row("3", "Format partitions or disks")
    table.add_row("4", "Flash Samsung devices (Odin/Heimdall CLI)")
    table.add_row("5", "Run programs or executables")
    table.add_row("6", "Edit or create text files (notepad)")
    table.add_row("7", "Remove files or folders (del/rd)")
    table.add_row("8", "Exit")
    console.print(table)

while True:
    try:
        console.print("[bold magenta]Welcome to Simplified Terminal[/bold magenta]")
        show_menu()
        try:
            q = int(Prompt.ask("Enter your option"))
        except ValueError:
            console.print("[red]Invalid input, please enter a number.[/red]")
            abcd = int(Prompt.ask("Exit (1) or try again (2)?"))
            if abcd == 1:
                break
            elif abcd == 2:
                subprocess.run(["cls"], shell=True)
                continue

        # Option 1 - Create folder
        if q == 1:
            ES = int(Prompt.ask("Requires admin terminal? (1- No, 2- Yes)"))
            fn = Prompt.ask("Enter folder name")
            if ES == 2:
                cmd = ["powershell", "Start-Process", "cmd", f'/c md "{fn}"', "-Verb", "RunAs"]
            else:
                cmd = ["cmd", "/c", "md", fn]
            subprocess.run(cmd)

        # Option 2 - Install or remove program (winget)
        elif q == 2:
            bq1 = int(Prompt.ask("Install(1) or remove(2)?"))
            pn = Prompt.ask("Enter program name")
            action = "install" if bq1 == 1 else "uninstall"
            # Winget exige admin para a maioria das instalações globais de sistema
            cmd = ["powershell", "Start-Process", "winget", f'{action} {pn}', "-Verb", "RunAs"]
            subprocess.run(cmd)

        # Option 3 - Format partitions or disks
        elif q == 3:
            console.print("[yellow]⚠%EF%B8%8F Warning: if it's removable media, plug it now.[/yellow]")
            input("Press Enter when ready...")
            # Get-Disk necessita de privilégios elevados para listar mídias físicas corretamente
            subprocess.run(["powershell", "Start-Process", "powershell", "-ArgumentList 'Get-Disk; Read-Host \"Press Enter to close\"'", "-Verb", "RunAs"])
            cq1 = Prompt.ask("Enter partition volume letter (example: E:)")
            cq2 = int(Prompt.ask("Choose filesystem: FAT32(1), NTFS(2), exFAT(3)"))
            fs_map = {1: "FAT32", 2: "NTFS", 3: "exFAT"}
            if cq2 in fs_map:
                confirm = Prompt.ask(f"Are you sure you want to format {cq1} as {fs_map[cq2]}? (y/n)")
                if confirm.lower() == "y":
                    # Format exige obrigatoriamente elevação administrativa UAC
                    subprocess.run(["powershell", "Start-Process", "format", f'{cq1} /FS:{fs_map[cq2]} /Q', "-Verb", "RunAs"])
            else:
                console.print("[red]Invalid filesystem choice.[/red]")

        # Option 4 - Heimdall / CLI Flasher
        elif q == 4:
            dq1 = int(Prompt.ask("Install custom OS? (1- Yes, 2- No)"))
            if dq1 == 1:
                dq2 = Prompt.ask("Choose partition to flash (example: --BOOT)")
                dq3 = Prompt.ask("Enter file source path")
                confirm = Prompt.ask(f"⚠%EF%B8%8F Are you sure you want to flash {dq2} with {dq3}? (y/n)")
                if confirm.lower() == "y":
                    if not dq2.startswith("-"):
                        dq2 = f"--{dq2}"
                    subprocess.run(["heimdall", "flash", dq2, dq3])
                else:
                    console.print("[red]Flash aborted.[/red]")
            else:
                console.print("[yellow]Abort.[/yellow]")

        # Option 5 - Run programs
        elif q == 5:
            eq1 = Prompt.ask("Enter file source path")
            ES = int(Prompt.ask("Requires admin terminal? (1- No, 2- Yes)"))
            if ES == 2:
                cmd = ["powershell", "Start-Process", "cmd", f'/c "{eq1}"', "-Verb", "RunAs"]
            else:
                cmd = ["cmd", "/c", eq1]
            subprocess.run(cmd)

        # Option 6 - Edit or create text files (notepad)
        elif q == 6:
            fq1 = Prompt.ask("Enter file source path (or new file name)")
            ES = int(Prompt.ask("Requires admin terminal? (1- No, 2- Yes)"))
            if ES == 2:
                cmd = ["powershell", "Start-Process", "notepad", f'"{fq1}"', "-Verb", "RunAs"]
            else:
                cmd = ["notepad", fq1]
            subprocess.run(cmd)

        # Option 7 - Remove files or folders (del / rd)
        elif q == 7:
            hq1 = Prompt.ask("Enter file or folder path")
            ES = int(Prompt.ask("Requires admin terminal? (1- No, 2- Yes)"))
            EF = int(Prompt.ask("Enable forced? (1- No, 2- Yes)"))
            
            # Monta os argumentos base dependendo se é pasta ou arquivo
            if os.path.isdir(hq1):
                args = f'/c rd /s /q "{hq1}"' if EF == 2 else f'/c rd "{hq1}"'
            else:
                args = f'/c del /f /q "{hq1}"' if EF == 2 else f'/c del "{hq1}"'
                
            if ES == 2:
                cmd = ["powershell", "Start-Process", "cmd", args, "-Verb", "RunAs"]
            else:
                cmd = ["cmd", "/c"] + args.split(' ', 2)[1:]
                
            confirm = Prompt.ask(f"⚠%EF%B8%8F Are you sure you want to delete {hq1}? (y/n)")
            if confirm.lower() == "y":
                subprocess.run(cmd)

        # Option 8 - Exit
        elif q == 8:
            console.print("[yellow]Exiting... Goodbye![/yellow]")
            break
        else:
            console.print("[red]Invalid option.[/red]")

        abcd = int(Prompt.ask("Exit (1) or run another command (2)?"))
        if abcd == 1:
            break
        elif abcd == 2:
            subprocess.run(["cls"], shell=True)

    except KeyboardInterrupt:
        console.print("\n[red]Interrupted. Do you really want to exit?[/red]")
        YN = int(Prompt.ask("1- No / 2- Yes"))
        if YN == 1:
            console.print("[green]Restarting...[/green]")
            time.sleep(0.5)
            subprocess.run(["cls"], shell=True)
        elif YN == 2:
            console.print("[yellow]Goodbye![/yellow]")
            time.sleep(0.3)
            subprocess.run(["cls"], shell=True)
            break
