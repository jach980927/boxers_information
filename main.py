from  app  import read_csv
from  app import charts 
from  app import utils

def run():
    data = read_csv.read_csv('./app/box_csv/fighters.csv')    
    boxer = input('Type name of boxer ==>')
    result = utils.get_boxer_data(data, boxer)
    print(result)
    boxer = result[0]
    labels, values = utils.get_ko_rate(boxer)

    charts.generate_pie_chart(labels, values)


if __name__ == '__main__':
    run()
