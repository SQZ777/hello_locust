from locust import HttpLocust, TaskSet, task
import random


class Actions(TaskSet):

    def give_number(self):
        self.number = random.randint(1, 100)
        print('hello {}'.format(self.number))

    def on_start(self):
        self.give_number()

    def on_stop(self):
        print("bye bye {}".format(self.number))
    
    @task(1)
    def login(self):
        payload = {"user":"1","password":"1","secretBodyToken":"9487"}
        headers = {"Cookie": "secretCookieToken=0487"}
        with self.client.post('/',
                        json = payload,
                        headers = headers,
                        name = "login") as res:
                        print(res.status_code)
                        print(res.json())
                        print(res.elapsed.total_seconds())


class ActionUser(HttpLocust):
    task_set = Actions
    min_wait = 100
    max_wait = 700