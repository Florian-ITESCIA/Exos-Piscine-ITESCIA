def enquete(name) :
    if name == 'Colonel Moutarde':
        adn = "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC"
    if name == 'Mlle Rose':
        adn = "CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG"
    if name == 'Mme Pervenche':
        adn = "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCC"
    if name == 'M. Leblanc':
        adn = "CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"
    if adn.find("CATA") >= 0 and adn.find("ATGC") >= 0 and adn.find("CATATGC") == -1 and adn.find("ATGCCATA") == -1:
        print(name + " est le coupable")
    else :
        print(name + ' est innocent')

enquete('Colonel Moutarde')
enquete('Mlle Rose')
enquete('Mme Pervenche')
enquete('M. Leblanc')