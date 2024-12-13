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

        i = len(files) - 1

        id_files = []
        for id, size in enumerate(files):
            id_files.append([size, id])

        while i > 0:
            file = id_files[i]
            for j in range(id_files.index(file)):
                if spaces[j] >= file[0]:

                    spaces[j] -= file[0]
                    spaces.insert(j, 0)
                    spaces[i] += file[0]
                    if i+1 < len(spaces):
                        spaces[i] += spaces[i+1]
                        spaces.pop(i+1)

                    id_files.pop(i)
                    id_files.insert(j+1, file)
                    break
            i -= 1

        disk = []
        for i in range(len(id_files)):
            for each in range(id_files[i][0]):
                disk.append(id_files[i][1])
            for each in range(spaces[i]):
                disk.append('.')

        result = 0

        for i, each in enumerate(disk):
            if each != '.':
                result += each * i

        return result
