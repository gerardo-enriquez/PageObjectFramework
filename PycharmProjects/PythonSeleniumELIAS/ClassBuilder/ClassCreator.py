import pandas as pd
import os

path = os.getcwd()
os.chdir(path)


file = 'C:/Users/LaxLoba/PycharmProjects/PythonSeleniumELIAS/ClassBuilder/SSPMappingsClassCreator.xlsx'


excel = pd.read_excel(file)
pageNames = excel.PAGENAME.unique()
# numberofrowsperpage = excel.loc[excel['PAGENAME'].isin(["AccountContactInformation"])]
# df = pd.DataFrame(numberofrowsperpage)
# text = []
# pagename = str(df.PAGENAME.unique()).strip("['']")
# print(pagename)
# filename = pagename + '.py'
# f = open(filename,"a")
# f.write("from selenium.webdriver.common.by import By\nfrom selenium.webdriver import ActionChains\nfrom Modules.GenericPageActions import GenericPageActions\n\n\n\n")
# for i in range(0,df.shape[0]):
#     appended = "\t\t\t{} = ({})\n".format(str(list(df.loc[[i], 'ObjectName'].values)).strip("['']"),str(list(df.loc[[i], 'MAP'].values)).strip("['']"))
#     print(appended)
#     f.write(appended)
#
# f.close()

for pageName in pageNames:
    numberofrowsperpage = excel.loc[excel['PAGENAME'].isin([pageName])]
    df = pd.DataFrame(numberofrowsperpage)
    print(df)
    filename = pageName + '.py'
    f = open(filename, "a")
    f.write("from selenium.webdriver.common.by import By\n"
            "from selenium.webdriver import ActionChains\n"
            "from Modules.GenericPageActions import GenericPageActions\n\n\n\n")
    for i in range(0, df.shape[0]):
        appended = "\t\t\t{} = ({})\n".format(str(list(df.loc[[i], 'ObjectName'].values)).strip("['']"),
                                              str(list(df.loc[[i], 'MAP'].values)).strip("['']"))
        print(appended)
        f.write(appended)
    df = df.iloc[0:0]

f.close()