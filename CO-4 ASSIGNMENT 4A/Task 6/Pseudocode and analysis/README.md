Task 6 – Design Challenge: Energy-Aware Job Scheduling

Stage 1 – Problem interpretation

Input: jobs with start time, finish time and energy-saving value. Output: a set of selected jobs and maximum total energy-saving value. Objective: maximise the sum of values. Constraints: one server; selected jobs must not overlap. A job finishing at t and another starting at t are compatible. Decision: include or exclude each job.

Stage 2 – Strategy

Use weighted interval scheduling with dynamic programming. Choosing the earliest-finishing job or highest-value job alone is not generally optimal: one high-value long job may prevent several compatible jobs from being selected. DP compares including each job with excluding it, using the best compatible earlier solution.

Stage 3 – State and critical information

Sort jobs by finish time. Let p(i) be the largest index smaller than i whose job finishes at or before job i starts. DP[i] is the maximum energy-saving value obtainable from the first i jobs in finish-time order. Include job i: value[i] + DP[p(i)]. Exclude job i: DP[i-1]. Base: DP[0] = 0.

Stage 4 – Complete pseudocode

ALGORITHM EnergyAwareSchedule(Jobs)

INPUT: Jobs with ID, start, finish, saving value

OUTPUT: Selected jobs and maximum saving value
BEGIN
    SORT Jobs by increasing finish time
    n <- number of Jobs

    FOR i <- 1 TO n DO
        p[i] <- largest j < i such that finish[j] <= start[i]
        IF no such j exists THEN p[i] <- 0
    END FOR

    DP[0] <- 0
    FOR i <- 1 TO n DO
        include <- value[i] + DP[p[i]]
        exclude <- DP[i-1]
        DP[i] <- MAX(include, exclude)
    END FOR

    selected <- empty list
    i <- n
    WHILE i > 0 DO
        IF value[i] + DP[p[i]] > DP[i-1] THEN
            APPEND Jobs[i].ID to selected
            i <- p[i]
        ELSE
            i <- i - 1
        END IF
    END WHILE

    REVERSE selected
    RETURN selected, DP[n]
END


For equal include/exclude values, this pseudocode excludes the current job; another optimal schedule may exist.

Stage 5 – Desk-check of the given dataset
Job	Start	Finish	Value	p(i)
J1	1	3	20	0
J2	2	5	50	0
J3	4	6	30	1
J4	6	8	40	3
J5	5	9	60	2
J6	8	10	30	4
J7	9	11	50	5
J8	11	13	40	7

i	Job	Include	Exclude	DP[i]
0	–	–	–	0
1	J1	20	0	20
2	J2	50	20	50
3	J3	50	50	50
4	J4	90	50	90
5	J5	110	90	110
6	J6	120	110	120
7	J7	160	120	160
8	J8	200	160	200

Reconstruction selects J8, J7, J5, J2 when tracing backwards.

Selected schedule: J2 (2–5), J5 (5–9), J7 (9–11), J8 (11–13).

Total energy saving = 50 + 60 + 50 + 40 = 200.

Stage 6 – Attack your own design

Use this adversarial dataset:
Job	Start	Finish	Value
A	1	10	100
B	1	3	40
C	3	5	40
D	5	7	40
E	7	10	40

This challenges a highest-value-first greedy strategy: job A has the largest individual value but blocks four compatible jobs.

Before calculation, predict that choosing A alone gives 100, while the four shorter jobs may give a better total.

DP computes the best compatible combination:

A alone = 100.

B, C, D and E are mutually compatible because each next job starts when the previous one finishes.

Their total = 40 + 40 + 40 + 40 = 160.

Result: DP selects B, C, D and E for 160, which is optimal.

The critical decision is comparing include and exclude values at every state. The example demonstrates why a single locally attractive choice is not a safe general strategy.

Complexity

Sorting takes O(n log n). Finding all predecessor indices by a linear scan takes O(n^2) in this simple design; DP and reconstruction take O(n). Total time is O(n^2) and space is O(n). Using binary search for each predecessor reduces the total to O(n log n).
