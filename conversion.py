# Define conversion categories and their units
conversion_categories = {
    "Length": {
        "meters": ["kilometers", "feet", "yards", "miles", "inches"],
        "kilometers": ["meters", "miles"],
        "miles": ["kilometers", "meters", "feet", "yards"],
        "yards": ["meters", "feet", "inches", "miles"],
        "feet": ["meters", "yards", "inches", "miles"],
        "inches": ["meters", "feet", "yards"]
    },
    "Energy": {
        "joules": ["kilojoules", "calories", "kilocalories"],
        "kilojoules": ["joules", "calories"],
        "calories": ["joules", "kilocalories"],
        "kilocalories": ["joules", "calories"]
    },
    "Speed": {
        "meters_per_second": ["kilometers_per_hour", "miles_per_hour"],
        "kilometers_per_hour": ["meters_per_second", "miles_per_hour"],
        "miles_per_hour": ["meters_per_second", "kilometers_per_hour"]
    },
    "Temperature": {
        "celsius": ["fahrenheit", "kelvin"],
        "fahrenheit": ["celsius", "kelvin"],
        "kelvin": ["celsius", "fahrenheit"]
    },
    "Time": {
        "seconds": ["minutes", "hours", "days"],
        "minutes": ["seconds", "hours", "days"],
        "hours": ["seconds", "minutes", "days"],
        "days": ["seconds", "minutes", "hours"]
    },
    "Mass": {
        "grams": ["kilograms", "pounds", "ounces"],
        "kilograms": ["grams", "pounds"],
        "pounds": ["grams", "kilograms", "ounces"],
        "ounces": ["grams", "pounds"]
    },
    "Volume": {
        "liters": ["milliliters", "gallons"],
        "milliliters": ["liters"],
        "gallons": ["liters"]
    },
    "Pressure": {
        "pascals": ["kilopascals", "bars", "atmospheres"],
        "kilopascals": ["pascals", "bars"],
        "bars": ["pascals", "kilopascals", "atmospheres"],
        "atmospheres": ["pascals", "bars"]
    },
    "Frequency": {
        "hertz": ["kilohertz", "megahertz"],
        "kilohertz": ["hertz", "megahertz"],
        "megahertz": ["hertz", "kilohertz"]
    }
}