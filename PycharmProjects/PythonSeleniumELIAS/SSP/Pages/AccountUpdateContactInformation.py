from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			CheckTextMessage = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">textMessage</v><n>TYPE</n><v criteria="isequalto">checkbox</v>)
			ComboHomeState = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">state</v><n>ClassName</n><v criteria="isequalto"></v>)
			ComboMailState = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">mailState</v>)
			LinkBack = (<instance>2|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Back</v>)
			LinkCancel = (<instance>2|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Cancel</v>)
			LinkSaveandContinue = (<instance>1|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Save and Continue</v>)
			RadioHasHomeNo = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">hasHome2</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioHasHomeYes = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">hasHome1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioMailingSameAsHomeNo = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">sameAddress2</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioMailingSameAsHomeYes = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">sameAddress1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioOptOutPaperMailingNo = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">optInOutStatus2</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioOptOutPaperMailingYes = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">optInOutStatus1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			TextEmail = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">email</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextHomeAddressLine1 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">addressLine1</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextHomeAddressLine2 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">addressLine2</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextHomeCity = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">city</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextHomePhoneNumber = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">homePhoneNumber</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextMailAddressLine1 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">mailAddressLine1</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextMailAddressLine2 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">mailAddressLine2</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextMailCity = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">mailCity</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextMailZipcode = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">mailZipcode</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextMobilePhoneNumber = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">mobilePhoneNumber</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextHomeZipCode = (<instance>1|<tagname>input</tagname>|<n>name</n><v criteria="isequalto">zipcode</v><n>id</n><v criteria="isequalto">zipcode</v><n>type</n><v criteria="isequalto">text</v></findby>)
