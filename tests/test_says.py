from ptravis import says


def test_say_hello():
    assert "hello" == says.say_hello()

def test_say_helloworld():
    assert "helloworld" == says.say_helloworld()