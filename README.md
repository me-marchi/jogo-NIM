# jogo-NIM
Atividade "Jogo NIM" realizado como parte do Curso "Introdução à Ciência da Computação com Python USP - Parte 1", organizado pela da Universidade de São Paulo (USP) e realizado na plataforma Coursera.

O jogo funciona da seguinte maneira: O usuário deve escolher inicialmente um número de peças para começar o jogo, e um número de peças máximas que podem ser retiradas a cada rodada. Desta forma, o usuário e o computador devem se revezar para retirar peças do jogo, sendo que o objetivo final é ser o jogador que retira as últimas peças do jogo. A cada rodada, cada jogador deve retirar no mínimo 1 peça e no máximo x peças, sendo x o número de peças que foi definido no início da partida para ser o número máximo a ser retirado. O usuário também pode escolher se quer jogar 1 partida ou um campeonato com 3 partidas.

Este jogo é um pouco confuso de explicar, por isso usarei um exemplo:

Número total de peças: 10
Número máximo de peças a serem retiradas: 3

Jogador 1: Tira 3 peças, sobram 7
Jogador 2: Tira 2 peças, sobram 5
Jogador 1: Tira 2 peças, sobram 3
Jogar 2: Tira 3 peças, acabaram as peças e ele ganhou o jogo!

Desta forma, o programa foi construído de modo que o computador sempre ganhará o jogo. Dependendo dos valores inseridos pelo usuário, o programa decide se o usuário deve começar ou o computador, de modo a sempre garantir a vitória do computador. 
