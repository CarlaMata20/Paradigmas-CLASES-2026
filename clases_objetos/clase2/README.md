# clase2

## Requisitos

- [uv](https://docs.astral.sh/uv/) instalado
- Python >= 3.14 (uv lo instala automáticamente si no lo tenés)

## Comandos básicos

### Sincronizar dependencias

```bash
uv sync
```

Crea el entorno virtual (`.venv/`) e instala las dependencias declaradas en `pyproject.toml`.

### Ejecutar `main.py`

```bash
uv run main.py
```

O de forma equivalente:

```bash
uv run python main.py
```

`uv run` sincroniza el entorno antes de ejecutar, así que no hace falta correr `uv sync` manualmente cada vez.

### Agregar una dependencia

```bash
uv add <paquete>
```

### Eliminar una dependencia

```bash
uv remove <paquete>
```
