from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			PasswordPassword = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="startswith">password</v><n>TYPE</n><v criteria="isequalto">password</v>)
			PasswordConfirmPassword = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">confirmPassword</v><n>TYPE</n><v criteria="isequalto">password</v>)
			TextFirstName = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">firstName</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextMiddleName = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">middleName</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextLastName = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">lastName</v><n>TYPE</n><v criteria="isequalto">text</v>)
			PasswordElectronicPin = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">electronicPin</v><n>TYPE</n><v criteria="isequalto">password</v>)
			PasswordReEnterPin = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">reEnterPin</v><n>TYPE</n><v criteria="isequalto">password</v>)
			ComboFirstQuestion = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">firstQ</v>)
			TextFirstAnswer = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">firstAns</v><n>TYPE</n><v criteria="isequalto">text</v>)
			ComboSecondQuestion = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">secQ</v>)
			TextSecondAnswer = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">secAns</v><n>TYPE</n><v criteria="isequalto">text</v>)
			LinkSignUp = (<instance>2|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Sign Up</v>)
			LinkCancel = (<instance>2|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Cancel</v>)
