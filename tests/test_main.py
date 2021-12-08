from .. import helloworld

class Test_App():
    def test_app(self,define_string,capsys):
        assert define_string=="Hello World\n"
        helloworld.work()
        stdout,stderr = capsys.readouterr()
        assert define_string == stdout