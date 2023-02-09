import re
import hashlib
import ripemd160
import base58

'''  OP_CODE  '''
OP_1 = 0x51
OP_2 = 0x52
OP_3 = 0x53
OP_CHECKMULTISIG = 0xae

def locking_script(redeem_script) -> str:
    redeem_script = redeem_script
    SHA256 = hashlib.sha256(redeem_script).digest()
    RIPEMD160 = ripemd160.ripemd160(SHA256)
    p2sh = bytes([0x05]) + RIPEMD160
    p2sh = p2sh + hashlib.sha256(hashlib.sha256(p2sh).digest()).digest()[:4]
    p2sh = base58.b58encode(p2sh)
    locking = p2sh.decode()
    return locking

def check_format(item:str) -> bool:
    if re.match("^[a-fA-F0-9]{64}$", item):
        return True
    else:
        return False

def check_public_key(public_key) -> bool:
    if len(public_key) == 66:
        if public_key[0:2] == "02":
            return True
    if len(public_key) == 66:
        if public_key[0:2] == "03":
            return True
    elif len(public_key) == 130:
        if public_key[0:2] == "04":
            return True
    elif len(public_key) == 64:
        if int(public_key[0:2], 16) in [2, 3]:
            return True
    return False


def multisig_3of3(pubkey=[]) -> str:
    pubkey1 = bytes.fromhex(pubkey[0])
    pubkey2 = bytes.fromhex(pubkey[1])
    pubkey3 = bytes.fromhex(pubkey[2])

    REDEEM_SCRIPT = (
            bytes([OP_3]) +
            len(pubkey1).to_bytes(1, 'big') + pubkey1 +
            len(pubkey2).to_bytes(1, 'big') + pubkey2 +
            len(pubkey3).to_bytes(1, 'big') + pubkey3 +
            bytes([OP_3, OP_CHECKMULTISIG])
    )
    script = REDEEM_SCRIPT
    return script

def multisig_2of3(pubkey=[]) -> str:
    pubkey1 = bytes.fromhex(pubkey[0])
    pubkey2 = bytes.fromhex(pubkey[1])
    pubkey3 = bytes.fromhex(pubkey[2])

    REDEEM_SCRIPT = (
            bytes([OP_2]) +
            len(pubkey1).to_bytes(1, 'big') + pubkey1 +
            len(pubkey2).to_bytes(1, 'big') + pubkey2 +
            len(pubkey3).to_bytes(1, 'big') + pubkey3 +
            bytes([OP_3, OP_CHECKMULTISIG])
    )
    script = REDEEM_SCRIPT
    return script

def multisig_1of3(pubkey=[]) -> str:
    pubkey1 = bytes.fromhex(pubkey[0])
    pubkey2 = bytes.fromhex(pubkey[1])
    pubkey3 = bytes.fromhex(pubkey[2])

    REDEEM_SCRIPT = (
            bytes([OP_1]) +
            len(pubkey1).to_bytes(1, 'big') + pubkey1 +
            len(pubkey2).to_bytes(1, 'big') + pubkey2 +
            len(pubkey3).to_bytes(1, 'big') + pubkey3 +
            bytes([OP_3, OP_CHECKMULTISIG])
    )
    script = REDEEM_SCRIPT
    return script


#if __name__ == "__main__":
for i in range(3):
    keys_stored = []
    print()
    n_sig = int(input("Enter the Signatures required for unlock: "))

    key = int(input('Enter the keys to create MultiSig: '))

    if n_sig == 1 and key == 3:
        for i in range(3):
            print()
            keys = input('Enter your public key: ')

            if check_public_key(keys) == True and check_format(keys[2:]) == True:
                print("Valid public key format %s" % keys)
                keys_stored.append(keys)
            else:
                print("Invalid public key format!!")
        Raw_Redeem_Script = multisig_1of3(keys_stored)
        Redeem_Script = Raw_Redeem_Script.hex()

        Locking_Script = locking_script(Raw_Redeem_Script)
        print('\n'
              'Redeem Script: %s' % Redeem_Script)
        print('Locking Script %s ' % Locking_Script)

    elif n_sig == 2 and key == 3:
        for i in range(3):
            print()
            keys = input('Enter your public key: ')

            if check_public_key(keys) == True and check_format(keys[2:]) == True:
                print("Valid public key format %s" % keys)
                keys_stored.append(keys)
            else:
                print("Invalid public key format!!")
        Raw_Redeem_Script = multisig_2of3(keys_stored)
        Redeem_Script = Raw_Redeem_Script.hex()

        Locking_Script = locking_script(Raw_Redeem_Script)
        print('\n'
              'Redeem Script: %s' % Redeem_Script)
        print('Locking Script %s ' % Locking_Script)

    elif n_sig == 3 and key == 3:
        for i in range(3):
            print()
            keys = input('Enter your public key: ')

            if check_public_key(keys) == True and check_format(keys[2:]) == True:
                print("Valid public key format %s" % keys)
                keys_stored.append(keys)
            else:
                print("Invalid public key format!!")
        Raw_Redeem_Script = multisig_3of3(keys_stored)
        Redeem_Script = Raw_Redeem_Script.hex()

        Locking_Script = locking_script(Raw_Redeem_Script)
        print('\n'
              'Redeem Script: %s' % Redeem_Script)
        print('Locking Script %s ' % Locking_Script)

    else:
        print('Not in option!!')