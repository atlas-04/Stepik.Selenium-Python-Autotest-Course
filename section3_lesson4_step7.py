import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("\n", "^_^", "\n")
    yield
    print("\n", ":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print("\n", ":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print("\n", ":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки
        pass
        
    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
        pass