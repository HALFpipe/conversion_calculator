import pandas as pd
import shinyswatch
from shiny import App, render, ui

app_ui = ui.page_navbar(
    # Available themes:
    #  cerulean, cosmo, cyborg, darkly, flatly, journal, litera, lumen, lux,
    #  materia, minty, morph, pulse, quartz, sandstone, simplex, sketchy, slate,
    #  solar, spacelab, superhero, united, vapor, yeti, zephyr
    # shinyswatch.theme.pulse(),
    shinyswatch.theme.superhero(),
    ui.nav(
        "",
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.input_file("file", "File input:"),
                ui.tags.h5("Upload file"),
                ui.input_action_button("action", "Upload", class_="btn-primary"),
            ),
            ui.panel_main(
                ui.navset_tab(
                    ui.nav(
                        "Tab 1",
                        ui.tags.h4("Table"),
                        ui.output_table("table"),
                        ui.tags.h4("Verbatim text output"),
                        ui.output_text_verbatim("txtout"),
                        ui.tags.h1("Header 1"),
                        ui.tags.h2("Header 2"),
                        ui.tags.h3("Header 3"),
                        ui.tags.h4("Header 4"),
                        ui.tags.h5("Header 5"),
                    ),
                    ui.nav("Tab 2"),
                    ui.nav("Tab 3"),
                )
            ),
        ),
    ),
    title="Conversion Calculator",
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)
