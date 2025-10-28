
                              ┌──────────────────────────────────────────────┐
                              │               Merkle Root                   │
                              │            Hash of (H12 + H34)               |         
                              └──────────────────────────────────────────────┘
                                             ▲
                                             │
                ┌────────────────────────────┴────────────────────────────┐
                │                                                         │
      ┌────────────────────────────┐                       ┌────────────────────────────┐
      │         H12                │                       │           H34              │
      │   Hash of (Tx1 + Tx2)      │                       │   Hash of (Tx3 + Tx4)      │
      └────────────────────────────┘                       └────────────────────────────┘
                ▲                                                         ▲
                │                                                         │
      ┌─────────┴──────────┐                                 ┌────────────┴──────────┐
      │                    │                                 │                       │
┌────────────┐     ┌────────────┐                  ┌────────────┐           ┌────────────┐
│   Tx1      │     │   Tx2      │                  │   Tx3      │           │   Tx4      │
│ hash1      │     │ hash2      │                  │ hash3      │           │ hash4      │
└────────────┘     └────────────┘                  └────────────┘           └────────────┘
Level 1 — Transactions (Leaves):
These are your original transactions (t1, t2, t3, t4).

Each hash uniquely identifies a transaction.

Level 2 — First Hash Layer:
Combine pairs of transactions and hash them using double SHA-256.

Hash(t1+t2) and Hash(t3+t4) summarize the integrity of their respective pairs.

Any change in a transaction alters the hash.

Level 3 — Merkle Root:
Combine the Level 1 hashes and double SHA-256 again.

The result is the Merkle root, representing all transactions in the block.

This root goes into the block header and ensures the block’s integrity.