import conversion_calculator
import io
import shinyswatch
from shiny import App, render, ui, reactive
from typing import List


app_ui = ui.page_fluid(
    shinyswatch.theme.superhero(),
    ui.download_button("download_template", "Download Template"),
    ui.input_file("file1", "Choose a file to upload for conversion:", multiple=True),
    ui.output_table("file_content"),
    ui.download_button("download_conversion", "Download Conversion"),
)

def server(input, output, session):
    MAX_SIZE = 50000

    @session.download(filename="template.csv")
    def download_template():
        return conversion_calculator.lib.get_csv_template_path()

    @output
    @render.table
    def file_content():
        file_infos = input.file1()
        if not file_infos:
            return

        if len(file_infos) > 1:
            return
        
        return conversion_calculator.lib.parse_input_csv(file_infos[0]['datapath'])
    
    # the following, from here to the end of the server function, doesn't work; it's the part of this which actually does the conversion
    @reactive.Calc
    def run_conversion():
        file_infos = input.file1() 
        return conversion_calculator.lib.convert_spreadsheet(conversion_calculator.lib.parse_input_csv(file_infos[0]['datapath']))

    @session.download(filename="converted.csv")
    def download_conversion():
        file_infos = input.file1()
        if not file_infos:
            return

        if len(file_infos) > 1:
            return

        try:
#            input_df = conversion_calculator.lib.parse_input_csv(file_infos[0]['datapath'])
#            converted_df = conversion_calculator.lib.convert_spreadsheet(input_df)
             return io.BytesIO(conversion_calculator.lib.dataframe_to_csv(run_conversion()).encode('utf-8'))
        except Exception as e:
            return io.BytesIO(str(e).encode('utf-8'))

app = App(app_ui, server)
