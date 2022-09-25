from ast import keyword
import rich.console
import rich.table
import search
import sys

console = rich.console.Console()

if __name__ == "__main__":
    if sys.argv.__len__() > 1:
        keyword = sys.argv[1]
    else:
        keyword = console.input("[bold blue]Key Word: [/]")
    
    try:
        with console.status("Working . . ."):
            package_list = search.search(keyword)
    except:
        console.print_exception()
        sys.exit(-1)
    
    table = rich.table.Table()
    table.add_column("Name")
    table.add_column("Version")
    table.add_column("Information")

    for pack in package_list:
        if pack["name"] != None:
            table.add_row(
                pack["name"].replace(keyword, f"[bold yellow]{keyword}[/]"),
                pack["version"],
                pack["info"].replace(keyword, f"[bold yellow]{keyword}[/]")
            )
    console.print(table)

    
