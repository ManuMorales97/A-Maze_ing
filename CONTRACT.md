# Contrato entre Manu y Maria (temporal: borrar antes de entregar)

## Coordenadas
- `(x, y)`: `x` columna (crece al Este), `y` fila (crece al Sur).
- `(0, 0)` es la esquina superior izquierda.
- En listas: `grid[y][x]` (primero la fila).

## Celda (entero 0-15, 1 = pared cerrada)
| Bit | Valor | Pared |
|-----|-------|-------|
| 0   | 1     | N     |
| 1   | 2     | E     |
| 2   | 4     | S     |
| 3   | 8     | W     |

Un dígito hexadecimal = una celda. Constantes y helpers en
`mazegen/maze.py` (Maria las importa, no las duplica).

## Lo que expone Manu: `MazeGenerator` (mazegen/generator.py)
```python
gen = MazeGenerator(width, height, entry=(0, 0), exit_=None,
                    seed=None, perfect=False)
gen.generate(seed=None)
gen.grid      # list[list[int]], grid[y][x]
gen.entry     # tuple[int, int]
gen.exit      # tuple[int, int]
gen.blocked   # set[tuple[int, int]]  celdas del "42"
gen.solution  # str, p. ej. "EESSWWNE"
gen.seed      # int
gen.has_42    # bool, False si no cupo el 42
```
Parámetros inválidos -> `ValueError`.
HOY es una versión FALSA: siempre devuelve el laberinto 3x3 de juguete.
Las firmas no cambian; si hay que cambiarlas, avisar al otro antes.

## Lo que expone Maria (app/)
```python
parse_config(path) -> Config          # lanza ConfigError
write_maze(path, grid, entry, exit_, solution) -> None   # puede lanzar OSError
run_menu(gen, output_file) -> None
```

## Errores
- Maria: `ConfigError` en el parseo.
- Manu: `ValueError` en el generador.
- `a_maze_ing.py` captura ambos y muestra un mensaje claro.

## Pendiente de comprobar
- ¿Hexadecimal en mayúsculas o minúsculas? (el PDF usa minúsculas;
  probar con `maze_analyzer.py`). Los tests usan mayúsculas.
- Elegir licencia (Maria) y rellenar los TODO del README.

## Ramas de Git
`manu/nucleo` y `maria/app`. Cada uno solo toca sus carpetas.
