# QAP 4, Isaac Doyle SD7
# Data files for One stop insurance company.

import datetime
from datetime import timedelta
import FormatValues as FV

# Open OSICDef.dat file and read values into variables

f = open("OSICdef.dat", "r")
POLICY_NUM = int(f.readline())
BASE_RATE = float(f.readline())
ADD_DISC_RATE = float(f.readline())
ADD_LIB_RATE = float(f.readline())
GLASS_COV_RATE = float(f.readline())
LOAN_CAR_RATE = float(f.readline())
HST_RATE = float(f.readline())
PROS_FEE = float(f.readline())
f.close()

#Needed inputs for program
while True:
    CxNameFirst = input("Enter the cx first name: ").title()
    CxNameLast = input("Enter the cx last name: ").title()
    CxAddress = input("Enter the cx address: ").title()
    City = input("Enter the cx city: ").title()
    Prov = input("Enter the cx province: ").title()
    Postal = input("Enter the cx postal code (X1X 1X1):").upper()
    PhoneNum = input("Enter the cx phone number (xxx-xxx-xxxx): ")
    NumCars = int(input("Enter the number of cars being insured: "))
    ExtraLiab = input("Enter whether the cx wants extra liability (Y or N): ").upper()
    OptLoanCar = input("Enter whether optional loaner car (Y or N): ").upper()
    OptGlassCov = input("Enter whether the cx would like additional glass coverage (Y or N): ").upper()
    PayOption = input("Enter whether cx will pay in full or monthly (F or M): ").upper()
    PolicyStartDate = datetime.datetime.now()
    PolicyStartDateDsp = PolicyStartDate.strftime("%Y-%m-%d")
    if PolicyStartDateDsp > "25":
        PolicyStartDateDsp = ((PolicyStartDate.replace(day=1) + timedelta(days=32)).replace(day=1))

#Calculations needed for program
    if NumCars == 1:
        BaseCost = BASE_RATE
    else:
        BaseCost = BASE_RATE * NumCars - (((NumCars - 1) * BASE_RATE) * ADD_DISC_RATE)

    if ExtraLiab == "Y":
        ExtraLibCost = ADD_LIB_RATE * NumCars
    elif ExtraLiab == "N":
        ExtraLibCost = 0
    else:
        break

    if OptGlassCov == "Y":
        OptGlassCost = GLASS_COV_RATE * NumCars
    elif OptGlassCov == "N":
        OptGlassCost = 0
    else:
        break

    if OptLoanCar == "Y":
        OptLoanCost = LOAN_CAR_RATE * NumCars
    elif OptLoanCar == "N":
        OptLoanCost = 0
    else:
        break

    ExtraCost = ExtraLibCost + OptLoanCost + OptGlassCost
    TotInsPrem = ExtraCost + BaseCost
    HST = TotInsPrem * HST_RATE
    TotFullCost = TotInsPrem + HST

    if PayOption == "M":
        MonPayment = (TotFullCost + PROS_FEE) / 8
    else:
        MonPayment = 0

    print("-------------------------------------------")
    print("One Stop Insurance Company Invoice")
    print()
    print(f"{POLICY_NUM}-{CxNameFirst[0]}{CxNameLast[0]} ")
    print(f"{CxAddress:<20s}, {City:<10s}, {Prov:<10s}")
    print(f"{Postal:<6s},     {PhoneNum:<10s}")
    print(f"Policy start Date:               {(PolicyStartDateDsp)}")
    print("-------------------------------------------")
    print(f"Number of vehicles on policy:          {NumCars}")
    print()
    print(f"Cost of Extra liability:           {FV.FDollar2(ExtraLibCost)}")
    print(f"Cost of Loaner car option:         {FV.FDollar2(OptLoanCost)}")
    print(f"Cost of Optional glass coverage:   {FV.FDollar2(OptGlassCost)}")
    print("                                   ---------")
    print(f"Total Cost of extra coverage:      {FV.FDollar2(ExtraCost)}")
    print(f"Cost of base policy:               {FV.FDollar2(BaseCost)}")
    print(f"Total premium cost:                {FV.FDollar2(TotInsPrem)}")
    print(f"HST:                               {FV.FDollar2(HST)}")
    print("                                   ---------")
    print(f"Total cost plus HST (@15%)         {FV.FDollar2(TotFullCost)}")
    if PayOption == "M":
        print(f"Monthly payment                    {FV.FDollar2(MonPayment)}")
    else:
        break
    f = open("Policies.dat", "a")
    f.write("{}, ".format(str(POLICY_NUM)))
    f.write("{}, ".format(CxNameFirst, CxNameLast))
    f.write("{}, ".format(CxAddress))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Prov))
    f.write("{}, ".format(Postal))
    f.write("{}, ".format(PhoneNum))
    f.write("{}, ".format(NumCars))
    f.write("{}, ".format(ExtraLiab))
    f.write("{}, ".format(OptLoanCar))
    f.write("{}, ".format(OptGlassCov))
    f.write("{}, ".format(PayOption))
    f.write("{}\n, ".format(FV.FDollar2(TotFullCost)))
    f.close()
    print()
    print("Policy information processed and saved.")
    POLICY_NUM += 1