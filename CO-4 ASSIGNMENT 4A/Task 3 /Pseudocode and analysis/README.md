Task 3 – Dynamic Programming: 0/1 Knapsack
1. State Definition
DP[i][w] represents the maximum value that can be obtained using only the first i items with a weight capacity of at most w.
2. Recurrence
Let item i have weight weight[i] and value value[i].

Base Cases:
- DP[0][w] = 0 for every capacity w.
- DP[i][0] = 0 for every item count i.
Recurrence Formula:

If weight[i] is greater than w, the item cannot fit.

DP[i][w] = DP[i-1][w]

Otherwise, choose the maximum value between excluding and including the item.

DP[i][w] = MAX(DP[i-1][w], value[i] + DP[i-1][w-weight[i]])
- The first term excludes the item.
- The second term includes the item and adds its value to the best result for the remaining capacity.
3. Pseudocode with Reconstruction
ALGORITHM: Knapsack01(Items, W)

INPUT: n items with weight and value; capacity W.

OUTPUT: Maximum value and selected item IDs.
BEGIN

    CREATE DP[0..n][0..W]

    FOR w ← 0 TO W DO
        DP[0][w] ← 0
    END FOR

    FOR i ← 0 TO n DO
        DP[i][0] ← 0
    END FOR

    FOR i ← 1 TO n DO
        FOR w ← 1 TO W DO

            IF weight[i] > w THEN
                DP[i][w] ← DP[i-1][w]
            ELSE
                exclude ← DP[i-1][w]
                include ← value[i] + DP[i-1][w-weight[i]]

                DP[i][w] ← MAX(exclude, include)
            END IF

        END FOR
    END FOR

    selected ← empty list
    w ← W

    FOR i ← n DOWNTO 1 DO
        IF DP[i][w] != DP[i-1][w] THEN
            APPEND item[i].ID to selected
            w ← w - weight[i]
        END IF
    END FOR

    REVERSE selected

    RETURN DP[n][W], selected

END


4. Desk Check
Capacity = 7

Input:
Item	Weight	Value
P	2	12
Q	3	20
R	4	25
S	5	30

Important States:
1. With P and Q, capacity 5 gives value 12 + 20 = 32.
2. At capacity 7, P + R gives weight 6 and value 37.
3. Q + S weighs 8, so it is infeasible.
4. P + S weighs 7 and gives value 42.
5. Q + R weighs 7 and gives value 45.
6. All four items weigh 14 and cannot fit.
Optimal Selection:
- Selected Items = Q and R.
- Total Weight = 3 + 4 = 7.
- Maximum Value = 20 + 25 = 45.
Final DP Row for Capacities 0 through 7:
Capacity	0	1	2	3	4	5	6	7
DP Value	0	0	12	20	25	32	32	45

Maximum Value = 45.
5. Dependency Explanation
Each state in row i depends on the states from row i-1.

Therefore, the previous row must be calculated before the current row.

Processing items from first to last ensures that every include and exclude value is already available.

Reconstruction moves backwards through the DP table to identify the selected items.
6. Complexity Analysis
There are (n+1)(W+1) states, and each state takes constant time.

Time Complexity: O(nW)

Space Complexity: O(nW)

Result: Thus, the 0/1 Knapsack problem is solved using Dynamic Programming to obtain the maximum possible value without exceeding the given weight capacity.
