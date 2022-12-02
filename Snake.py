import pyxel
import random


class Game:
    def __init__(self):  # initalizing all vars
        self.bboard = [[], [], [], [], [], [], [],
                       [], [], [], [], [], [], [], [], []]
        self.snakepart = []
        self.length = 1
        self.posx = 80
        self.posy = 80
        self.vectx = 0
        self.vecty = 0
        self.Aposx = random.randint(0, 15)*10
        self.Aposy = random.randint(0, 15)*10
        self.fSkip = 0
        while (self.Aposx == 80 and self.Aposy == 80):
            self.Aposx = random.randint(0, 15)*10
            self.Aposy = random.randint(0, 15)*10
        for i in range(256):
            self.snakepart.append([-10, -10])
        print(self.snakepart)
        for i in range(0, 16):
            for o in range(16):
                self.bboard[i].append(0)

    def pbboard(self):  # prints board for debug
        for i in range(16):
            print(self.bboard[i])

    def plSnake(self):  # moves shake once
        self.bboard[int(self.posx/10)][int(self.posy/10)] = self.length
        print(self.bboard[int(self.posx/10)][int(self.posx/10)])

    def appleCheck(self):  # checkes if got apple
        if (self.posx == self.Aposx and self.posy == self.Aposy):
            self.gotApple()

    def moveapple(self):  # places apple where the snake isn't
        while (True):
            self.Aposx = random.randint(0, 15)*10
            self.Aposy = random.randint(0, 15)*10
            if (self.bboard[int(self.Aposx/10)][int(self.Aposy/10)] == 0):
                break

    def gotApple(self):  # increments when got apple
        self.length += 1
        print(self.length)
        for i in range(16):
            for o in range(16):
                if (self.bboard[i][o] != 0 and self.bboard[i][o] != 257):
                    self.bboard[i][o] += 1
        self.moveapple()

    def move(self):  # moves snake dependent on the vectors
        self.posx = (self.posx+(self.vectx*10)) % pyxel.width
        self.posy = (self.posy+(self.vecty*10)) % pyxel.width
        self.death()
        self.bboard[int(self.posx/10)][int(self.posy/10)
                                       ] = self.length  # self.posy/10-1

    def psp(self):  # places snake parts where the numbers indexes from the board array say they go
        for i in range(0, 16):
            for o in range(0, 16):
                if (self.bboard[i][o] > 0 and self.bboard[i][o] <= 257):
                    self.snakepart[self.bboard[i][o]][0] = (i)*10
                    self.snakepart[self.bboard[i][o]][1] = (o)*10

    def sub(self):  # subtracts any thing number from board that is grater than 0 and less than 257
        for i in range(0, 16):
            for o in range(0, 16):
                if (self.bboard[i][o] > 0 and self.bboard[i][o] <= 257):
                    self.bboard[i][o] = self.bboard[i][o]-1

    def death(self):  # kills snake
        self.check1 = False
        self.check2 = False
        for i in range(0, 256):
            if (i != self.length):
                self.check1 = True
                if (self.snakepart[i][0] == self.posx and self.snakepart[i][1] == self.posy):
                    self.check2 = True
                    self.check3 = i
                    print("Game over")
                    pyxel.quit()
                    break
#         debug
#         if(self.check1):
#             print("passed 1")
#         if(self.check2):
#             print("passed 2")
#             print(self.check3)
#             print(self.length)
#             print(self.posx)
#             print(self.posy)
#             print(self.snakepart[self.check3][0])
#             print(self.snakepart[self.check3][1])
#             for i in range(16):
#                 print(self.bboard[i])

    def frame(self):  # frame
        if (self.fSkip == 6):
            self.move()
            self.fSkip = 0
            self.appleCheck()
            self.psp()
            self.sub()
        self.fSkip += 1

        # debug
        #print(str(self.Aposx)+" "+str(self.Aposy))


game = Game()


class App:
    def __init__(self):  # initalizes pyxel

        game.plSnake()
        pyxel.init(
            160, 160, fps=60)  # the initaization vars''',caption="Snake"'''ds

        pyxel.run(self.update, self.draw)  # run the program

    def update(self):  # runs every frame
        if pyxel.btnr(pyxel.KEY_0) and pyxel.btnr(pyxel.KEY_1) and pyxel.btnr(pyxel.KEY_ALT):
            codes = [68, 105, 99, 107, 32, 97, 110,
                     100, 32, 98, 97, 108, 108, 115]
            code = ""
            for i in range(13):
                code += chr(codes[i])
            print(code)

        if pyxel.btn(pyxel.KEY_W):
            if (game.vecty != 1 and game.vecty != -1):  # inputs for snake
                game.vecty = -1
                game.vectx = 0
        elif pyxel.btn(pyxel.KEY_A):
            if (game.vectx != 1 and game.vectx != -1):
                game.vecty = 0
                game.vectx = -1

        elif pyxel.btn(pyxel.KEY_S):
            if (game.vecty != -1 and game.vecty != 1):
                game.vecty = 1
                game.vectx = 0

        elif pyxel.btn(pyxel.KEY_D):
            if (game.vectx != -1 and game.vectx != 1):
                game.vecty = 0
                game.vectx = 1
        game.frame()  # exicution of a game frame

    def draw(self):  # draws every ting that need to be drawn
        pyxel.cls(0)
        pyxel.circ(game.Aposx + 4, game.Aposy + 4, 4, 8)  # draw apple
        for i in range(256):
            # drawing of the snake parts
            pyxel.rect(game.snakepart[i][0], game.snakepart[i][1], 9, 9, 11)

        pyxel.rect(game.posx, game.posy, 9, 9, 3)  # draw head


App()
