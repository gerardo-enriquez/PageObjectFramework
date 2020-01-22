from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			RadioQuestion2Answer = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioQuestion3Answer = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioQuestion4Answer = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v>)
			LinkContinue = (<instance>1|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="isequalto">Continue </v>)
			Q1ErrorValidation = (<instance>1|<tagname>DIV</tagname>|<n>INNERTEXT</n><v criteria="isequalto">1) You may have opened a student loan in or around August 2010. Please select the lender you have previously or you are currently making payments to. If you have not received student loan with any of these lenders now or in the past , please select “NONE OF THE ABOVE/DOES NOT APPLY”. * : Error! All questions must be answered to continue.</v>)
			Q2ErrorValdiation = (<instance>1|<tagname>DIV</tagname>|<n>INNERTEXT</n><v criteria="isequalto">2) Which of the following institutions do you have a bank account with? If there is not a matched bank name, please select “NONE OF THE ABOVE”. * : Error! All questions must be answered to continue.</v>)
			Q3ErrorValdiation = (<instance>1|<tagname>DIV</tagname>|<n>INNERTEXT</n><v criteria="isequalto">3) Please select the county of the address you provided. * : Error! All questions must be answered to continue.</v>)
			Q4ErrorValdiation = (<instance>1|<tagname>DIV</tagname>|<n>INNERTEXT</n><v criteria="isequalto">4) You currently or previously resided on one of the following streets. Please select the street name from the following choices. * : Error! All questions must be answered to continue.</v>)
			LinkErrorMessageFieldLevel = (<instance>1|<tagname>DIV</tagname>|<n>INNERTEXT</n><v criteria="contains">Error! Required Field</v>)
