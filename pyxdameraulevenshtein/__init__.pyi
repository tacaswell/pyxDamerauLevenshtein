from typing import Sequence, Any, List

def damerau_levenshtein_distance(seq1: Sequence[Any], seq2: Sequence[Any]) -> int: ...
def normalized_damerau_levenshtein_distance(seq1: Sequence[Any], seq2: Sequence[Any]) -> float: ...
def damerau_levenshtein_distance_seqs(seq: Sequence[Any], seqs: Sequence[Sequence[Any]]) -> List[int]: ...
def normalized_damerau_levenshtein_distance_seqs(seq: Sequence[Any], seqs: Sequence[Sequence[Any]]) -> List[float]: ...