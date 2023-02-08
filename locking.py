import base58
import hashlib
import ripemd160

def p2sh_lock(script:str) -> str:
    script_hash_sha256 = hashlib.sha256(script).digest()
    script_hash_ripemd160 = ripemd160.ripemd160(script_hash_sha256)
    p2sh = bytes([0x05]) + script_hash_ripemd160
    p2sh = p2sh + hashlib.sha256(hashlib.sha256(p2sh).digest()).digest()[:4]
    p2sh = base58.b58encode(p2sh)
    return p2sh.decode()


#script = bytes.fromhex("522103fc40d00ba42d7082fa9c76f90a7aa6a6f2656e5acb25d5c08fccf51dbf64b1ff2102b8e771b814a264690641329a89f2080e4967454331c95e0b54c3c041a9dec90021037f99844861ea8b70a3ac13047f74308fb8479d14ff60e115b89efb566f1f0ae353ae")
#print(p2sh_lock(script))