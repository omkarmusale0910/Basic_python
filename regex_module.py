text="""According to the International Monetary Fund (IMF), the Indian economy in 2022 was nominally worth $3.46 trillion; it was the fifth-largest economy by market exchange rates, and is around $11.6 trillion, the third-largest by purchasing power parity (PPP).[304] With its average annual GDP growth rate of 5.8% over the past two decades, and reaching 6.1% during 2011-2012,[305] India is one of the world's fastest-growing economies.[306] However, the country ranks 139th in the world in nominal GDP per capita and 118th in GDP per capita at PPP.[307] Until 1991, all Indian governments followed protectionist policies that were influenced by socialist economics. Widespread state intervention and regulation largely walled the economy off from the outside world. An acute balance of payments crisis in 1991 forced the nation to liberalise its economy;[308] since then it has moved slowly towards a free-market system[309][310] by emphasising both foreign trade and direct investment inflows.[311] India has been a member of World Trade Organization since 1 January 1995.[312]
$50 value $0.25
"""


import re

# remove [123] type substring from 

text_new=re.sub(r'\[\d{3}\]','',text)
print(text_new)

# find GDP grow in %

# finding after $ number
reg1=r'\$(\d*\.\d*)'
reg2=r'\$(\d* )'

money=re.findall(reg1,text_new)
money1=re.findall(reg2,text_new)
print(money,money1)

reg3=r'\$(\d*(?:\.\d)?)'
money3=re.findall(reg3,text_new)
print(money3)


