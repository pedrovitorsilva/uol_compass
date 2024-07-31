#!/bin/bash
# Código para criar modelo de pasta para as sprints
# Sintaxe: sh modelo_sprint.sh {número da sprint}

NUMERO_SPRINT="$1" 

mkdir sprint$NUMERO_SPRINT
cd sprint$NUMERO_SPRINT

echo "SPRINT $NUMERO_SPRINT - README" > README.md

mkdir exercicios
mkdir evidencias

mkdir desafio
echo "SPRINT $NUMERO_SPRINT - DESAFIO" > desafio/README.md

mkdir certificados
echo "Não houve certificados nesta sprint. :)" > certificados/certificados.txt 