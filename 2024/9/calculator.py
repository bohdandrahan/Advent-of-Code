class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):
        print('calculate 1 is running')

        disk = []
        for i, number in enumerate(self.data):
            print(i, number)
            if i % 2 == 0:
                for each in range(int(number)):
                    disk.append(int(i//2))
            else:
                for each in range(int(number)):
                    disk.append('.')
        print(disk)
        print(disk.count('.'))

        l = 0
        r = len(disk) - 1

        while l < r:
            if disk[l] != '.':

                l += 1
                continue
            if disk[r] == '.':
                r -= 1
                continue

            disk[l] = disk[r]
            disk[r] = '.'
            l += 1
            r -= 1

        result = 0
        for i, each in enumerate(disk):
            if each == '.':
                break
            result += i * each

        print(disk)

        return result

    def calculate2(self):
        print('calculate 2 is running')

        files = []
        spaces = []

        disk = []

        for i, number in enumerate(self.data):
            if i % 2 == 0:
                files.append(int(number))
            else:
                spaces.append(int(number))

        print(files, spaces, 'BEFORE')

        id_files = []

        for id, size in enumerate(files):
            id_files.append([size, id])

        i = len(id_files) - 1

        disk = []
        for i in range(len(id_files)):
            for each in range(id_files[i][0]):
                disk.append(id_files[i][1])
            for each in range(spaces[i]):
                disk.append('.')

        print(disk)
        print('THIS', id_files, spaces)

        result = 0
        return result
