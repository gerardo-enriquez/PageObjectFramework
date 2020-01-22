from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			RadioRenewEligibilityAutomaticallyNo = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">autoRenewEligFalse</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioRenew5Years = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">applicationDetailBean.yearsAutoRenewElig1</v><n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">5</v>)
			CheckSign = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">checktoSign</v><n>TYPE</n><v criteria="isequalto">checkbox</v>)
			TextName = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>CLASSNAME</n><v criteria="isequalto">signatureBox</v>)
			ComboDescription = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="contains">role</v>)
			RadioSignWithPIN = (<instance>1|<tagname>INPUT</tagname>|<n>NAME</n><v criteria="isequalto">pinRadio</v><n>ID</n><v criteria="isequalto">radio</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			CheckPINSignOLD = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">textMessage</v><n>TYPE</n><v criteria="isequalto">checkbox</v>)
			PasswordPIN = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">pin</v><n>TYPE</n><v criteria="isequalto">password</v>)
			ComboPINDescription = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">rolePin</v>)
			RadioRenew4Years = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">applicationDetailBean.yearsAutoRenewElig2</v><n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">4</v>)
			RadioRenew3Years = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">applicationDetailBean.yearsAutoRenewElig3</v><n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">3</v>)
			RadioRenew2Years = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">applicationDetailBean.yearsAutoRenewElig4</v><n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">2</v>)
			RadioRenew1Year = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">applicationDetailBean.yearsAutoRenewElig5</v><n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">1</v>)
			TextNonApplicantFirstName = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">firstName</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextNonApplicantMiddleName = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">middleName</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextNonApplicantLastName = (<instance>1|<tagname>INPUT</tagname>|<n>NAME</n><v criteria="isequalto">lastName</v><n>TYPE</n><v criteria="isequalto">text</v>)
			ComboNonApplicantRelation = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">relation</v>)
			TextNonApplicantHomePhone = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">homePhone</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextNonApplicantOtherPhone = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">otherPhone</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextNonApplicantSuffix = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">suffix</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextNonApplicantEmailAddress = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">emailAddress</v><n>TYPE</n><v criteria="isequalto">text</v>)
			TextNonApplicantAddressLine1 = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v>)
			TextNonApplicantAddressLine2 = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v>)
			TextNonApplicantCity = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v>)
			ComboNonApplicantState = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">state</v>)
			TextNonApplicantZipcode = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v>)
			CheckPINSign = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">pinCheckbox</v></findby>)
			TextPIN = (<instance>1|<tagname>INPUT</tagname>|<n>NAME</n><v criteria="isequalto">pin</v><n>ID</n><v criteria="isequalto">pin</v>)
