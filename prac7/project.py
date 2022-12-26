"""
Project
Estimate: 10 minutes
Actual:    minutes
"""

import datetime


class Project:
    def __init__(self, name, start_date: datetime, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage
        self.compare_mode = 0

    def __repr__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        if self.compare_mode == 0:
            return self.priority < other.priority
        elif self.compare_mode == 1:
            return self.start_date < other.start_date

    def set_compare_mode(self, mode):
        self.compare_mode = mode

    def update_completion(self, percentage):
        self.completion_percentage = percentage

    def update_priority(self, priority):
        self.priority = priority

    def is_completed(self):
        return self.completion_percentage == 100

    def file_str(self):
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"
