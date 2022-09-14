# Hangman Challenge

<br>

## Desafio do Jogo de Forca

<br>

<strong>Objetivo</strong> - Criar jogo de Forca utilizando Python

- [x] `v1` - Jogo Rodando no próprio Terminal
- [ ] `v2` - Jogo Rodando em Aplicação Web (*#ToDo*)

<br>

<strong>Regras</strong>

### Modo de Jogar

 <details>
    <p>

- Palavra
  - Será solicitado que a 1ª pessoa insira uma palavra no sistema. Essa palavra passa a ser o objetivo a ser descoberto pela 2ª pessoa

<br>

  - Adivinhação da palavra 
    - A 2ª pessoa irá palpitar letras a fim de descobrir a *palavra-objetivo*
    - O jogo irá retornar uma resposta
      - Palpite correto -> `posição da letra na palavra`
      - Palpite errado -> `Adiciona letra a grupo de palpites incorretos`
    - O jogo irá se encerrar ou com a palavra correta sendo descoberta, ou com as vidas acabando

<br>

### Vidas

- A 2ª pessoa terá a seguinte quantidade de lidas:
  - 1 + Qtd. de letras na *palavra-objetivo*
    </p>
    </details>