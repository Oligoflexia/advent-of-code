import argparse
from pathlib import Path
import os
import sys
import subprocess


def new_sol_file(day, year, type):
    if day < 10:
        filename = f"0{day}.py"
    else:
        filename = f"{day}.py"

    folder = Path(str(year))
    data_folder = folder / "data"

    input_type = tuple()

    match str.lower(type):
        case "si":
            input_type = ("StringInput", "input_str")
        case "ssi":
            input_type = ("SplitStringInput", "input_str_list")
        case "ii":
            input_type = ("IntInput", "input_int")
        case "sii":
            input_type = ("SplitIntInput", "input_int_list")

    import_str = f"from utils.input_formatter import {input_type[0]}"

    lhs = f"InputObject, {input_type[1]} ="
    rhs = f" {input_type[0]}.return_input({day}, {year})"
    declaration_str = lhs + rhs

    file_content = import_str + "\n\n" + declaration_str

    try:
        data_folder.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Error: {e}")
        return

    full_filename = os.path.join(folder, filename)

    with open(full_filename, "w") as file:
        file.write(file_content)

    venv_python = sys.executable

    subprocess.run([venv_python, str(full_filename)], check=True)


def main():
    parser = argparse.ArgumentParser(prog="aoc")
    subparsers = parser.add_subparsers(help="sub-command help")

    # aoc new command
    parser_new = subparsers.add_parser("new", help="Create new solution file")
    parser_new.add_argument(
        "-d", "--day", type=int, required=True, help="Puzzle day"
    )
    parser_new.add_argument(
        "-y", "--year", type=int, required=True, help="Puzzle year"
    )
    parser_new.add_argument(
        "-t", "--type", type=str, required=True, help="Type of input string"
    )

    parser_new.set_defaults(
        func=lambda args: new_sol_file(args.day, args.year, args.type)
    )

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
