import click
from covidcharter.service import VirginiaData


@click.command()
@click.option('--county', help='The county or locality to get the graph for')
def graph(county):
    service = VirginiaData()
    try:
        click.echo('Graphing the data...')
        df = service.filter_by_county(county)
        service.plot_data(df)
    except SystemError:
        click.echo("The Virginia Department of Health data is not available at this time, please try again later")
    except ValueError:
        counties = service.get_all_counties()
        click.echo('Please try entering a different county or check the spelling. The covidcharter data chart generator '
                   'requires a county from the following list: %s'
                   % counties)


if __name__ == '__main__':
    graph()
