from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			DIV = (<instance>1|<tagname>DIV</tagname>|<n>CertifyPath</n><v criteria="isequalto">0,DIV,12</v></findby>)
			accountlabelvisibility = (<instance>2|<tagname>DIV</tagname>|<n>INNERTEXT</n><v criteria="isequalto">Account</v></findby>)
			LinkRecaptchaDiv = (<instance>1|<tagname>DIV</tagname>|<n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>className</n><v criteria="isequalto">rc-anchor-center-item rc-anchor-checkbox-holder</v><n>disabled</n><v criteria="isequalto">False</v><n>FrameId</n><v criteria="isequalto">0</v></findby>)
			TextUserName = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="contains">username</v><n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>ID</n><v criteria="doesnotcontain">header</v></findby>)
			PasswordPasswordOld = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="startswith">password</v><n>TYPE</n><v criteria="isequalto">password</v>)
			PasswordConfirmPassword = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">confirmPassword</v><n>TYPE</n><v criteria="isequalto">password</v>)
			PasswordElectronicPin = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">electronicPin</v><n>TYPE</n><v criteria="isequalto">password</v>)
			PasswordReEnterPin = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">reEnterPin</v><n>TYPE</n><v criteria="isequalto">password</v>)
			ComboFirstQuestion = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">firstQ</v><n>ClassName</n><v criteria="isequalto"></v>)
			TextFirstAnswer = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">firstAns</v><n>TYPE</n><v criteria="isequalto">text</v>)
			ComboSecondQuestion = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">secQ</v><n>ClassName</n><v criteria="isequalto"></v>)
			TextSecondAnswer = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">secAns</v><n>TYPE</n><v criteria="isequalto">text</v>)
			LinkSignUp = (<instance>3|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Sign Up</v>)
			LinkCancel = (<instance>2|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Cancel</v>)
			LinkBack = (<instance>2|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Back</v>)
