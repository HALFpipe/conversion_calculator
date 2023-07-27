import pathlib

import typer
from typing_extensions import Annotated

import conversion_calculator

app = typer.Typer()


@app.command()
def convert(
    input_file: str, output_file: str, force: Annotated[bool, "--force", "-f"] = False
):
    if not pathlib.Path(input_file).exists():
        raise typer.BadParameter(f"Input file {input_file} does not exist.")

    if pathlib.Path(output_file).exists() and not force:
        raise typer.BadParameter(f"Output file {output_file} already exists.")

    with open(input_file, "r") as f:
        try:
            converted_data = conversion_calculator.lib.convert_spreadsheet(
                conversion_calculator.lib.parse_input_csv(f)
            )
            with open(output_file, "w") as g:
                g.write(conversion_calculator.lib.dataframe_to_csv(converted_data))
        except Exception as e:
            raise typer.BadParameter(f"Error parsing input file: {e}")


def main():
    app()


if __name__ == "__main__":
    main()
