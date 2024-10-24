(* Import the necessary libraries for arithmetic *)
Require Import Coq.Arith.Arith.
Require Import Coq.Arith.PeanoNat.

(* Declare the cardinality values as parameters *)
Variable nA : nat.
Variable nB : nat.
Variable nA_inter_B : nat.

(* Define the cardinality of the union of A and B *)
Definition nA_union_B := nA + nB - nA_inter_B.

(* Prove that the definition of nA_union_B is correct *)
Theorem calculate_nA_union_B :
  nA_union_B = nA + nB - nA_inter_B.
Proof.
  (* Since the definition is straightforward, the proof is immediate *)
  reflexivity.
Qed.