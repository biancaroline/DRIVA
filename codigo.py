import pandas as pd
import matplotlib.pyplot as plt

tb = pd.read_csv('DadosEmpresa.csv')
tb2 = pd.read_csv('DadosEndereco.csv')
# CONCATENAR ARQUIVOS
merged = tb.merge(tb2, on='cnpj')

## Gere um arquivo csv com todas as empresas que tem opção_pelo_simples como SIM
x = tb[tb['opcao_pelo_simples']=='SIM']
x.to_csv('opção_pelo_simples_sim.csv')

## Gere outro arquivo csv que contenha todas as informações das empresas que são de Curitiba ou de Londrina e que tenham capital social maior que 5000 reais
y = merged[((merged['municipio']=='CURITIBA') |(merged['municipio']=='LONDRINA')) & (merged['capital_social']>5000)]
y.to_csv('cwb_ou_ldb_mais5000.csv')

## Faça um gráfico que mostre o total de empresas em cada bairro de Curitiba
z = tb2[tb2['municipio']=='CURITIBA']
z['bairro'].value_counts().plot.bar()
plt.rcParams.update({'font.size': 6})
plt.tight_layout()
plt.show()

##  OUTRA ANÁLISE: Agrupar os municipios pela média da capital social, classificar do menor para o maior e criar histograma de frequência
'''Comentário: A próxima análise foi escolhida para que fosse possível verificar a média do capital social de cada cidade, que em seguida foi classificada por ordem crescente. Para complementá-la, foi criado um histograma de frequências, podendo concluir que mais cidades possuem capital médio baixo do que alto, sendo 96 cidades com média de até 150 mil reais e apenas três com capital maior que 1 milhão de reais.'''

a = merged.groupby('municipio').mean()['capital_social'].sort_values()
#a.to_csv('media_por_municipio.csv')
plt.title('Histograma de frequência', fontsize=20)
plt.xlabel('Média do capital social', fontsize=10)
plt.ylabel('Frequência Absoluta', fontsize=10)
plt.hist(a, 20, range=[0, 3.504400E6], rwidth=0.5,align='mid')
plt.show()

