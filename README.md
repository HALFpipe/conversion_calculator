# conversion_calculator

A Python Shiny application that provides functions necessary to convert verbal learning scores.

## Development notes

This is a [poetry](https://python-poetry.org/) based project, and assumes a recent python (3.9 or greater), and poetry 1.5

## Requirements

1. Accept and validate a completed [verbal learning template csv](src/conversion_calculator/static/verbal-learning-template.csv)
2. Return scores conversions for each column, based on the column name; (see 9. below)
3. Ignore unknown columns
4. Generate errors on unacceptable input data
   * any input that isn't in valid csv format
   * any input that contains no single matching column header
5. Generate a blank template on demand
6. Work with Shiny
7. a function which returns a text object containing the template
8. a function which returns a stream io object container the template
9. column names matching the default column format will be calculated.  Non-matching columns will be ignored
   * columns in scope match the regular expression 

      ```python
      r"^(cvlt|cvltc|ravlt|hvlt)_([a-z_])+$"
      ```
   * the column names shall be split on '_'
   * the total number of tokens after splitting on '_' determines what conversion to apply
      * matching column titles with four tokens
         1. instrument
         2. item
         3. trial
         4. value type
      * matching columns with three tokens
         1. instrument
         2. item
         3. value type
      * matching columns with two tokens
         1. instrument
         2. instrument metadata type
   * cvlt, cvltc, ravlt, hvlt are the instrument names
   * dr, imfr, sdcr, sdfr, ldfr, ldcr, recog, rep, int are the item names
   * t1, t2, t3, t4, t5, t13, t15, tb, b are the trial names
   * total, hits, c, i, fp are the value types
   * form, version are instrument metadata types
   * conditionals
      * if instrument is 'cvltc', ignore
      * if the item is in ['sdfr', 'ldfr']
      * if the trial isn't in ['totals', 't1', 't2', 't3', 't4', 't5', 'b']
10. a function which takes a string (matching the column formatting rules above), and returns a tuple of values representing the source value, and the desired target value, and raises an error on negative, non-integer, or out of range values.
11. a function which returns a text object containing the resulting converted data
12. a function which return a stream object containing the resulting converted data
13. a function which takes a text object, and returns a random sample of the converted dataset.