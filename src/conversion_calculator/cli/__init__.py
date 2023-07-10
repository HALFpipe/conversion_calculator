import typer
import pathlib

app = typer.Typer()

@app.command()
def convert(input_file: str, output_file: str):
    typer.echo(f"Not implemented yet")

def main():
    app()

if __name__ == '__main__':
    main()
