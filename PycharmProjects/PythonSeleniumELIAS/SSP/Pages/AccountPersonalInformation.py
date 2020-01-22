from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			TextMiddleName = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">middleName</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextLastName = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">lastName</v><n>TYPE</n><v criteria="isequalto">text</v>)
			ComboSuffix = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">suffix</v><n>ClassName</n><v criteria="isequalto">hasScript</v>)
			TextDateOfBirth = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">dateOfBirth</v><n>TYPE</n><v criteria="isequalto">text</v>)
			LinkSaveandContinue = (<instance>1|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Save and Continue</v>)
			LinkCancel = (<instance>2|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Cancel</v>)
			PasswordSocialSecurityNumberPlaceholder = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">socialSecurityNumberPlaceholder</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextSocialSecurityNumber = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">socialSecurityNumber</v><n>TYPE</n><v criteria="isequalto">text</v>)
			LinkIdentityVerification = (<instance>1|<tagname>DIV</tagname>|<n>INNERTEXT</n><v criteria="contains">REPLACEME</v><n>IsHidden</n><v criteria="isequalto">True</v><n>IsVisible</n><v criteria="isequalto">True</v><n>className</n><v criteria="isequalto">fullrow1</v><n>disabled</n><v criteria="isequalto">False</v></findby>)
			LinkSaveAndContinue = (<instance>1|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Save and Continue</v>)
