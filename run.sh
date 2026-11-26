#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# Usa npm como gestor de paquetes del frontend para evitar fallos de Bun.
export REFLEX_USE_NPM=1

exec .venv/bin/reflex run "$@"
