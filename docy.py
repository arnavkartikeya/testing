import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='kid_bot.json')


sh = gc.open_by_key("1rHFWP2wJmcXNDjOezm9y9Ab8pbwl_Qg75ANvHR9jN1w")
wks = sh[0]

def saveFails(fail: str):
    global sh
    global wks
    
    df = pd.DataFrame()
    df["failed responses"] = []
    row1 = []
    row1 = wks.get_col(1)
    if fail in row1:
        return
        print("failed response already exists")
    row1.remove("failed responses")
    row1.append(fail)

    df["failed responses"] = row1

    wks.set_dataframe(df, "A1")