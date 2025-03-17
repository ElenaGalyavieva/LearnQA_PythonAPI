class TestEx10:
    def test_ex10(self):
        phrase = input("Set a phrase: ")
        x = 0
        for n in phrase:
            x = x + 1

        assert (x < 15), "Phrase has more simbols, than 15"