import sys
sys.path.append('D:\github\python')
from Cek_typo import cek_typo as ct
from Normalisasi_KBBI import normalisasi_kbbi as nkbi
from modulku import praproses as pps
from modulku import StemNstopW as stm
def praposes(a):
    #a = teks
    a = pps.preprocessing(a)
    a = pps.removePunc(a)
    a = ct.norm_typo(a)
    a = nkbi.norm_kbbi(a)
    a = stm.stemmer_kata(a)
    a = stm.stop_word(a)
    return a
def savek ():
    nkbi.save_gdiganti()
    ct.save_gdiganti()
    stm.save_kta()
def saves():
    stm.save_kta()
