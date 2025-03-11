
from choH import choH
from choH.utils.testutils import csv_column_to_list


def test_min_val_data_set_1() :
    assert 5 == 5

def test_min_val_data_set_2() :
    assert 4 == 5

def test_min_val_data_set_3() :
    X = [float(x for x in csv_column_to_list("test.data.csv",0)]
    score = choH(X)
    assert 5 == 5




    

# -12.162452676414286    
