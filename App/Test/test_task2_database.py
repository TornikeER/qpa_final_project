import unittest

from Script_task2 import convert_dna_to_rna, convert_rna_to_protein


class DatabaseTest(unittest.TestCase):
    def test_convert_dna_to_rna(self):
        self.assertEqual(convert_dna_to_rna('ATTTGGCTACTAACAATCTA'), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(convert_dna_to_rna('GTTGTAATGGCCTACATTA'), 'GUUGUAAUGGCCUACAUUA')
        self.assertEqual(convert_dna_to_rna('CAGGTGGTGTTGTTCAGTT'), 'CAGGUGGUGUUGUUCAGUU')
        self.assertEqual(convert_dna_to_rna('GCTAACTAAC'), 'GCUAACUAAC')
        self.assertEqual(convert_dna_to_rna('GCTAACTAACATCTTTGGCACTGTT'), 'GCUAACUAACAUCUUUGGCACUGUU')
        self.assertEqual(convert_dna_to_rna('TATGAAAAACTCAAA'), 'UAUGAAAAACUCAAA')
        self.assertEqual(convert_dna_to_rna('CCCGTCCTTGATTGGCTTGAAGAGAAGTTT'), 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU')

    def test_convert_rna_to_protein(self):
        self.assertEqual(convert_rna_to_protein('AUUUGGCUACUAACAAUCUA'), 'IWLLTI')
        self.assertEqual(convert_rna_to_protein('GUUGUAAUGGCCUACAUUA'), 'VVMAYI')
        self.assertEqual(convert_rna_to_protein('CAGGUGGUGUUGUUCAGUU'), 'QVVLFS')
        self.assertEqual(convert_rna_to_protein('GCUAACUAAC'), 'AN*')
        self.assertEqual(convert_rna_to_protein('GCUAACUAACAUCUUUGGCACUGUU'), 'AN*HLWHC')
        self.assertEqual(convert_rna_to_protein('UAUGAAAAACUCAAA'), 'YEKLK')
        self.assertEqual(
            convert_rna_to_protein('CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'), 'PVLDWLEEKF')


if __name__ == '__main__':
    unittest.main()


# if __name__ == '__main__':
#     create_database()