Instalação do solver GLPK. Para utilização é só criar o seu arquivo python
    e colocar o aqruivo dele dentro do docoker compose, no commmand: python seucommando.py 

Esse arquivo será executado ao chamar docker compose up --build
Na primeira vez a execução irá demorar bastante pois vai baixar e instalar o solver, python, etc.
Em execuções posteriores ele vai manter o setup e só irá executar o comando colocado no command