from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			CheckREPParentalControl = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">textMessage</v><n>TYPE</n><v criteria="isequalto">checkbox</v>)
			ComboREPRelationship = (<instance>REPLACEME|<tagname>SELECT</tagname>|<n>INNERTEXT</n><v criteria="contains">Select One Aunt/Uncle</v>)
			TextREPStartDate = (<instance>1|<tagname>INPUT</tagname>|<n>CLASSNAME</n><v criteria="isequalto">hasDatepicker</v><n>OUTERHTML</n><v criteria="contains">relationshipStartDate</v><n>TYPE</n><v criteria="isequalto">text</v>)
