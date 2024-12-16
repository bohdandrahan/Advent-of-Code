import zlib
import struct
import os


class Calculator():

    def __init__(self, data):
        self.data = data
        self.is_test = data["is_test"]

        # convention from here and now-on:
        # X is index by widht
        # Y is index by height.
        # I know, it's just a bit unintuitive but because we itterate
        # over rows first then over each element, X is logically associated with rows and not columns.:

        self.width = 11 if data["is_test"] else 101
        self.height = 7 if data["is_test"] else 103

        self.number_of_seconds_to_run = 100
        self.quadrant_ranges_x = [[0, self.width//2],
                                  [self.width//2 + 1, self.width]]
        self.quadrant_ranges_y = [[0, self.height//2],
                                  [self.height//2 + 1, self.height]]

    def calculate1(self):
        print('calculate 1 is running')
        self.finished_map = [[0 for y in range(self.height)]
                             for x in range(self.width)]
        for robot in self.data["robots"]:
            finish_position = self.get_position_after_N_seconds(
                robot["position"], robot["velocity"], self.number_of_seconds_to_run)

            self.finished_map[finish_position[0]][finish_position[1]] += 1

        result = 1
        for quadrant_x in self.quadrant_ranges_x:
            for quadrant_y in self.quadrant_ranges_y:
                current_num = 0
                for x in range(quadrant_x[0], quadrant_x[1]):
                    for y in range(quadrant_y[0], quadrant_y[1]):
                        current_num += self.finished_map[x][y]
                result *= current_num
        return result

    # 7285

    def calculate2(self):
        print('calculate 2 is running')

        k = 0
        for i in range(50000):

            self.map = [[0 for y in range(self.height)]
                        for x in range(self.width)]

            for j, robot in enumerate(self.data["robots"]):
                next_postition = self.get_position_after_N_seconds(
                    robot["position"], robot["velocity"], 1)
                self.data["robots"][j]["position"] = next_postition
                robot["position"] = next_postition

                self.map[next_postition[0]][next_postition[1]] = 255

            if ((i+1) - 14) % 101 == 0:
                self.makeGrayPNG(self.map)
                with open("2024/14/pngs/" + str(k) + "_" + str(i) + ".png", "wb") as f:
                    f.write(self.makeGrayPNG(self.map))
                k += 1

        result = 1
        return result

    def get_position_after_N_seconds(self, position, velocity, N):
        next_position = [position[0] + velocity[0], position[1] + velocity[1]]
        next_position = [next_position[0] % self.width,
                         next_position[1] % self.height]
        if N == 1:
            return next_position
        else:
            return self.get_position_after_N_seconds(next_position, velocity, N - 1)

    def makeGrayPNG(self, data):
        height = self.width  # Sue me
        width = self.height

        def I1(value):
            return struct.pack("!B", value & (2**8-1))

        def I4(value):
            return struct.pack("!I", value & (2**32-1))
        # compute width&height from data if not explicit
        if height is None:
            height = len(data)  # rows
        if width is None:
            width = 0
            for row in data:
                if width < len(row):
                    width = len(row)
        # generate these chunks depending on image type
        makeIHDR = True
        makeIDAT = True
        makeIEND = True
        png = b"\x89" + "PNG\r\n\x1A\n".encode('ascii')
        if makeIHDR:
            colortype = 0  # true gray image (no palette)
            bitdepth = 8  # with one byte per pixel (0..255)
            compression = 0  # zlib (no choice here)
            filtertype = 0  # adaptive (each scanline seperately)
            interlaced = 0  # no
            IHDR = I4(width) + I4(height) + I1(bitdepth)
            IHDR += I1(colortype) + I1(compression)
            IHDR += I1(filtertype) + I1(interlaced)
            block = "IHDR".encode('ascii') + IHDR
            png += I4(len(IHDR)) + block + I4(zlib.crc32(block))
        if makeIDAT:
            raw = b""
            for y in range(height):
                raw += b"\0"  # no filter for this scanline
                for x in range(width):
                    c = b"\0"  # default black pixel
                    if y < len(data) and x < len(data[y]):
                        c = I1(data[y][x])
                    raw += c
            compressor = zlib.compressobj()
            compressed = compressor.compress(raw)
            compressed += compressor.flush()  # !!
            block = "IDAT".encode('ascii') + compressed
            png += I4(len(compressed)) + block + I4(zlib.crc32(block))
        if makeIEND:
            block = "IEND".encode('ascii')
            png += I4(0) + block + I4(zlib.crc32(block))
        return png
