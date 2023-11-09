from calculators import *


numberOfComparisons = int(
    input("Enter the number of vehicles you want to compare: "))


costsPerVehicle = {}


for i in range(numberOfComparisons):
    carBrandNormal = input("Enter the brand of the car: ")
    carBrand = carBrandNormal.lower()
    costsPerVehicle[carBrand] = 0
    highwayEfficiency, cityEfficiency, carGallonsInTank = getCarEffiencyStats()
    yearsTo75K, monthlyCityMiles, monthlyHighwayMiles = getUserDrivingPatterns()
    fuelCostPerGallon, monthlyMaintenanceCostOneYear = getUserDrivingDemographics(
        yearsTo75K, carBrand)
    monthlyLoanPayments = getUserLoanDetails()
    totalGasCostMonthly = calculateGallonsNeededPerMonth(
        fuelCostPerGallon, monthlyCityMiles, monthlyHighwayMiles, cityEfficiency, highwayEfficiency)

    totalCarMonthlyCosts = monthlyLoanPayments + \
        monthlyMaintenanceCostOneYear + totalGasCostMonthly
    costsPerVehicle[carBrandNormal] = totalCarMonthlyCosts
    print(totalCarMonthlyCosts, "for the ", carBrandNormal)


print(costsPerVehicle)

# compare the cars saved in costsPerVehicle and give the car with the lowest payment
# get max value from dictionary and the key associated with it
print("The best car to buy going off of payments alone is the",
      min(costsPerVehicle, key=costsPerVehicle.get))
