#include <iostream>
#include <queue>
#include<bits/stdc++.h>
using namespace std;

struct Job {
    int id;
    int priority;
    int deadline;
    int duration;

    Job(int id, int priority, int deadline, int duration) :
        id(id), priority(priority), deadline(deadline), duration(duration) {}

    bool operator<(const Job& other) const {
        return priority < other.priority;
    }
};

struct JobComparator {
    bool operator()(const Job& lhs, const Job& rhs) const {
        return lhs.deadline > rhs.deadline;
    }
};

void scheduleJobs(priority_queue<Job>& pq, const int current_time) {
    priority_queue<Job, vector<Job>, JobComparator> deadline_queue;

    while (!pq.empty()) {
        Job current_job = pq.top();
        pq.pop();

        if (current_time + current_job.duration <= current_job.deadline) {
            cout << "Scheduled job " << current_job.id << " at time " << current_time << endl;
            current_time += current_job.duration;
        } else {
            deadline_queue.push(current_job);
        }
    }

    while (!deadline_queue.empty()) {
        Job current_job = deadline_queue.top();
        deadline_queue.pop();

        if (current_time + current_job.duration <= current_job.deadline) {
            cout << "Scheduled job " << current_job.id << " at time " << current_time << endl;
            current_time += current_job.duration;
        } else {
            cout << "Could not schedule job " << current_job.id << endl;
        }
    }
}

int main() {
    priority_queue<Job> jobs;

    jobs.emplace(1, 3, 10, 3);
    jobs.emplace(2, 1, 8, 2);
    jobs.emplace(3, 2, 5, 1);

    scheduleJobs(jobs, 0);

    return 0;
}