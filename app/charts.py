import matplotlib.pyplot as plt


def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig('charts/bar.png')


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('charts/pie.png')


if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [50, 89, 301]
  generate_pie_chart(labels, values)
