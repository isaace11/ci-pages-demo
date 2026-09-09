from main import saludo

def test_saludo():
    # valor incorrecto a propósito para que pytest falle
    assert saludo() == "hola mundo" 