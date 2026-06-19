#!/usr/bin/env python3
import os
import subprocess
import time
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

subprocess.run(['clear'])
print('© 2026 - Exaral. All rights reserved.')
print('')
console = Console()

def show_menu():
    table = Table(title="", style="bold green")
    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")
    table.add_row("1", "Create folder")
    table.add_row("2", "Install or remove program (apt)")
    table.add_row("3", "Format partitions or disks")  # CORRIGIDO: Linha unificada
    table.add_row("4", "Heimdall (flash Samsung devices)")
    table.add_row("5", "Run Windows programs via Wine")
    table.add_row("6", "Edit or create text files (nano)")
    table.add_row("7", "Remove files or folders (rm)")
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
                subprocess.run(["clear"])
                continue

        # Option 1 - Create folder
        if q == 1:
            ES = int(Prompt.ask("Enable sudo? (1- No, 2- Yes)"))
            fn = Prompt.ask("Enter folder name")
            cmd = ["mkdir", fn] if ES == 1 else ["sudo", "mkdir", fn]
            subprocess.run(cmd)

        # Option 2 - Install or remove program (apt)
        elif q == 2:
            bq1 = int(Prompt.ask("Install(1) or remove(2)?"))
            pn = Prompt.ask("Enter program name")
            cmd = ["sudo", "apt", "install", pn] if bq1 == 1 else ["sudo", "apt", "remove", pn]
            subprocess.run(cmd)

        # Option 3 - Format partitions or disks
        elif q == 3:
            console.print("[yellow]⚠️%EF%B8%8F Warning: if it's removable media, plug it now.[/yellow]")
            input("Press Enter when ready...")
            subprocess.run(["lsblk"])
            cq1 = Prompt.ask("Enter partition or disk (example: /dev/sdx)")
            cq2 = int(Prompt.ask("Choose filesystem: FAT32(1), EXT4(2), NTFS(3)"))
            fs_map = {1: "mkfs.vfat", 2: "mkfs.ext4", 3: "mkfs.ntfs"}
            if cq2 in fs_map:
                confirm = Prompt.ask(f"Are you sure you want to format {cq1} as {fs_map[cq2].split('.')[1].upper()}? (y/n)")
                if confirm.lower() == "y":
                    subprocess.run(["sudo", fs_map[cq2], cq1])
            else:
                console.print("[red]Invalid filesystem choice.[/red]")

        # Option 4 - Heimdall
        elif q == 4:
            dq1 = int(Prompt.ask("Install custom OS? (1- Yes, 2- No)"))
            if dq1 == 1:
                dq2 = Prompt.ask("Choose partition to flash (example: --BOOT)")
                dq3 = Prompt.ask("Enter file source path")
                confirm = Prompt.ask(f"⚠️%EF%B8%8F Are you sure you want to flash {dq2} with {dq3}? (y/n)")
                if confirm.lower() == "y":
                    if not dq2.startswith("-"):
                        dq2 = f"--{dq2}"
                    subprocess.run(["heimdall", "flash", dq2, dq3])
                else:
                    console.print("[red]Flash aborted.[/red]")
            else:
                console.print("[yellow]Abort.[/yellow]")

        # Option 5 - Run Windows programs via Wine
        elif q == 5:
            eq1 = Prompt.ask("Enter file source path")
            console.print("[yellow]Note: Wine should ideally run without sudo to prevent lockouts.[/yellow]")
            ES = int(Prompt.ask("Enable sudo? (1- No, 2- Yes)"))
            cmd = ["wine", eq1] if ES == 1 else ["sudo", "wine", eq1]
            subprocess.run(cmd)

        # Option 6 - Edit or create text files (nano)
        elif q == 6:
            fq1 = Prompt.ask("Enter file source path (or new file name)")
            ES = int(Prompt.ask("Enable sudo? (1- No, 2- Yes)"))
            cmd = ["nano", fq1] if ES == 1 else ["sudo", "nano", fq1]
            subprocess.run(cmd)

        # Option 7 - Remove files or folders (rm)
        elif q == 7:
            hq1 = Prompt.ask("Enter file or folder path")
            ES = int(Prompt.ask("Enable sudo? (1- No, 2- Yes)"))
            EF = int(Prompt.ask("Enable forced? (1- No, 2- Yes)"))
            
            # Fixed forced/recursive logic
            if os.path.isdir(hq1):
                cmd = ["rm", "-rf", hq1] if EF == 2 else ["rm", "-r", hq1]
            else:
                cmd = ["rm", "-f", hq1] if EF == 2 else ["rm", hq1]
                
            if ES == 2:
                cmd.insert(0, "sudo")
                
            confirm = Prompt.ask(f"⚠️%EF%B8%8F Are you sure you want to delete {hq1}? (y/n)")
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
            subprocess.run(["clear"])

    except KeyboardInterrupt:
        console.print("\n[red]Interrupted. Do you really want to exit?[/red]")
        YN = int(Prompt.ask("1- No / 2- Yes"))
        if YN == 1:
            console.print("[green]Restarting...[/green]")
            time.sleep(0.5)
            subprocess.run(["clear"])
        elif YN == 2:
            console.print("[yellow]Goodbye![/yellow]")
            time.sleep(0.3)
            subprocess.run(["clear"])
            break
