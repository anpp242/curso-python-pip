import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('./data.csv')
  data = list(
      filter(lambda country: country['Continent'] == 'South America', data))
  country = input('Escribe un pais:\n ')

  result = utils.populationByCountry(data, country)

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
