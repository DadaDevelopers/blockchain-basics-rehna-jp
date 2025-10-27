import hashlib

# Your 4 transactions (TXIDs)
tx_hashes = [
    "71a8825eb1b87d1f65f48435473df489945ded4a44458e1a578f9083ba5ec080",  # t1
    "37c38986b885e2c4ad770b1e809ebe6e005872fda4c38377ed54fee6e04021ff",  # t2
    "3247bdccf3e5ef16aeb407871d782345e7530af5795a30d8ea9676184bb2f48e",  # t3
    "2b34030f8a1ef02b55a9c60c7a7946106e8f992208d4115f2e7b26cfbdb39c5c"   # t4
]

def double_sha256(b):
    """Perform Bitcoin-style double SHA-256 hashing."""
    return hashlib.sha256(hashlib.sha256(b).digest()).hexdigest()

# Level 1: Pairwise hashes
hash_ab = double_sha256(bytes.fromhex(tx_hashes[0]) + bytes.fromhex(tx_hashes[1]))
hash_cd = double_sha256(bytes.fromhex(tx_hashes[2]) + bytes.fromhex(tx_hashes[3]))

# Level 2: Merkle root
merkle_root = double_sha256(bytes.fromhex(hash_ab) + bytes.fromhex(hash_cd))

# Display ASCII Merkle tree
ascii_tree = f"""
                  Merkle Root
                       |
                {merkle_root[:16]}...
                       |
           +-----------+-----------+
           |                       |
   {hash_ab[:16]}...           {hash_cd[:16]}...
           |                       |
      +----+----+             +----+----+
      |         |             |         |
  t1 {tx_hashes[0][:8]}... t2 {tx_hashes[1][:8]}... t3 {tx_hashes[2][:8]}... t4 {tx_hashes[3][:8]}...
"""

print(ascii_tree)

print("Hash(t0+t1):", hash_ab)
print("Hash(t2+t3):", hash_cd)
print("Merkle Root:", merkle_root)
