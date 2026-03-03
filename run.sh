#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

pick_python_with_tk() {
  local candidates=()
  if [[ "$(uname -s)" == "Darwin" ]]; then
    candidates=(python3.12 python3 /usr/bin/python3)
  else
    candidates=(python3.12 python3.11 python3)
  fi

  local cmd=""
  local bin=""
  for cmd in "${candidates[@]}"; do
    if ! bin="$(command -v "$cmd" 2>/dev/null)"; then
      continue
    fi
    if "$bin" - <<'PY' >/dev/null 2>&1
import tkinter
PY
    then
      echo "$bin"
      return 0
    fi
  done
  return 1
}

if ! BASE_PYTHON="$(pick_python_with_tk)"; then
  echo "❌ No encontré una instalación de Python con tkinter disponible."
  if [[ "$(uname -s)" == "Darwin" ]]; then
    echo "En macOS, instala una versión con Tk (por ejemplo python3.12) y vuelve a ejecutar ./run.sh"
  fi
  exit 1
fi

if [ ! -d "$ROOT_DIR/venv" ]; then
  echo "📦 Creando entorno virtual en ./venv con: $BASE_PYTHON"
  "$BASE_PYTHON" -m venv venv
fi

if ! "$ROOT_DIR/venv/bin/python" - <<'PY' >/dev/null 2>&1
import tkinter
PY
then
  TS="$(date +%Y%m%d_%H%M%S)"
  BACKUP_DIR="$ROOT_DIR/venv.no_tk.$TS"
  echo "⚠️ El venv actual no tiene tkinter. Moviendo a: $BACKUP_DIR"
  mv "$ROOT_DIR/venv" "$BACKUP_DIR"
  echo "📦 Recreando entorno virtual con: $BASE_PYTHON"
  "$BASE_PYTHON" -m venv venv
fi

PYTHON_BIN="$ROOT_DIR/venv/bin/python"
PIP_BIN="$ROOT_DIR/venv/bin/pip"

echo "📦 Verificando dependencias..."
"$PIP_BIN" install -q -r requirements.txt

echo "🌐 Verificando navegador Chromium para Playwright..."
"$PYTHON_BIN" -m playwright install chromium >/dev/null

echo "🚀 Iniciando interfaz visual..."
exec "$PYTHON_BIN" gui.py
