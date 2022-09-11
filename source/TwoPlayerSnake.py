#TwoPlayerSnake class which is a two player version

from SnakeGame import *

class TwoPlayerSnake( SnakeGame ):
    def __init__(self):
        super().__init__()
        self.tie = False
        
    def startGame(self):
        super().startGame()
        self.root.bind("<Left>", self.goLeft)
        self.root.bind("<Right>", self.goRight)
        self.root.bind("<Up>", self.goUp)
        self.root.bind("<Down>", self.goDown)

        #add two snakes
        self.snakes = [
            Snake(self.canvas, self.snakeSize, self.snakeSize*((self.grid[0]//2) - 10),
                  self.snakeSize*((self.grid[1]//2)), "red", self.grid),
            Snake(self.canvas, self.snakeSize, self.snakeSize*((self.grid[0]//2) + 10),
                  self.snakeSize*((self.grid[1]//2)), "green", self.grid)]

        self.occupied[ self.snakes[0].getPosition() ] = [ self.snakes[0].body[0].type]
        self.occupied[ self.snakes[1].getPosition() ] = [ self.snakes[1].body[0].type]

        #start game loop
        self.loop()

    def loop(self):
        #make sure game is still running
        if not(self.pause) and self.active:
            for snake in self.snakes:
                snake.move(self.occupied)
                if self.check(snake,self.food):
                    snake.anotherOne()
                    self.newFood()

                snake.commit = False

            #Check for collisions
            oneP_lose = self.collide(self.snakes[0])
            twoP_lose = self.collide(self.snakes[1])

            if oneP_lose and twoP_lose:
                self.tie = True
                self.end()

            elif oneP_lose:
                self.end(self.snakes[0])

            elif twoP_lose:
                self.end(self.snakes[1])

            self.root.after(self.speed,self.loop)


    def end(self):
        #stop game
        self.active = False

        frame = Frame(self.root)

        if self.tie:
            message = ttk.Label( frame, text ="Tie!!!", font = "TkDefaultFont 30")
            self.tie = False
        else:
            message = ttk.Label( frame, text ="Winner is " + snake.color +"!", font = "TkDefaultFont 30")

        restart = Button( frame, text = "Restart", command = self.startGame )
        menu = Button( frame, text = "Main Menu", command = self.snakeMenu )

        message.grid()
        restart.grid()
        menu.grid()

        #output information to window game
        self.canvas.create_window(self.snakeSize*( self.grid[0]//2 ),
                                  self.snakeSize*( self.grid[1]//2 ),
                                  window = frame)
                                  
        
