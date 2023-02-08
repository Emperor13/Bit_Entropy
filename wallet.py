from embit.descriptor import Descriptor
from embit.networks import NETWORKS
from embit import bip39, bip32, ec
from binascii import hexlify
import os

'''
ความยาว Entropy เริ่มต้น (128-256bits) : ENT
ความยาว checksum : CS
ความยาวของประโยคช่วยจำ : MS

CS = ENT / 32
MS = (ENT + CS) / 11
'''
'''
#  entropy = bytes(random.getrandbits(8) for i in range(16))
#  print("Entropy: " + str(entropy))
'''
print('[ HD Wallet!! ]')


def build(cal):
    if cal == 0 or cal == 1 or cal == 2 or cal == 3 or cal == 4:
        length = BITS[cal]
        length_binary = BITS[cal]
        print()
        entropy_2 = os.urandom(length // 8)
        mnemonic = bip39.mnemonic_from_bytes(entropy_2)
        # mnemonic = "super choice radio shuffle glimpse copper pipe burger scorpion share gossip certain"
        seed = bip39.mnemonic_to_seed(mnemonic)

        xprv = bip32.HDKey.from_seed(seed, version=NETWORKS["main"]["xprv"])
        zprv = bip32.HDKey.from_seed(seed, version=NETWORKS["main"]["zprv"])
        yprv = bip32.HDKey.from_seed(seed, version=NETWORKS["main"]["yprv"])  # xprv, zprv, yprv
            

        pieces = mnemonic.split(' ')
        word = []
        for piece in pieces:
            word.append(piece)

        print("Mnemonic: [ {} ]".format(mnemonic))
        print('\t└── {} Word, {} Bits'.format(len(word), length))
        ln()

        # root private key
        print("[Master Private Key] \n\t├── " + str(xprv))
        print('\t├── %s' % zprv)
        print('\t└── %s' % yprv)

        print()
        xpub = xprv.derive("m/84h/0h/0h").to_public()
        zpub = zprv.derive("m/84h/0h/0h").to_public()
        ypub = yprv.derive("m/84h/0h/0h").to_public()

        print("[Master Public Key] \n\t├── %s" % xpub)
        print('\t├── %s' % zpub)
        print('\t└── %s' % ypub)

        ln()
        locking_script = ["sh", "wpkh", "tr"]
        addr_type = locking_script[1]
        desc = Descriptor.from_string(
            "%s([%s/84h/0h/0h]%s/{0,1}/*)" % (addr_type, hexlify(yprv.my_fingerprint).decode(), xpub))

        print('\t\t[address p2{}]'.format(addr_type))
        for i in range(5):
            print('\t', '-' * 50)
            print('\t', i + 1, "| ", desc.derive(i).address())

            # pubkey = ec.PrivateKey.sec(xpub)
    else:
        print()
        ln()
        print('\t\t[Not in option!!]')


def ln():
    print()
    print('────' * 30, '\n')


if __name__ == "__main__":
    BITS = [128, 160, 192, 224, 256]
    index = 1
    for i in range(5):
        # while True:
        ln()
        Select = input(
            'select | [1] 12word | [2] 15word | [3] 18word | [4] 21word | [5] 24word |: ')
        if Select == 'e' or Select == 'E':
            print()
            ln()
            print('\t\t[Stop!!]')
            break
        Result = int(Select)-index
        build(int(Result))
