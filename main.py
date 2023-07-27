import click

import weather


@click.command()
@click.option('--city', help='Enter city name', default='Pune')
def entry(city):
    """This function takes command line parameters as inputs and prints them."""
    print(f"Querying weather for {city}.")
    print("Please wait...")
    information = weather.get_weather(city)
    print(information)


if __name__ == '__main__':
    entry()
