from exam_prep.python_oop_exam_16_aug_2020.project import CannotInstallException
from exam_prep.python_oop_exam_16_aug_2020.project import HeavyHardware
from exam_prep.python_oop_exam_16_aug_2020.project import PowerHardware
from exam_prep.python_oop_exam_16_aug_2020.project import ExpressSoftware
from exam_prep.python_oop_exam_16_aug_2020.project import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        try:
            hardware = [hardware for hardware in System._hardware if hardware.name == hardware_name][0]
        except IndexError as ex:
            return 'Hardware does not exist'

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)

        try:
            hardware.install(express_software)
            System._software.append(express_software)
        except CannotInstallException as ex:
            return 'Software cannot be installed'

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        try:
            hardware = [hardware for hardware in System._hardware if hardware.name == hardware_name][0]
        except IndexError as ex:
            return 'Hardware does not exist'

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)

        try:
            hardware.install(light_software)
            System._software.append(light_software)
        except CannotInstallException as ex:
            return 'Software cannot be installed'

    @staticmethod
    def release_software_component(hardware_name, software_name):
        try:
            hardware = [hardware for hardware in System._hardware if hardware.name == hardware_name][0]
            software = [software for software in System._software if software.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError as ex:
            return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        total_used_memory = sum(
            [comp.memory_consumption for hardware in System._hardware for comp in hardware.software_components]
        )
        total_memory = sum([hardware.memory for hardware in System._hardware])

        total_used_capacity = sum(
            [comp.capacity_consumption for hardware in System._hardware for comp in hardware.software_components]
        )
        total_capacity = sum([hardware.capacity for hardware in System._hardware])

        result = f'System Analysis\n' \
                 f'Hardware Components: {len(System._hardware)}\n' \
                 f'Software Components: {len(System._software)}\n' \
                 f'Total Operational Memory: {int(total_used_memory)} / {int(total_memory)}\n' \
                 f'Total Capacity Taken: {int(total_used_capacity)} / {int(total_capacity)}'
        return result

    @staticmethod
    def system_split():
        result = ''

        for hardware in System._hardware:
            express_software_comps_count = len([comp for comp in hardware.software_components if comp.type == 'Express'])
            light_software_comps_count = len([comp for comp in hardware.software_components if comp.type == 'Light'])
            total_memory_used = sum([comp.memory_consumption for comp in hardware.software_components])
            total_capacity_used = sum([comp.capacity_consumption for comp in hardware.software_components])
            software_components = ', '.join([comp.name for comp in hardware.software_components]) \
                if hardware.software_components else 'None'

            result += f'Hardware Component - {hardware.name}\n' \
                      f'Express Software Components: {express_software_comps_count}\n' \
                      f'Light Software Components: {light_software_comps_count}\n' \
                      f'Memory Usage: {int(total_memory_used)} / {int(hardware.memory)}\n' \
                      f'Capacity Usage: {int(total_capacity_used)} / {int(hardware.capacity)}\n' \
                      f'Type: {hardware.type}\n' \
                      f'Software Components: {software_components}'

        return result