import requests
import ssl
import difflib
import jellyfish


def getStateGasPrice(apiKEY, state):
    """
    Docstring:
    This function takes in the apiKEY and the state and returns the gas price information
    of the state.

    """
    capitalizedState = state.upper()
    state = {
        "state": capitalizedState
    }
    url = "https://gas-price.p.rapidapi.com/stateUsaPrice"

    headers = {
        "X-RapidAPI-Key": apiKEY,
        "X-RapidAPI-Host": "gas-price.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=state, timeout=2.5)

    return response.json()["result"]["state"]


def getTypeOfFuelAndPrice(stateGasData, dieselOrGasoline, typeOfGasoline):
    """
    This function will take in the stateGasData from the API request
    The type of fuel the user wants with their care they are comparing
    and then the octane type of their gasoline if not diesel
    this information is then used to return the price of the fuel out of the 
    api response dictionary
    """
    dieselOrGasoline = dieselOrGasoline.lower()
    typeOfGasoline = typeOfGasoline.lower()

    fuelCost = 0
    if dieselOrGasoline != "diesel":
        if typeOfGasoline == "mid":
            fuelCost = stateGasData["midGrade"]
        elif typeOfGasoline == "regular":
            fuelCost = stateGasData["gasoline"]
        else:
            fuelCost = stateGasData["premium"]
    else:
        fuelCost = stateGasData[dieselOrGasoline]
    return fuelCost


def closestMatchingBrandName(brandName, maintenance_costs):
    """
    This function will take in the carBrand and then compare it to the brand names
    in the maintenance_costs dictionary. It will then return the top 3 closest matches
    It will return a dictionary with the index of the brand name and the brand name
    The user ultimately will need to tell us which index they want to use
    """
    carBrand = brandName.lower()

    # Calculate Levenshtein Distance between the input and each brand in the dictionary
    distances = {brand: jellyfish.levenshtein_distance(
        carBrand, brand.lower()) for brand in maintenance_costs}

    # Sort the brands by the Levenshtein Distance in ascending order (lower is better)
    sorted_brands = sorted(distances, key=distances.get)[:3]

    brandCodes = {
    }
    for x in range(0, len(sorted_brands), 1):
        brandCodes[x] = sorted_brands[x]

    # Return the top 3 closest matches
    return brandCodes


def calculate_car_loan_monthly_cost(principal, interest_rate, loan_term,
                                    down_payment, trade_in_value, tax_rate):
    """
    Calculate the monthly payment for a car loan including taxes and interest.

    Parameters:
    principal (float): The total price of the car.
    interest_rate (float): The annual interest rate of the loan.
    loan_term (float): The total duration of the loan in years.
    down_payment (float): The down payment made on the car.
    trade_in_value (float): The value of the trade-in, if any.
    tax_rate (float): The sales tax rate for the car purchase.

    Returns:
    float: The monthly payment for the car loan.
    """
    tax_rate = tax_rate / 100
    # Adjust principal for down payment and trade-in value
    adjusted_principal = principal - trade_in_value - down_payment

    # Calculate tax amount and add to the adjusted principal
    tax_amount = adjusted_principal * tax_rate
    principal_with_tax = adjusted_principal + tax_amount

    # Convert annual interest rate to monthly and loan term to months
    monthly_interest_rate = (interest_rate / 100) / 12
    total_loan_term_months = loan_term * 12

    # Monthly payment calculation using the formula for an amortized loan
    if monthly_interest_rate == 0:  # To handle the case when the interest rate is 0
        monthly_payment = principal_with_tax / total_loan_term_months
    else:
        monthly_payment = (principal_with_tax * monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate)
                           ** -total_loan_term_months)

    return monthly_payment
