WIDTH = 1200
HEIGHT = 800
FPS = 480
BG_COLOR = "black"
CENTRAL_LINE = {
    "color": "white",
    "width": 3
}
BALL = {
    "color": "white",
    "speed": 1,
    "size" : 8,
    "dx"   : WIDTH // 2,
    "dy"   : HEIGHT // 2
}
DIRECTIONS = {
    "top-right": (BALL["speed"], -BALL["speed"]),
    "bottom-right": (BALL["speed"], BALL["speed"]),
    "top-left": (-BALL["speed"], -BALL["speed"]),
    "bottom-left": (-BALL["speed"], BALL["speed"])
}
PLAYER = {
    "height": HEIGHT // 10,
    "width": WIDTH // 200,
    "color": "white",
    "dx": WIDTH // 24,
    "dy": (HEIGHT // 2) - (HEIGHT // 15) // 2,
    "speed": 1
}
SCORE = {
    "font": "JetBrains Mono",
    "color": "white",
    "size": 175,
    "dx": WIDTH // 4,
    "dy": HEIGHT // 10
}