from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			RadioUserEnteredMailingAddress = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">mailingAddressIndex0</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioNormalizedHomeAddress = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">homeAddressIndex1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioNormalizedMailingAddress = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">mailingAddressIndex1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			ComboHomeAddressCounty = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">homeAddressLst0.county</v><n>ClassName</n><v criteria="isequalto"></v>)
			ComboMailingAddressCounty = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">mailingAddressLst0.county</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>type</n><v criteria="isequalto">select-one</v></findby>)
			Save and Continue = (<instance>1|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Save and Continue</v>)
			Back = (<instance>2|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Back</v>)
