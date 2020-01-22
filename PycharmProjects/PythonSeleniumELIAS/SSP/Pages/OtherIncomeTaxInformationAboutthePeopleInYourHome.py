from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			TextDependentNames = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v>)
			RadioClaimDependentNotListedNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioClaimDependentNotListedYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			RadioClaimAsDependentNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioClaimAsDependentYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			ComboFilingStatus = (<instance>1|<tagname>SELECT</tagname>|)
			ComboJointFiler = (<instance>1|<tagname>SELECT</tagname>|)
			ComboWhoWillClaim = (<instance>1|<tagname>SELECT</tagname>|)
			ComboHowManyDependentsNotListed = (<instance>1|<tagname>SELECT</tagname>|)
			GenericTaxApplicantName = (<instance>1|<tagname>B</tagname>|<n>tagName</n><v criteria="isequalto">B</v>)
			LinkGenericName = (<instance>1|<tagname>B</tagname>|<n>OUTERHTML</n><v criteria="startswith"><B></v><n>TAGNAME</n><v criteria="isequalto">B</v>)
