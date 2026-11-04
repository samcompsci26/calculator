from calculator import add,subtract,multiply,divide

def test_add(): #arrange is 2,3 being input, act and assert are being combined into one line on the function
    assert add(2,3) == 5

def test_subtract():
    assert subtract(7,3) == 4 #7-3

def test_multiply():
    assert multiply(2,3) == 6 #2*3

def test_divide():
    assert divide(15,3) == 5 #15/3

def test_divide_uneven():
    #arrange
    a,b = 11,2
    #act
    result = divide(a,b)
    #assert
    assert result == 5.5
