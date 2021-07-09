from typing import List

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = []
        result.append('System Analysis')
        result.append(f'Hardware Components: {len(System._hardware)}')
        result.append(f'Software Components: {len(System._software)}')
        result.append(
            f'Total Operational Memory: {sum([el.used_memory for el in System._hardware])} / {sum([el.memory for el in System._hardware])}')
        result.append(
            f'Total Capacity Taken: {sum([el.used_capacity for el in System._hardware])} / {sum([el.capacity for el in System._hardware])}')

        return '\n'.join(result)

    @staticmethod
    def system_split():
        result = ''
        for h in System._hardware:
            result += f'Hardware Component - {h.name}\n'
            result += f'Express Software Components: {len([s for s in h.software_components if s.__class__.__name__ == "ExpressSoftware"])}\n'
            result += f'Light Software Components: {len([s for s in h.software_components if s.__class__.__name__ == "LightSoftware"])}\n'
            result += f"Memory Usage: {sum([s.memory_consumption for s in h.software_components])} / {h.memory}\n"
            result += f"Capacity Usage: {sum([s.capacity_consumption for s in h.software_components])} / {h.capacity}\n"
            result += f"Type: {h.type}\n"
            names = ', '.join([s.name for s in h.software_components])
            result += f"Software Components: {names if names else None}"

        return result
