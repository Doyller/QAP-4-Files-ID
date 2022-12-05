# matplotlib claim graphing

import matplotlib.pyplot as plt

while True:
    CJan = float(input("Enter the dollar value of claims in January: "))
    CFeb = float(input("Enter the dollar value of claims in February: "))
    CMar = float(input("Enter the dollar value of claims in March: "))
    CApr = float(input("Enter the dollar value of claims in April: "))
    CMay = float(input("Enter the dollar value of claims in May: "))
    CJune = float(input("Enter the dollar value of claims in June: "))
    CJuly = float(input("Enter the dollar value of claims in July: "))
    CAug = float(input("Enter the dollar value of claims in August: "))
    CSept = float(input("Enter the dollar value of claims in September: "))
    COct = float(input("Enter the dollar value of claims in October: "))
    CNov = float(input("Enter the dollar value of claims in November: "))
    CDec = float(input("Enter the dollar value of claims in December: "))
    Jan = "Jan"
    Feb = "Feb"
    Mar = "Mar"
    Apr = "Apr"
    May = "May"
    June = "June"
    July = "July"
    Aug = "Aug"
    Sept = "Sept"
    Oct = "Oct"
    Nov = "Nov"
    Dec = "Dec"

    x = [Jan, Feb, Mar, Apr, May, June, July, Aug, Sept, Oct, Nov, Dec]
    y = [CJan, CFeb, CMar, CApr, CMay, CJune, CJuly, CAug, CSept, COct, CNov, CDec]

    plt.title('Claim amounts month over month')
    plt.scatter(x, y,   color='darkblue', marker='x', label="Monthly claim")
    plt.xlabel("Month")
    plt.ylabel("Dollar Value")
    plt.grid(True)
    plt.legend()
    plt.show()
