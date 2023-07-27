### CLI Based Weather App

> This is a simple CLI based weather app made using Python. It uses the OpenWeatherMap API to fetch the weather data.

```bash
$ python3 main.py --help
usage: main.py [-h] [-city CITY = "Pune"] 
```

1. Clone the repository

```bash
$ git clone https://github.com/rajendrakumaryadav/weatherapp-cli.git
```

2. Install the requirements

```bash
$ pip3 install -r requirements.txt
```

3. Update the config.yaml.example file with your API key and rename it to config.yaml

```bash
mv config.yaml.example config.yaml
```

4. Update the city name in the config.yaml file

> api_key: "your api key" with your own key.

5. You can check the help section for more information using below command.

```bash
$ python3 main.py --help
```

#### Output:

```text
Usage: main.py [OPTIONS]

  This function takes command line parameters as inputs and prints them.

Options:
  --city TEXT  Enter city name
  --help       Show this message and exit.
```

6. Run the script with default city `Pune`.

```bash
$ python3 main.py 
```

#### Output:

```text
Querying weather for Pune.
Please wait...
Weather report for Pune:
Description: heavy intensity rain
Humidity: 76
Pressure: 1008
Wind Speed: 5.55
```

7. Run the script with city name as parameter `Mumbai`.

```bash
$ python3 main.py -city "Mumbai"
```

#### Output:

```text
Querying weather for Mumbai.
Please wait...
Weather report for Mumbai:
Description: moderate rain
Humidity: 100
Pressure: 1007
Wind Speed: 6.17
```

8. Run the script with city name as parameter `Lucknow`.

```bash
$ python3 main.py -city "Lucknow"
```

#### Output:

```text
Querying weather for Lucknow.
Please wait...
Weather report for Lucknow:
Description: haze
Humidity: 62
Pressure: 1000
Wind Speed: 1.54
```

```console
$ info
> Please wait...

--------------------------------
Author: Rajendra Kumar R Yadav
--------------------------------
Location: /home/rajendraryadav
Frameworks: NextJs
Languages: C, PHP, Python, SQL, Typescript, Javascript
---------------------------------
```
With :heart: by Rajendra Kumar Yadav from India.