import mftool
import pandas as pd
from datetime import date
# Replace 'path/to/your/file.xlsx' with the actual path to your Excel file in Google Drive
# df = pd.read_excel('/content/drive/My Drive/finance/msesaransh.xlsx') 
# print(df)
# 120492;INF192K01CC7;-;JM Flexicap Fund (Direct) - Growth Option;120.9389;23-Aug-2024
# 150597;INF769K01IS5;-;Mirae Asset Global X Artificial Intelligence & Technology ETF Fund of Fund - Direct Plan- Growth;17.569;23-Aug-2024
# 152430;INF179KC1IC4;-;HDFC NIFTY200 Momentum 30 Index Fund - Direct Plan;12.277;23-Aug-2024
# 120351;INF767K01GW5;-;LIC MF Infrastructure Fund-Direct Plan-Growth;58.596;23-Aug-2024
import requests
def find_line_in_url(url, search_string):
  response = requests.get(url)
  if response.status_code == 200:
    for line in response.text.splitlines():
      if search_string in line:
        print(line)
  return None

# url = "https://raw.githubusercontent.com/NayakwadiS/mftool/master/data/Scheme_codes.txt"
# url = "https://www.amfiindia.com/spages/NAVAll.txt"

#scheme_code = "152430"  # Replace with the desired scheme code
#start_date = "01-Jan-2023"  # Replace with your desired start date

mf = mftool.Mftool()
# Fetch historical NAV data up to today
#df = mf.get_scheme_historical_nav(scheme_code, as_Dataframe=True)

def getPerCent(df, curIdx, rowIdx):
  curNav = float(df.iloc[curIdx]['nav'])
  rowNav = float(df.iloc[rowIdx]['nav'])
  if rowNav == 0:
    return 1000
  perCent = ((curNav - rowNav) / rowNav*100)
  # print(perCent, curNav, rowNav)
  return perCent

def printStat(df, curIdx, rowIdx):
  if ((curIdx == -1) or (rowIdx == -1)):
    print("No returns")
    return
  perCent = getPerCent(df, curIdx, rowIdx)
  rowNav = float(df.iloc[rowIdx]['nav'])
  curNav = float(df.iloc[curIdx]['nav'])
  print (df.index[rowIdx], rowNav, df.index[curIdx], curNav, f"{perCent:.2f}")

def findHighIndexInDF(df, curIdx, perCent):
  for index, row in df.iterrows():
    rowIdx = df.index.get_loc(index)
    if getPerCent(df, curIdx, rowIdx) > perCent:
      return (curIdx, rowIdx)
  return (curIdx, -1)

def findLowIndexInDF(df, curIdx, perCent):
  for index, row in df.iterrows():
    rowIdx = df.index.get_loc(index)
    if getPerCent(df, curIdx, rowIdx) < perCent:
      return (curIdx, rowIdx)
  return (curIdx, -1)

mfList = ["107763", "120351", "120350", "107763", "107764"]
# Fetch historical NAV data up to today
df = mf.get_scheme_historical_nav(mfList[0], as_Dataframe=True)
df2 = mf.get_scheme_details(mfList[0])
print(df2)
curIdx, highIdx = (findHighIndexInDF(df, 0, 9))
printStat(df, curIdx, highIdx)
curIdx, lowIdx = (findLowIndexInDF(df, 0, -3))
printStat(df, curIdx, lowIdx)
