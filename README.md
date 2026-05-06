# ⚽ PALAVRA SECRETA DO TIMÃO
---

## 📖 Descrição do Projeto

Jogo de **Palavra Secreta** temático do **Corinthians**, desenvolvido em Python para terminal/console. O jogador deve descobrir palavras e frases relacionadas ao maior clube popular do Brasil antes de esgotar suas tentativas.

---

## 📁 Estrutura de Arquivos

```
corinthians_game/
│
├── jogo.py          ← Código principal do jogo
├── resultados.txt   ← Gerado automaticamente ao jogar
└── README.md        ← Este arquivo
```

---

## 📊 Arquivo de Resultados (`resultados.txt`)

Gerado automaticamente. Colunas:

```
=======================================================
  PALAVRA SECRETA DO TIMAO - REGISTRO DE PARTIDAS
=======================================================

-------------------------------------------------------
DATA        : "DATA" "HORARIO"
JOGADOR     : "NOME"
PALAVRA     : "PALAVRA"
NIVEL       : "DIFICIL"
PONTUACAO   : "x pts"
TENTATIVAS  : "0"
ACERTOS     : "6"
ERROS       : "0"
RESULTADO   : "VENCEU!"
-------------------------------------------------------
```

---

## ⭐ Regras e Pontuação

| Nível   | Tentativas | Acerto por letra | Erro por letra |
|---------|-----------|-----------------|---------------|
| Fácil   | 8         | +10 pts         | -3 pts        |
| Médio   | 6         | +15 pts         | -5 pts        |
| Difícil | 5         | +25 pts         | -10 pts       |

- **Bônus de eficiência**: +5 pts por cada tentativa não utilizada ao vencer
- O jogador propõe **uma letra por vez**
- Letras já tentadas não podem ser repetidas
- Letras iniciais são reveladas como dica visual
- Partida encerrada ao esgotar tentativas ou revelar toda a palavra

---

## 🏆 Funcionalidades

- ✅ Banco de 25 palavras/frases temáticas do Corinthians
- ✅ Seleção aleatória de palavras
- ✅ 3 níveis de dificuldade
- ✅ Barra visual de tentativas restantes
- ✅ Hall da Fama com histórico de partidas
- ✅ Salvamento automático em TXT
- ✅ Pontuação dinâmica com bônus de eficiência
- ✅ Controle completo de acertos, erros e tentativas

---

**Vai Corinthians! 🖤🤍⚽**
