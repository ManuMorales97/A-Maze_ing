N = 1
E = 2
S = 4
W = 8

ALL_WALLS = N | E | S | W
DELTA = {N: (0, -1), E: (1, 0), S: (0, 1), W: (-1, 0)}
OPPOSITE = {N: S, S: N, E: W, W: E}
LETTER = {N: "N", E: "E", S: "S", W: "W"}

grid = list[list[int]]

def new_grid(width: int, height: int) -> grid:
    return [[ALL_WALLS for _ in range(width)] for _ in range(height)]


def in_bounds(grid: grid, x: int, y: int) -> bool:
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def neighbors(grid: grid, x: int, y: int) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []
    for d in (N, E, S, W):
        dx, dy = DELTA[d]
        nx = x + dx
        ny = y + dy
        if in_bounds(grid, nx, ny):
            result.append((d, nx, ny))
    return result


def remove_wall(grid: grid, x: int, y: int, d: int) -> None:
    dx, dy = DELTA[d]
    nx = x + dx
    ny = y + dy
    if not in_bounds(grid, nx, ny):
        raise ValueError(f"Cannot open a border wall at ({x}, {y})")
    grid[y][x] &= ~d
    grid[ny][nx] &= ~OPPOSITE[d]


def is_coherent(grid: grid) -> bool:
    if not grid or not grid[0]:
        return False
    width = len(grid[0])
    for row in grid:
        if len(row) != width:
            return False
    for y in range(len(grid)):
        for x in range(width):
            for d in (N, E, S, W):
                dx, dy = DELTA[d]
                nx = x + dx
                ny = y + dy
                closed = bool(grid[y][x] & d)
                if in_bounds(grid, nx, ny):
                    neighbor_closed = bool(grid[ny][nx] & OPPOSITE[d])
                    if closed != neighbor_closed:
                        return False
                elif not closed:
                    return False
    return True
