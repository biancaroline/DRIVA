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
plt.show()

##  OUTRAS ANÁLISES
## Gráfico que mostre o total de empresas em curitiba com capital social maior ou igual a 10000 reais
a = merged[(merged['municipio']=='CURITIBA') & (merged['capital_social']>=10000)]
a['bairro'].value_counts().plot.bar()
plt.show()

## Agrupar os municipios pela média da capital social e classificar do menor para o maior 
b = merged.groupby('municipio').mean()['capital_social'].sort_values()
