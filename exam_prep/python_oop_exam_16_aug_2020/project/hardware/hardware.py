class CannotInstallException(Exception):
    pass


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.memory = memory
        self.capacity = capacity
        self.type = type
        self.name = name
        self.software_components = []

    def install(self, software):
        total_consumption = sum([s.capacity_consumption for s in self.software_components])\
                           + software.capacity_consumption
        total_memory = sum([s.memory_consumption for s in self.software_components]) + software.memory_consumption
        if self.capacity < total_consumption or self.memory < total_memory:
            raise CannotInstallException('Software cannot be installed')

        self.software_components.append(software)

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)
