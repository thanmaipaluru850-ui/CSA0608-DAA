Task 2: Job Sequencing with Deadlines
def job_sequencing(jobs):
    if any(deadline < 1 for _, deadline, _ in jobs):
        raise ValueError("Deadlines must be at least 1")
    max_deadline = max((deadline for _, deadline, _ in jobs), default=0)
    slots = [None] * (max_deadline + 1)  # slot 0 is unused
    total_profit = 0

    for job_id, deadline, profit in sorted(jobs, key=lambda x: x[2], reverse=True):
        for slot in range(min(deadline, max_deadline), 0, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                break
    return slots[1:], total_profit

if __name__ == "__main__":
    jobs = [("A", 2, 80), ("B", 1, 35), ("C", 2, 60),
            ("D", 3, 40), ("E", 1, 25)]
    schedule, profit = job_sequencing(jobs)
    print("Slots:", schedule)
    print("Maximum profit:", profit)
