from utilityProjectA import *
from apiKeyProjectA import apiKEY
from costOfMaintenanceProjectA import maintenance_costs


def getCarEffiencyStats():
    highwayEfficiency = input("Enter the highway efficiency of the vehicle: ")
    highwayEfficiency = float(highwayEfficiency)

    cityEfficiency = input("Enter the city efficiency of the vehicle: ")
    cityEfficiency = float(cityEfficiency)

    carGallonsInTank = input("Enter the number of gallons in the tank: ")
    carGallonsInTank = float(carGallonsInTank)
    print("Highway Efficiency", highwayEfficiency,
          "City Efficiency", cityEfficiency,
          )

    return highwayEfficiency, cityEfficiency, carGallonsInTank


def getUserDrivingPatterns():
    cityMilesDriveWeekdays = input(
        "Enter the number of city miles you drive on weekdays: ")
    cityMilesDriveWeekdays = float(cityMilesDriveWeekdays)

    highwayMilesDriveWeekdays = input(
        "Enter the number of highway miles you drive on weekdays: ")
    highwayMilesDriveWeekdays = float(highwayMilesDriveWeekdays)

    cityMilesDriveWeekends = input(
        "Enter the number of city miles you drive on weekends: ")
    cityMilesDriveWeekends = float(cityMilesDriveWeekends)

    highwayMilesDriveWeekends = input(
        "Enter the number of highway miles you drive on weekends: ")
    highwayMilesDriveWeekends = float(highwayMilesDriveWeekends)

    cityMilesDrive = cityMilesDriveWeekdays + cityMilesDriveWeekends
    highwayMilesDrive = highwayMilesDriveWeekdays + highwayMilesDriveWeekends

    cityMilesDrive = cityMilesDrive * 52
    highwayMilesDrive = highwayMilesDrive * 52

    monthlyCityMiles = cityMilesDrive / 12
    monthlyHighwayMiles = highwayMilesDrive / 12

    totalYearlyMiles = cityMilesDrive + highwayMilesDrive
    yearsTo75K = 75000 / totalYearlyMiles

    print("Monthly City Miles", monthlyCityMiles,
          "Monthly Highway Miles", monthlyHighwayMiles,
          )
    return yearsTo75K, monthlyCityMiles, monthlyHighwayMiles


def getUserDrivingDemographics(yearsTo75K, carBrand):
    stateLivingIn = input("Enter the state you live in: ")
    dieselOrGasoline = input("Is the car Diesel or Gas?: ").lower()
    typeOfGasoline = input(
        "Octane of Gasoline - Mid, Regular, or Premium?: ").lower()

    # stateGasData = getStateGasPrice(apiKEY, stateLivingIn)
    fuelCostPerGallon = float(input("Enter the gas price of your state: "))
    # fuelCostPerGallon = getTypeOfFuelAndPrice(
    #     stateGasData, dieselOrGasoline, typeOfGasoline)
    # print("Fuel Cost", fuelCostPerGallon)
    matchingBrands = closestMatchingBrandName(carBrand, maintenance_costs)
    print("TYPEEE", type(matchingBrands))
    userBrandIDPick = int(
        input(f"{matchingBrands} - Enter the index of the brand you want to use: "))
    finalBrandName = list(matchingBrands.values())[userBrandIDPick]
    costTo75k = maintenance_costs[finalBrandName]
    oneYearCost = costTo75k / yearsTo75K
    monthlyMaintenanceCostOneYear = oneYearCost / 12
    print("Monthly Maintenance Cost One Year", monthlyMaintenanceCostOneYear,
          "Fuel Cost Per Gallon", fuelCostPerGallon)
    return fuelCostPerGallon, monthlyMaintenanceCostOneYear


def getUserLoanDetails():
    carPrincipal = float(input("Enter the principal of the car: "))
    carInterestRate = float(input("Enter the interest rate of the car: "))
    carLoanTerm = float(input("Enter the loan term of the car: "))
    carDownPayment = float(input("Enter the down payment of the car: "))
    carTradeInValue = float(input("Enter the trade in value of the car: "))
    carTaxRate = float(input("Enter the tax rate of the car: "))
    monthlyLoanPayments = calculate_car_loan_monthly_cost(carPrincipal, carInterestRate, carLoanTerm,
                                                          carDownPayment, carTradeInValue, carTaxRate)
    print("Monthly Loan Payments", monthlyLoanPayments)
    return monthlyLoanPayments


def calculateGallonsNeededPerMonth(fuelCostPerGallon, monthlyCityMiles, monthlyHighwayMiles, cityEfficiency, highwayEfficiency):
    gallonsCity = monthlyCityMiles / cityEfficiency
    cityGallonsMonthly = gallonsCity
    gallonsHighway = monthlyHighwayMiles / highwayEfficiency
    highwayGallonsMonthly = gallonsHighway
    totalGallonsMonthly = cityGallonsMonthly + highwayGallonsMonthly
    totalGasCostMonthly = totalGallonsMonthly * fuelCostPerGallon
    print("Total Gas Cost Monthly", totalGasCostMonthly)
    return totalGasCostMonthly
