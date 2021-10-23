input.onButtonPressed(Button.A, function () {
    game.resume()
    player.turn(Direction.Right, 90)
})
input.onButtonPressed(Button.AB, function () {
    game.pause()
})
input.onButtonPressed(Button.B, function () {
    game.resume()
    player.turn(Direction.Left, 90)
})
let player: game.LedSprite = null
player = game.createSprite(2, 2)
let sus = game.createSprite(randint(1, 5), randint(1, 5))
let kill = 1
game.setScore(0)
basic.forever(function () {
    if (player.isTouching(sus)) {
        sus.delete()
        sus = game.createSprite(randint(1, 5), randint(1, 5))
        game.addScore(1)
    }
    player.move(1)
    sus.move(1)
    sus.turn(Direction.Right, randint(90, 180))
    if (game.score() > kill) {
        basic.clearScreen()
        basic.showString("Scores")
        basic.showNumber(game.score())
    }
    basic.pause(500)
})
