# PyFOL Prover - version 1.0

> "Mathematics is a game played according to certain simple rules with meaningless marks on paper." (David Hilbert)

### Abstract
This repository was created to host the code and resources related to the final project of the INF420 course (Artificial Intelligence) at UFV (Universidade Federal de Viçosa), however I intend to keep updating and improving it over time. This project is a simple proposition prover, using First Order Logic, in Python.

### Resumo
Esse repositório foi criado para armazenar o código e os recursos relacionados ao projeto final do curso de INF420 (Inteligencia Artificial) na UFV (Universidade Federal de Viçosa), porém pretendo seguir o atualizando e incrementando ao longo do tempo. Este projeto se trata de um singelo provador de proposições, utilizando Lógica de Primeira Ordem, em Python.

### Tutorial - EN
After downloading the PyFOL lib, create a .py file in the same folder where "pyfol" and "examples" folders are. Then paste the folowing lines in your code:

```
import pyfol.prover.prover as pr
import pyfol.env.environment as environment

import pyfol.ds.graph_drawer as gd # If you want to plot a graph (IMPORTANT: you need networkx lib)
```
When you run your code, a HTML file will open with the documentation.

### Tutorial - PTBR
Depois de baixar a biblioteca PyFOL, crie um arquivo .py na mesma paste em que estão as pastas "pyfol" e "examples". Então, cole as seguintes linhas no seu código:

```
import pyfol.prover.prover as pr
import pyfol.env.environment as environment

import pyfol.ds.graph_drawer as gd # Se você quer plotar um grafo (IMPORTANTE: você precisa da biblioteca networkx)
```

Quando você executar um código com essas linhas, um arquivo HTML irá abrir com a documentação.

### Results
It's possible to check the results with the proof agent at the [Google Colaboratory](https://colab.research.google.com/drive/1z7eB68cjP_bKOe4WK07rXpqihZOr7zPc?usp=sharing) link.

### Resultados
É possível verificar resultados de teste realizados com o agente inteligente de provas no seguinte link para o [Google Colaboratory](https://colab.research.google.com/drive/1z7eB68cjP_bKOe4WK07rXpqihZOr7zPc?usp=sharing).
