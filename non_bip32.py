from embit import ec
import hashlib
import base58
import os

def create_wif(private_key_hex:str) -> str:
    private_key_bytes = bytes.fromhex(private_key_hex)
    version = b'\x80'
    extended_key = version + private_key_bytes
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    wif = base58.b58encode(extended_key + checksum)
    return wif.decode('utf-8')

def set_format(item:str) -> str:
    Frist = item[:15]
    Last = item[-15:]
    result = Frist + "........." + Last
    return result

def random_entropy():
    entropy = os.urandom(99999)
    entropy = int.from_bytes(entropy, byteorder='big')
    private_key = hashlib.sha256(str(entropy).encode()).hexdigest()
    return private_key

def main():
    Entropy = random_entropy()
    wif = create_wif(Entropy)
    print("Private Key: ", wif)
    prv = ec.PrivateKey.from_wif(wif)
    pub = prv.get_public_key()
    print('Public Key: %s' % pub,'\n')
    print(set_format(str(prv)))
    print(set_format(str(pub)))

if __name__ == "__main__":
    main()
