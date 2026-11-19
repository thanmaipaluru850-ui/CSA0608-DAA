Task 2 – Job Sequencing with Deadlines
1. Problem Model
Input: A set of jobs, where each job has a Job ID, deadline, and profit. Each job requires one time slot.

Output: Selected jobs with their assigned time slots and the total profit.

Objective: To maximise the total profit by completing jobs before or on their deadlines.

Constraints:
- Only one job can be performed in one time slot.
- A job must be completed before or on its deadline.
- Each job requires one time slot.
Decision: Decide whether to select a job and which available time slot to assign.

Feasibility Information: Check the job deadline and whether the selected time slot is empty.
2. Greedy Hypothesis
The greedy method sorts all jobs in descending order of profit.

It selects the highest-profit job first and assigns it to the latest available time slot before its deadline.

This method helps to maximise profit while keeping earlier slots available for other jobs.
3. Pseudocode
ALGORITHM: JobSequencing(Jobs)

INPUT: Jobs with ID, Deadline and Profit.

OUTPUT: Job Schedule and Maximum Profit.
BEGIN
    maxDeadline ← Maximum deadline among Jobs

    CREATE slots[1...maxDeadline]
    Initially all slots are EMPTY

    SORT Jobs in descending order of profit

    totalProfit ← 0

    FOR each job j in Jobs DO

        FOR slot ← MIN(j.deadline, maxDeadline) DOWNTO 1 DO

            IF slots[slot] is EMPTY THEN
                slots[slot] ← j.ID
                totalProfit ← totalProfit + j.profit
                BREAK
            END IF

        END FOR

    END FOR

    RETURN slots, totalProfit
END


4. Desk Check
Input:
Job	Deadline	Profit
A	2	80
B	1	35
C	2	60
D	3	40
E	1	25

Profit Order:

A(80), C(60), D(40), B(35), E(25).

Step-by-Step Execution:
Job	Slot Decision	Schedule	Profit
A	Put in slot 2	[–, A, –]	80
C	Put in slot 1	[C, A, –]	140
D	Put in slot 3	[C, A, D]	180
B	Rejected	[C, A, D]	180
E	Rejected	[C, A, D]	180

Final Schedule:
- Slot 1 = C
- Slot 2 = A
- Slot 3 = D
Maximum Profit = 60 + 80 + 40 = 180.
5. Challenge / Modified Input
Change only Job D's profit from 40 to 90.

New Profit Order:

D(90), A(80), C(60), B(35), E(25).

Step-by-Step Execution:
1. D is placed in slot 3.
2. A is placed in slot 2.
3. C is placed in slot 1.
4. B and E cannot be placed because the available slots are full.
Final Schedule:
- Slot 1 = C
- Slot 2 = A
- Slot 3 = D
New Maximum Profit = 90 + 80 + 60 = 230.

Changed Decision: Job D gets the highest priority because its profit is increased from 40 to 90. The selected jobs remain the same, but the total profit increases from 180 to 230.
6. Complexity Analysis
Let:
- n = Number of jobs.
- d = Maximum deadline.
Time Complexity:
- Sorting the jobs: O(n log n)
- Searching for an available slot: O(nd)
- Total Time Complexity: O(n log n + nd)
Space Complexity:

O(d), because an array of size d is used to store the job slots.

Result: Thus, the Job Sequencing with Deadlines problem is solved using the Greedy Algorithm to maximise the total profit by selecting jobs in descending order of profit and assigning them to the latest available slots.
