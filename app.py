import conversion_calculator
import shinyswatch
from shiny import App, render, ui, reactive


def ui_card(title, *args):
    return (
        ui.div(
            {"class": "card mb-4"},
            ui.div(title, class_="card-header"),
            ui.div({"class": "card-body"}, *args),
        ),
    )


app_ui = ui.page_fluid(
    shinyswatch.theme.superhero(),
    ui_card(
        "Download the verbal learning template",
        ui.download_button("verbal_learning_download_button", "Download CSV"),
    ),
    ui_panel_conditional(
        "download_converted_csv", "input.csv_convert",
        ui.download_button("csv_convert", "Download CSV"),
    ),
    ui_card(
        "Convert a complete verbal learning template",
        ui.input_file("csv_convert", "File input:"),
    ),
    title="Conversion Calculator",
)


def server(input, output, session):
    MAX_FILE_SIZE = 1000000

    @session.download()
    def verbal_learning_download_button():
        return conversion_calculator.lib.get_csv_template_path()

    @session.download()
    def csv_convert(input_csv):
        if not input_csv:
            return

        input_df = conversion_calculator.lib.parse_input_csv(input_csv)
        converted_df = conversion_calculator.lib.convert_spreadsheet(input_df)
        return conversion_calculator.lib.dataframe_to_csv(converted_df)


app = App(app_ui, server)
