# Casos de Prueba - Bot Sky Airline

Comandos listos para copiar y pegar.

## Preparación
```bash
cd bot-skyairline
source venv/bin/activate
```

## Flujos principales (visibles)

### 1) Solo ida, Perú, 1 adulto
```bash
venv/bin/python -u test_sky.py --market PE --tipo-viaje ONE_WAY --adultos 1 --ninos 0 --infantes 0 --checkpoint CHECKOUT
```

### 2) Ida y vuelta, Perú, 1 adulto
```bash
venv/bin/python -u test_sky.py --market PE --tipo-viaje ROUND_TRIP --adultos 1 --ninos 0 --infantes 0 --checkpoint CHECKOUT
```

### 3) Solo ida, Perú, 2 adultos y 1 niño
```bash
venv/bin/python -u test_sky.py --market PE --tipo-viaje ONE_WAY --adultos 2 --ninos 1 --infantes 0 --checkpoint CHECKOUT
```

### 4) Ida y vuelta, Perú, 2 adultos y 1 infante
```bash
venv/bin/python -u test_sky.py --market PE --tipo-viaje ROUND_TRIP --adultos 2 --ninos 0 --infantes 1 --checkpoint CHECKOUT
```

## Variante con exploración de frontend

### Guarda screenshots/reportes por etapa para revisar diferencias de UI
```bash
venv/bin/python -u test_sky.py --market PE --tipo-viaje ROUND_TRIP --adultos 1 --ninos 0 --infantes 0 --modo-exploracion --checkpoint CHECKOUT
```

## Flags que más se tocan
- `--market PE|CL|AR|BR`
- `--tipo-viaje ONE_WAY|ROUND_TRIP`
- `--adultos N`
- `--ninos N`
- `--infantes N`
- `--checkpoint BUSQUEDA|SELECCION_TARIFA|DATOS_PASAJERO|CHECKOUT|PAGO`
- `--modo-exploracion`

Nota: `--dias` menor a 16 se ajusta automáticamente a 16 por antifraude.
