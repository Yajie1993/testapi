import pytest

# @pytest.mark.usefixtures("my_fixture11")
@pytest.mark.smoke
def test_01():
    print('this is test')

class TestA:
    # def test_01(self,my_fixture11):
    #     print('this is a test')
    #     print(my_fixture11)

    @pytest.mark.parametrize("a",[1,2])
    @pytest.mark.parametrize("b", [3,4])
    def test_02(self,a,b):
        print(a+b)
    @pytest.mark.demo
    def test_03(self):
        print('this is c test')
        assert False