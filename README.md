# conversion_calculator

A Python Shiny application that provides functions necessary to convert verbal learning scores.

## Overview

conversion_calculator provides models for things like Instruments, methods for processing csv templates, as well as some boilerplate to make it's use more simple in something like Shiny.

The calculator assumes that a user will provide a completed csv formatted similarly to the [example file](src/conversion_calculator/static/verbal-learning-template.csv) contained in the [static](src/conversion_calculator/static/) folder.  This template is returned by `#conversion_calculator.lib.get_csv_temlate_as_str` or `#conversion_calculator.lib.get_csv_template_as_io`.

Though I strongly recommend the use of the template to provide data to be converted, `#conversion_calculator.lib.convert_spreadsheet` will take any properly formatted CSV.

`#conversion_calculator.lib.convert_spreadsheet` will attempt to identify columns which conform to a pre-arranged structure, and when found, attempt to find other columns without values which could be 'crosswalked' to.

## Development

This is a [poetry](https://python-poetry.org/) based project, and assumes a recent python (3.9 or greater), and poetry 1.5

### Tests

Once python 3.9 or greater is installed, along with Poetry 1.5 or greater, you can run the tests with:

```bash
poetry run pytest
```

### Original Requirements

see [docs/original_requirements.md](docs/original_requirements.md) for the original requirements for this project.
