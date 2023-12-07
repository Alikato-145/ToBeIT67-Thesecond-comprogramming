university ={
    "KMITL":"King Mongkut's Institute of Technology Ladkrabang",
    "RU":"Ramkhamhaeng University",
    "KMUTT":"King Mongkut's University of Technology Thonburi",
    "TU":"Thammasat University",
    "KKU":"Khon Kaen University",
    "PSU":"Prince of Songkla University",
    "KU":"Kasetsart University",
    "CMU":"Chiang Mai University",
    "CU":"Chulalongkorn University",
    "MU":"Mahidol University",
}
name = input()
name = name.upper()
if name in university:
    print(university[name])
if  name not in university:
    print("Error")