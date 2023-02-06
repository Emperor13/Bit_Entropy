from embit.descriptor import Descriptor
from embit.networks import NETWORKS
from embit import bip39, bip32
from binascii import hexlify
import os
def recovery_from_master_key(master_pubkey: str, type:int) -> str:
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