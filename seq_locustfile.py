from locust import Locust, TaskSequence, seq_task
import random


class Actions(TaskSequence):

    def give_number(self):
        self.number = random.randint(1,100)

    def on_start(self):
        self.give_number()

    def on_stop(self):
        print("bye bye {}".format(self.number))
    
    @seq_task(1)
    def say(self):
        print("Hello {}".format(self.number))

    @seq_task(2)
    def running(self):
        print("Running {}".format(self.number))


class ActionUser(Locust):
    task_set = Actions
    min_wait = 100
    max_wait = 700