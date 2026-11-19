Task 1 – Algorithm Design Review: Fractional Knapsack

1.Problem analysis A delivery vehicle has a fixed capacity. Every package has a weight and value. Packages may be divided, so this is the Fractional Knapsack problem. Input: vehicle capacity W; package weights weight[i] and values value[i]. Output: fraction of each package loaded and maximum total value. Objective: maximise total value without exceeding capacity. Constraint: 0 <= fraction[i] <= 1 and total loaded weight <= W.

2.Deficiencies in the proposed pseudocode “Arrange packages” does not state the sorting criterion. “Select the best package” does not define what best means. The algorithm does not validate that weights are positive or that values are valid. It does not state how to handle a package that is heavier than the remaining capacity. It does not calculate the fraction of a package that can fit. Remaining capacity is not updated explicitly. The stopping condition and result construction are unclear. The output does not identify which packages or fractions were selected.

3.Greedy rule Calculate value / weight for every package and consider packages in descending order of this ratio. Take a complete package when it fits; otherwise take only the fraction that fits and stop.

4.Corrected pseudocode ALGORITHM FractionalKnapsack(W, Packages) INPUT: Capacity W; each package has ID, weight, value OUTPUT: Selected fractions and maximum total value

BEGIN FOR each package p in Packages DO IF p.weight <= 0 THEN RETURN "Invalid package weight" END IF p.ratio <- p.value / p.weight END FOR

SORT Packages by ratio in descending order
remaining <- W
totalValue <- 0
selected <- empty list

FOR each package p in Packages DO
    IF remaining = 0 THEN
        BREAK
    END IF

    IF p.weight <= remaining THEN
        fraction <- 1
        remaining <- remaining - p.weight
        totalValue <- totalValue + p.value
    ELSE
        fraction <- remaining / p.weight
        totalValue <- totalValue + fraction * p.value
        remaining <- 0
    END IF

    APPEND (p.ID, fraction) to selected
END FOR
RETURN selected, totalValue
END

5. Sample manual trace Illustrative input (the assignment does not provide package values): Capacity = 50 kg. Package Weight (kg) Value Value/Weight A 10 60 6.0 B 20 100 5.0 C 30 120 4.0 Order: A, B, C. Take A completely: remaining = 40, value = 60. Take B completely: remaining = 20, value = 160. Take 20/30 of C: added value = 120 × 20/30 = 80. Final value = 240; remaining capacity = 0. 6. Design defence This is pseudocode because it describes the algorithm using language-independent operations such as SORT, FOR, IF, and RETURN. It specifies inputs, decisions, updates, and outputs without using Python-specific syntax or relying on informal instructions. 7. Complexity Sorting takes O(n log n) and the selection pass takes O(n). Total time complexity is O(n log n). The additional storage for selected fractions is O(n); sorting space depends on the sorting method.
