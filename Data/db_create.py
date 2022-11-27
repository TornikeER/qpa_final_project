
from os import path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data.db_tables import Dna, Rna, RnaCodon, AminoAcid
from Data.db_tables import Base
from Data.Tables import transcription_table, translation_table

ENGINE = create_engine('sqlite:///dataBase_for_task2.db')
SESSION = sessionmaker(ENGINE)


def create_database() -> None:
    if path.isfile('dataBase_for_task2.db'):
        return

    Base.metadata.create_all(ENGINE)
    with SESSION() as session:
        for nuke in transcription_table:
            rna_nuke = Rna(base_name=transcription_table[nuke])
            dna_nuke = Dna(base_name=nuke, child_rna=rna_nuke)
            session.add(dna_nuke)
        session.commit()

        for acid in translation_table:
            full_name = translation_table[acid]['full_name']
            new_acid = AminoAcid(acid_name=acid, acid_full_name=full_name)
            codons = translation_table[acid]['codons']
            for codon in codons:
                new_codon = RnaCodon(codon_name=codon, amino_acid=new_acid)
            session.add(new_codon)
        session.commit()

