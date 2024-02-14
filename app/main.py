import utils
import read_csv
import charts
import pandas as pd


def run():
  '''
  data = list(
      filter(lambda country: country['Continent'] == 'South America', data))
  country = input('Escribe un pais:\n ')

  '''
  dataFrames =  pd.read_csv('./data.csv' )
  dataFrames = dataFrames[dataFrames['Continent'] == 'Africa']

  country = dataFrames['Country/Territory'].values
  porcetages = dataFrames['World Population Percentage'].values

  charts.generate_pie_chart(country, porcetages)

  result = utils.populationByCountry(country, country)

  if (len(result) > 0):
    labels, values = utils.get_population_by_country(result)
    charts.generate_bar_chart(labels, values)

  labels = list(
      map(
          lambda x: x['Country/Territory'] + '\n' + x[
              'World Population Percentage'], data))
  world_population = list(map(lambda x: x['World Population Percentage'],
                              data))
  if len(labels) > 0:
    charts.generate_pie_chart(labels, world_population)


if __name__ == '__main__':
  run()
