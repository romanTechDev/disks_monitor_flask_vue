import subprocess

# all_disks_info_cmd = """lsblk -o +ROTA,DISC-GRAN"""

all_disks_name_cmd = '''lsblk -nl -o NAME'''
all_disks_size_cmd = '''lsblk -nl -o SIZE'''
all_disks_type_cmd = '''lsblk -nl -o TYPE'''
all_disks_mountpoint_cmd = '''lsblk -nl -o MOUNTPOINT'''

all_disks_name = subprocess.run(all_disks_name_cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout
all_disks_size = subprocess.run(all_disks_size_cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout
all_disks_type = subprocess.run(all_disks_type_cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout
all_disks_mountpoint = subprocess.run(all_disks_mountpoint_cmd, shell=True, stdout=subprocess.PIPE,
                                      encoding='utf-8').stdout

all_disks_name_array = []
all_disks_size_array = []
all_disks_type_array = []
all_disks_mountpoint_array = []
all_disks_priority_array = []

for disk_name in all_disks_name.split('\n'):
    all_disks_name_array.append(disk_name)

for disk_size in all_disks_size.split('\n'):
    all_disks_size_array.append(disk_size)

for disk_type in all_disks_type.split('\n'):
    all_disks_type_array.append(disk_type)

for disk_mountpoint in all_disks_mountpoint.split('\n'):
    all_disks_mountpoint_array.append(disk_mountpoint)


def set_disk_priority(all_disks_mountpoint_array, all_disks_type_array):
    all_disks_priority_array = []

    i = 0

    flag = 0
    all_flags = 0

    first_sorting = False

    is_system = False
    end_of_disk = False

    while i != len(all_disks_type_array):
        if first_sorting == True and i < len(all_disks_priority_array):
            i = len(all_disks_priority_array)

        if i == len(all_disks_type_array):
            break

        if end_of_disk == True and is_system == True:
            while flag != all_flags:
                all_disks_priority_array.append('system')
                flag += 1
            end_of_disk = False
            is_system = False
            first_sorting = True
            i = 0
            flag = 0
            all_flags = 0
            continue
        elif end_of_disk == True and is_system == False:
            while flag != all_flags:
                all_disks_priority_array.append('common')
                flag += 1
            end_of_disk = False
            first_sorting = True
            i = 0
            flag = 0
            all_flags = 0
            continue

        if all_disks_type_array[i] != 'part' and (
                all_disks_type_array[i - 1] == 'part' or all_disks_type_array[
            i - 1] != 'part') and first_sorting == True:  # начало нового диска
            if all_disks_mountpoint_array[i] == '/':
                is_system = True
                first_sorting = False
                all_flags += 1
                if i == len(all_disks_type_array) - 1:
                    i = 0
                    end_of_disk = True
                    continue
                i += 1
                continue
            else:
                first_sorting = False
                all_flags += 1
                if i == len(all_disks_type_array) - 1:
                    i = 0
                    end_of_disk = True
                    continue
                i += 1
                continue
        elif all_disks_type_array[i] != 'part' and (
                all_disks_type_array[i - 1] == 'part' or all_disks_type_array[
            i - 1] != 'part') and i != 0:  # конец диска
            end_of_disk = True
            continue

        if all_disks_mountpoint_array[i] == '/':
            is_system = True

        if all_disks_type_array[i - 1] == 'disk' and all_disks_type_array[i] == 'part':  # и так дальше
            all_flags += 1
            i += 1
            continue

        if all_disks_type_array[i - 1] == 'part' and all_disks_type_array[i] == 'part':  # и так дальше
            all_flags += 1
            i += 1
            continue

        if all_disks_type_array[i] == 'part' and all_disks_mountpoint_array[i] == '/':
            all_flags += 1
            is_system = True
            i += 1
            continue

        if i == len(all_disks_type_array):
            end_of_disk = True
            continue

        if all_disks_mountpoint_array[i] == '':
            all_flags += 1
            i += 1
            continue

        all_disks_priority_array = 'external'
        i += 1

    return all_disks_priority_array
