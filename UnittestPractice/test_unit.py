import unittest as ut
from cap import captext

class Test(ut.TestCase):
    
    def test_one_Word_str(self):
        text = 'python'
        finalstr = captext(text)
        self.assertEqual(finalstr,'Python')
    
    def test_multiple_word(self):
        text = 'megha marwah'
        finalstr = captext(text)
        self.assertEqual(finalstr,'Megha Marwah')

if __name__ == '__main__':
    ut.main()