# FeatureClassifier
Image processing algorithm that helps a drone to identify safe landing zones.

[Este projeto foi desenvolvido em outra plataforma de controle de versionamento e exportada para o GitHub após o término da disciplina Introdução ao Processamento de Imagens - UnB]

Algoritmo proposto pelo professor Alexandre Zaghetto - Departamento de ciência da computação, UnB

O algoritmo deve decidir se a região é
1. Segura - Asfalto
2. Não é ideal mas pode ser usada em emergências - grama
3. Completamente inapropriada - Perigo.  

![classes](images/classes.png?raw=true)

A figura abaixo ilustra o diagrama de blocos proposto, cada etapa está desenvolvida em um arquivo da pasta /src.

![diagram](images/diagram.png?raw=true)


+ Extração das features: Cálculo do contraste, correlação, energia e homogeneidade da matriz de co-ocorrência em níveis de cinza da imagem analisada.
+ Seleção de features: Seleção das features que serão utilizadas no conjunto de testes e treinamento através do cálculo da correlação entre elas - features mais descorrelacionadas entre si formam um bom conjunto de testes.
+ Classificação: Utilização de uma matriz de confusão para identificação das classes (não finalizado)

## Instalação e uso

Install python
```
sudo apt-get update
sudo apt-get install python3.6
```

Create a virtual environment called "venv" and activate it
```
python3 -m venv venv
source venv/bin/activate
```

Install the required packages
```
python3 -m pip install -r requirements.txt
```

Run 
```
python3 src/<filename>.py
```