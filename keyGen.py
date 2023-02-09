from embit.descriptor import Descriptor
from embit import bip39, bip32
from binascii import hexlify
import os

def key12():
    entropy_2 = os.urandom(128 // 8)
    mnemonic = bip39.mnemonic_from_bytes(entropy_2)
    #print('Mnemonic 12word : %s'% mnemonic)
    return mnemonic

def key15():
    entropy_2 = os.urandom(160 // 8)
    mnemonic = bip39.mnemonic_from_bytes(entropy_2)
    print('Mnemonic 15word : %s'% mnemonic)
    return mnemonic


def key18():
    entropy_2 = os.urandom(192 // 8)
    mnemonic = bip39.mnemonic_from_bytes(entropy_2)
    print('Mnemonic 18word : %s'% mnemonic)
    return mnemonic


def key21():
    entropy_2 = os.urandom(224 // 8)
    mnemonic = bip39.mnemonic_from_bytes(entropy_2)
    print('Mnemonic 21word : %s'% mnemonic)
    return mnemonic



def key24():
    entropy_2 = os.urandom(256 // 8)
    mnemonic = bip39.mnemonic_from_bytes(entropy_2)
    print('Mnemonic 24word : %s'% mnemonic)
    return mnemonic

'''
seed = b'discover carbon material cradle margin jacket alley divorce display address face diamond butter impose property slogan rural wrap remind sport draw protect mechanic betray'

root = bip32.HDKey.from_seed(seed)
print("[Master Private Key] \n\t└── %s"%root)

print()
xpub = root.derive("m/84h/0h/0h").to_public()
print("[Master Public Key] \n\t└── %s"%xpub)
'''
