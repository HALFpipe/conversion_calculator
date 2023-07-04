import conversion_calculator
import io
import shinyswatch
from shiny import App, render, ui, reactive
from typing import List


app_ui = ui.page_fluid(
    shinyswatch.theme.superhero(),
    ui.input_file("file1", "Choose a file to upload:", multiple=True),
    ui.output_table("file_content"),
    ui.download_button("download_conversion", "Download Conversion"),
)

def server(input, output, session):
    MAX_SIZE = 50000

    @output
    @render.table
    def file_content():
        file_infos = input.file1()
        if not file_infos:
            return

        if len(file_infos) > 1:
            return
        
        return conversion_calculator.lib.parse_input_csv(file_infos[0]['datapath'])
    
    @session.download()
    def download_conversion():
        file_infos = input.file1()
        if not file_infos:
            return

        if len(file_infos) > 1:
            return

        input_df = conversion_calculator.lib.parse_input_csv(file_infos[0]['datapath'])
        converted_df = conversion_calculator.lib.convert_spreadsheet(input_df)
        return io.BytesIO(conversion_calculator.lib.dataframe_to_csv(converted_df).encode('utf-8'))

app = App(app_ui, server)
