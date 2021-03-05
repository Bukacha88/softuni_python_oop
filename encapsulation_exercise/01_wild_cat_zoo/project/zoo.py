from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__workers_capacity = workers_capacity
        self.__animal_capacity = animal_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity <= 0:
            return "Not enough space for animal"
        if self.__budget < price and self.__animal_capacity > 0:
            return "Not enough budget"

        self.animals.append(animal)
        self.__animal_capacity -= 1
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__ } added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__ } hired successfully"

    def fire_worker(self, worker_name):
        workers = [w for w in self.workers if w.name == worker_name]
        if not workers:
            return f"There is no {worker_name} in the zoo"
        worker = workers[0]
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = sum([worker.salary for worker in self.workers])
        if self.__budget < salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tend = sum([animal.get_needs() for animal in self.animals])
        if self.__budget < tend:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= tend
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def get_animal_type(self, type_name: str):
        return [str(a) for a in self.animals if a.__class__.__name__ == type_name]

    def get_worker_type(self, type_name: str):
        return [str(w) for w in self.workers if w.__class__.__name__ == type_name]

    def animals_status(self):
        lions = self.get_animal_type("Lion")
        tigers = self.get_animal_type("Tiger")
        cheetahs = self.get_animal_type("Cheetah")
        new_line = "\n"

        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions)} Lions:\n{new_line.join(lions)}\n" \
               f"----- {len(tigers)} Tigers:\n{new_line.join(tigers)}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n{new_line.join(cheetahs)}"

    def workers_status(self):
        keepers = self.get_worker_type("Keeper")
        caretakers = self.get_worker_type("Caretaker")
        vets = self.get_worker_type("Vet")
        new_line = "\n"

        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers)} Keepers:\n{new_line.join(keepers)}\n" \
               f"----- {len(caretakers)} Caretakers:\n{new_line.join(caretakers)}\n" \
               f"----- {len(vets)} Vets:\n{new_line.join(vets)}"

