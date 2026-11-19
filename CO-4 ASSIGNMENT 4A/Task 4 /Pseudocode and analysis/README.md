Task 4 – Pseudocode Forensics: Word Break

1. Locate the defect The original algorithm checks only whether substring(Text, j, i) is in the dictionary. It does not check whether the prefix ending at position j can already be segmented. A dictionary word at the end of an invalid prefix must not make the whole prefix valid. The missing condition is DP[j] = TRUE.

2. Failing input and trace Text: abc Dictionary: { "bc" } The complete string abc cannot be segmented because a is not covered by any dictionary word. Correct initial state: DP[0] = TRUE. At i = 1, no valid dictionary word ends at position 1. Therefore DP[1] = FALSE. At i = 2, no valid dictionary word can be reached from a TRUE prefix. Therefore DP[2] = FALSE. At i = 3, the original algorithm finds substring Text[1..3] = "bc" in the dictionary and sets DP[3] = TRUE without checking DP[1]. This is the first incorrect state. The corrected algorithm checks DP[1] = TRUE as well. Since it is FALSE, it does not accept "bc" and leaves DP[3] = FALSE. Thus, the faulty algorithm returns TRUE, while the correct answer is FALSE.

3. Minimal correction IF DP[j] = TRUE AND substring(Text, j, i) is in Dictionary THEN DP[i] <- TRUE BREAK END IF

4. Regression check Text: apple Dictionary: { "app", "le", "apple" } Trace: DP[0] = TRUE. DP[3] = TRUE because "app" is a dictionary word and starts at reachable boundary 0. DP[5] = TRUE because "le" is a dictionary word and DP[3] = TRUE. Both the original and corrected algorithms return TRUE for this valid segmentation.

5.Corrected pseudocode ALGORITHM WordBreak(Text, Dictionary) BEGIN n <- LENGTH(Text) DP[0] <- TRUE FOR i <- 1 TO n DO DP[i] <- FALSE FOR j <- 0 TO i-1 DO IF DP[j] = TRUE AND substring(Text, j, i) is in Dictionary THEN DP[i] <- TRUE BREAK END IF END FOR END FOR RETURN DP[n] END

6. Complexity There are O(n^2) pairs of positions. With constant-time dictionary lookup and substring handling, time is O(n^2); DP storage is O(n). Actual substring construction may add copying cost depending on the implementation.
