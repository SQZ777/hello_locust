from locust import Locust, TaskSet, task
import random


class Actions(TaskSet):

    def give_number(self):
        self.number = random.randint(1,100)

    def on_start(self):
        self.give_number()

    def on_stop(self):
        print("bye bye {}".format(self.number))
        pass
    
    @task
    def say(self):
        print("Hello {}".format(self.number))


class ActionUser(Locust):
    task_set = Actions
    min_wait = 100
    max_wait = 700