Para extrair os dados deve-se estar dentro desse caminho 'src/extract' e efetuar o seguinte comando:

```bash
scrapy crawl mercadolivre -o ../../../data/bronze/data.jsonl
```

Após extrair os dados para a camada bronze precisamos efetuar algumas transformações antes de colocá-los na camada silver. Para iniciar o script de transformação, execute no caminho 'src/transform' o comando:

```bash
python main.py
```

Agora podemos subir um servidor e plotar um gráfico para visualizar os dados em um dashboard, para isso, precisamos estar no diretorio 'src/dashboard' e executar o seguinte comando:

```bash
streamlit run app.py
```

