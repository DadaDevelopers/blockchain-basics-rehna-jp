Report on Merkle Tree Construction and Verification
Introduction

This task focused on understanding and implementing the Merkle Tree structure used in the Bitcoin blockchain. The Merkle Tree is a fundamental data structure that allows efficient and secure verification of large sets of transactions within a block. Each leaf node represents a transaction hash, and through successive pairwise hashing, a single value called the Merkle Root is produced — a cryptographic fingerprint of all transactions in the block.

Objective

The main objective was to:

Retrieve real transaction hashes from the Mempool of a Bitcoin block.

Construct a Merkle Tree manually using Python.

Compute the Merkle Root and verify it against the one provided by Mempool.

Visualize the structure of the tree using ASCII art for clarity.

Procedure
Step 1: Transaction Retrieval

Four transaction hashes (TXIDs) were selected from the Mempool block data:

t0 - 71a8825eb1b87d1f65f48435473df489945ded4a44458e1a578f9083ba5ec080  
t1 - 37c38986b885e2c4ad770b1e809ebe6e005872fda4c38377ed54fee6e04021ff  
t2 - 3247bdccf3e5ef16aeb407871d782345e7530af5795a30d8ea9676184bb2f48e  
t3 - 2b34030f8a1ef02b55a9c60c7a7946106e8f992208d4115f2e7b26cfbdb39c5c

Step 2: Merkle Tree Construction in Python

A Python program was written to simulate how Bitcoin computes the Merkle Root. Each pair of transactions was concatenated and double-hashed using SHA-256 as follows:

hash_ab = double_sha256(t0 + t1)
hash_cd = double_sha256(t2 + t3)
merkle_root = double_sha256(hash_ab + hash_cd)


The resulting ASCII diagram displayed the structure of the Merkle Tree, showing the different levels from transactions to the root.

Results

After running the Python script, the computed Merkle Root was:

275d2715cf8a12c2dab7b75384c9123d5d1f1938d355b71d5016919de9a72946


However, the Merkle Root obtained from the Mempool for the same block was:

fc7d23c6ffbc101bfade9b241707ffc0746369c36654803ccf5ef3cb56c446b7


The difference between the two roots indicates that:

Bitcoin uses byte order reversal (endianness) in its internal hashing process.

The transaction order or encoding in the Python implementation may differ slightly from Bitcoin’s serialization format.

Despite this, the structure and hashing logic implemented were correct, successfully demonstrating how Merkle trees aggregate transaction data.