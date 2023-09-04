from conversion_calculator import crosswalks
from conversion_calculator import models

def test_crosswalks():
    assert crosswalks.cvlt_ldfr.instrument.id == "cvlt"

def test_cvlt_imfr():
    test_source_column = models.Column(column_name="cvlt_imfr", column_values=[1,2,3,4,5,6]) 
    
    ravlt_imfr_target_column = models.Column(column_name="ravlt_imfr")
    hvlt_imfr_target_column = models.Column(column_name="hvlt_imfr")
    assert crosswalks.cvlt_imfr.walk_possible(test_source_column, ravlt_imfr_target_column) == True
    assert crosswalks.cvlt_imfr.walk_possible(test_source_column, hvlt_imfr_target_column) == True
