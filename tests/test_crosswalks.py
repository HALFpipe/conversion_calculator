import pandas as pd
from conversion_calculator import crosswalks
from conversion_calculator import models
from conversion_calculator.lib import convert_all_values

def test_crosswalks():
    assert crosswalks.cvlt_ldfr_c.instrument.id == "cvlt"

def test_cvlt_imfr_c():
    test_source_column = models.Column(column_name="cvlt_imfr_c", column_values=[1,2,3,4,5,6]) 
    ravlt_target_values = pd.DataFrame({"ravlt_imfr_c": [2,2,3,4,5,6]})
    hvlt_target_values = pd.DataFrame({"hvlt_imfr_c": [3,3,4,5,5,6]})

    ravlt_imfr_target_column = models.Column(column_name="ravlt_imfr_c")
    hvlt_imfr_target_column = models.Column(column_name="hvlt_imfr_c")

    assert crosswalks.cvlt_imfr_c.walk_possible(test_source_column, ravlt_imfr_target_column) == True
    assert crosswalks.cvlt_imfr_c.walk_possible(test_source_column, hvlt_imfr_target_column) == True

    assert convert_all_values(test_source_column, ravlt_imfr_target_column).equals(ravlt_target_values)
    assert convert_all_values(test_source_column, hvlt_imfr_target_column).equals(hvlt_target_values)

