import sys
from datetime import date
from gs_quant.data import Dataset
from gs_quant.markets.securities import SecurityMaster, AssetIdentifier
from gs_quant.session import GsSession
import pandas as pd

itdoesntmatterjustdowhatever = open("data_raw.txt", 'w')
#sys.stdout = itdoesntmatterjustdowhatever

client_id = "b2a0a48a91854045b5c7eb12c8973901"
client_secret = "2cb4ec68204ddee53a1a892ea70ee110bc5db9c30aa04024336d69ea9e4fafc6"

scopes = GsSession.Scopes.get_default()
GsSession.use(client_id = client_id, client_secret = client_secret, scopes = scopes)

ds = Dataset("USCANFPP_MINI")

gsids = ds.get_coverage()["gsid"].values.tolist()
data = ds.get_data(date(2017, 1, 15), date(2018, 1, 15), gsid=gsids[0:5])

print(data.head())

for idx, row in data.iterrows():
    marqueeAssetId = row["assetId"]
    asset = SecurityMaster.get_asset(marqueeAssetId, AssetIdentifier.MARQUEE_ID)
    data.loc[data["assetId"] == marqueeAssetId, "assetName"] = asset.name

print(data.head())
itdoesntmatterjustdowhatever.write(data.to_string())
