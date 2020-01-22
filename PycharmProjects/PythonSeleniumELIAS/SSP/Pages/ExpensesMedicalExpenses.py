from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			ComboHowOften = (<instance>1|<tagname>SELECT</tagname>|)
			TextHowMuch = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v>)
			TextStartDate = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v>)
			ComboType = (<instance>1|<tagname>SELECT</tagname>|<n>CLASSNAME</n><v criteria="isequalto">hasScript</v><n>INNERTEXT</n><v criteria="isequalto"> Select One Medical Expenses</v>)
