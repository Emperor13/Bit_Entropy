from embit.descriptor import Descriptor
from embit.networks import NETWORKS
from embit import bip39, bip32
from binascii import hexlify
import os

'''

[Input] -> recovery_from_master_Publickey()
recovery_from_master_Publickey(master public key, format locking script)
master public ke = zpub6s6Gs9A8GHDt8DPWHtQWFWntDYzHT66zYwSnLfVWgbzHnNPu8i3xFjeSy1i8CakiQZvt1f5dVEjtrdFqu1TZQ7X8LEdyKHLMzbAxNsRtzBe

format locking script:
format [0] = p2pkh 19daR8JQw4XUvYepCS42CThseG3C1a7wSU
format [1] = bc1qt647qz8f8lxg80kktfveqnzlvjnqpmc4k9wcw8
format [1] = bc1p5w4kwyycqrkk8x52h784rvpxgu42q9rfrnlftqd7ea0z8leanfaqmtn6uj


[Output] -> recovery_from_master_Publickey()



'''
def recovery_from_master_Publickey(master_pubkey: str, type:int) -> str:
    entropy_2 = os.urandom(128 // 8)
    mnemonic = bip39.mnemonic_from_bytes(entropy_2)
    seed = bip39.mnemonic_to_seed(mnemonic)
    root = bip32.HDKey.from_seed(seed, version=NETWORKS["main"]["zprv"])

    xpub = master_pubkey
    locking_script = ["pkh", "wpkh", "tr"]
    addr_type = locking_script[type]
    desc = Descriptor.from_string("%s([%s/84h/0h/0h]%s/{0,1}/*)" % (addr_type, hexlify(root.my_fingerprint).decode(), xpub))

    store = []
    for i in range(3):
        result = desc.derive(i).address()
        store.append(result)
    return store


def recovery_from_seed(seed_phrase:str, type:int) -> str:
    mnemonic = seed_phrase
    seed = bip39.mnemonic_to_seed(mnemonic)

    root = bip32.HDKey.from_seed(seed, version=NETWORKS["main"]["zprv"])
    xpub = root.derive("m/84h/0h/0h").to_public()

    locking_script = ["pkh", "wpkh", "tr"]
    addr_type = locking_script[type]
    desc = Descriptor.from_string("%s([%s/84h/0h/0h]%s/{0,1}/*)" % (addr_type, hexlify(root.my_fingerprint).decode(), xpub))

    store = []
    for i in range(3):
        result = desc.derive(i).address()
        store.append(result)
    return store


def create_masterkey_from_seed(seed_phrase:str) -> str:

    mnemonic = seed_phrase
    seed = bip39.mnemonic_to_seed(mnemonic)

    xprv = bip32.HDKey.from_seed(seed, version=NETWORKS["main"]["xprv"])
    zprv = bip32.HDKey.from_seed(seed, version=NETWORKS["main"]["zprv"])
    yprv = bip32.HDKey.from_seed(seed, version=NETWORKS["main"]["yprv"])  # xprv, zprv, yprv

    xpub = xprv.derive("m/84h/0h/0h").to_public()
    zpub = zprv.derive("m/84h/0h/0h").to_public()
    ypub = yprv.derive("m/84h/0h/0h").to_public()

    master_private_key = [xprv, zprv, yprv]
    master_public_key = [xpub, zpub, ypub]
        
    return master_private_key, master_public_key

