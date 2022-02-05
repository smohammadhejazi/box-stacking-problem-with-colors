class Box:
    def __init__(self, w, top, bottom, left, right, front, back):
        self.w = w
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.front = front
        self.back = back

    def __lt__(self, other):
        return self.w < other.w

    def __str__(self):
        return "w=" + str(self.w) + " top=" + str(self.top) + " bottom=" + str(self.bottom) +\
               " left=" + str(self.left) + " right=" + str(self.right) +\
               " front=" + str(self.front) + " back=" + str(self.back)


def maxTower(boxArray):
    boxArrayExtended = []
    for box in boxArray:
        newBox1 = Box(box.w, box.bottom, box.top, box.right, box.left, box.back, box.front)
        newBox2 = Box(box.w, box.left, box.right, box.bottom, box.top, box.front, box.back)
        newBox3 = Box(box.w, box.right, box.left, box.top, box.bottom, box.front, box.back)
        newBox4 = Box(box.w, box.front, box.back, box.left, box.right, box.bottom, box.top)
        newBox5 = Box(box.w, box.back, box.front, box.left, box.right, box.top, box.bottom)
        boxArrayExtended.append(box)
        boxArrayExtended.append(newBox1)
        boxArrayExtended.append(newBox2)
        boxArrayExtended.append(newBox3)
        boxArrayExtended.append(newBox4)
        boxArrayExtended.append(newBox5)

    boxArrayExtended.sort(reverse=True)

    # Print extendedArray for debug
    # for box in boxArrayExtended:
    #     print(str(box))

    # Initialize maximum height for each box alone
    maxHeight = [1 for box in boxArrayExtended]
    previousBox = [-1 for box in boxArrayExtended]

    # Start from index 0 and compute all possible cases
    for i in range(0, len(boxArrayExtended)):
        for j in range(0, i):
            if (boxArrayExtended[i].w < boxArrayExtended[j].w and
                    boxArrayExtended[i].bottom == boxArrayExtended[j].top):
                if maxHeight[i] < maxHeight[j] + 1:
                    maxHeight[i] = maxHeight[j] + 1
                    previousBox[i] = j

    maxValue = max(maxHeight)
    maxIndex = maxHeight.index(maxValue)

    tower = []
    index = maxIndex
    while index != -1:
        tower.append(boxArrayExtended[index])
        index = previousBox[index]

    return tower


if __name__ == "__main__":
    # Test 1
    # boxArray = [Box(9, 'a', 'b', 'c', 'd', 'e', 'f'),
    #             Box(8, 'a', 'b', 'c', 'd', 'e', 'f'),
    #             Box(7, 'a', 'b', 'c', 'd', 'e', 'f'),
    #             Box(6, 'a', 'b', 'c', 'd', 'e', 'f')]

    # Test 2
    # boxArray = [Box(9, 'a', 'a', 'a', 'a', 'a', 'b'),
    #             Box(8, 'a', 'a', 'a', 'a', 'b', 'b'),
    #             Box(7, 'a', 'a', 'a', 'a', 'b', 'b'),
    #             Box(6, 'a', 'a', 'a', 'a', 'b', 'b')]

    # Test 3
    # boxArray = [Box(9, 'a', 'a', 'a', 'a', 'a', 'b'),
    #             Box(9, 'a', 'a', 'a', 'a', 'a', 'b'),
    #             Box(8, 'a', 'a', 'a', 'a', 'a', 'b'),
    #             Box(7, 'a', 'a', 'a', 'a', 'a', 'b')]

    # Test 4
    boxArray = [Box(9, 'a', 'a', 'a', 'a', 'a', 'a'),
                Box(8, 'a', 'a', 'a', 'a', 'a', 'a'),
                Box(7, 'a', 'v', 'a', 'a', 'a', 'a'),
                Box(6, 'a', 'a', 'a', 'a', 'a', 'a')]

    tower = maxTower(boxArray)
    print("Height = " + str(len(tower)))
    for box in tower:
        print(box)
