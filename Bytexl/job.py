from collections import deque

class Job:
    def __init__(self, name, time_needed):
        self.name = name
        self.time_needed = time_needed
        self.time_elapsed = 0

    def get_name(self):
        return self.name

    def get_time_needed(self):
        return self.time_needed

    def get_time_elapsed(self):
        return self.time_elapsed

    def __str__(self):
        return f"Job({self.name}, {self.time_needed}, {self.time_elapsed})"

    def elapsed_time(self, no_of_mins):
        self.time_elapsed += no_of_mins
        if self.time_elapsed >= self.time_needed:
            self.time_elapsed = self.time_needed


class Employee:
    def __init__(self, name):
        self.name = name
        self.allocated_job = None

    def set_allocated_job(self, allocated_job):
        self.allocated_job = allocated_job

    def get_name(self):
        return self.name

    def get_allocated_job(self):
        return self.allocated_job

    def elapsed_time(self, no_of_mins):
        if self.allocated_job is not None:
            self.allocated_job.elapsed_time(no_of_mins)
            if self.allocated_job.get_time_elapsed() == self.allocated_job.get_time_needed():
                completed_job = self.allocated_job
                self.allocated_job = None
                return completed_job
        return None


class Company:
    def __init__(self, emp_list):
        self.employees = [Employee(name) for name in emp_list]
        self.pending_jobs = deque()

    def get_employees(self):
        return self.employees

    def get_pending_jobs(self):
        return list(self.pending_jobs)

    def allocate_new_job(self, job):
        for employee in self.employees:
            if employee.get_allocated_job() is None:
                employee.set_allocated_job(job)
                return
        if len(self.pending_jobs) < 10:
            self.pending_jobs.append(job)
        else:
            print("Pending jobs queue is full.")

    def elapsed_time(self, no_of_mins):
        for employee in self.employees:
            completed_job = employee.elapsed_time(no_of_mins)
            if completed_job is not None and self.pending_jobs:
                next_job = self.pending_jobs.popleft()
                employee.set_allocated_job(next_job)

# Example Usage
if __name__ == "__main__":
    company = Company(["Aditya", "Hetvi", "Chatni"])
    job1 = Job("Job1", 30)
    job2 = Job("Job2", 45)
    job3 = Job("Job3", 60)
    job4 = Job("Job4", 20)
    
    company.allocate_new_job(job1)
    company.allocate_new_job(job2)
    company.allocate_new_job(job3)
    company.allocate_new_job(job4)
    
    # Simulate time passing
    company.elapsed_time(30)  # 30 minutes elapsed

    # Check the status of employees and pending jobs
    for employee in company.get_employees():
        print(f"Employee: {employee.get_name()}, Allocated Job: {employee.get_allocated_job()}")
    
    print("Pending Jobs:", company.get_pending_jobs())
    
    company.elapsed_time(30)  # 30 more minutes elapsed
    
    # Check again after more time has elapsed
    for employee in company.get_employees():
        print(f"Employee: {employee.get_name()}, Allocated Job: {employee.get_allocated_job()}")
    
    print("Pending Jobs:", company.get_pending_jobs())
