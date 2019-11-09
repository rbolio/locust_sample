from locust import HttpLocust, TaskSet, task


class MyTaskSet(TaskSet):
    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def promociones(self):
        self.client.get("/promociones")

    @task(3)
    def f_electronico(self):
        self.client.get("/folleto-electronico")

    @task(4)
    def focos(self):
        self.client.get("/iluminacion/focos")


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
