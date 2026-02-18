# ==========================================
# 2. DATOS DEL VUELO
# ==========================================

VUELO_ORIGEN = "Santiago"
VUELO_DESTINO = "Buenos Aires"

# Antifraude: no permitir búsquedas con menos de 16 días de anticipación
MIN_DIAS_A_FUTURO = 16
DIAS_A_FUTURO = 16  # Día disponible a seleccionar en calendario (mínimo 16)

# Tipo de viaje: ONE_WAY (solo ida) o ROUND_TRIP (ida y vuelta)
TIPO_VIAJE = "ONE_WAY"

# Solo para ROUND_TRIP: cantidad de días entre ida y vuelta
DIAS_RETORNO_DESDE_IDA = 4

# Cantidad de pasajeros por tipo
CANTIDAD_ADULTOS = 1
CANTIDAD_NINOS = 0
CANTIDAD_INFANTES = 0
