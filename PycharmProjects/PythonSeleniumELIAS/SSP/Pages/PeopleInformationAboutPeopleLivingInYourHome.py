from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			CheckProgramMedicaidOrChip = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v>)
			RadioApplyingForBenefitsNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">false</v>)
			RadioApplyingForBenefitsYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">true</v>)
			RadioHelpPayingMedicalBillNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">false</v>)
			RadioHelpPayingMedicalBillYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">true</v>)
			ComboLivingSituation = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="startswith">answerSets0.answers</v><n>Name</n><v criteria="startswith">answerSets[0].answers[</v><n>ClassName</n><v criteria="isequalto">hasScript</v>)
			ComboSuffix = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="startswith">answerSets0.answers</v><n>Name</n><v criteria="startswith">answerSets[0].answers[</v><n>ClassName</n><v criteria="isequalto">hasScript</v>)
			TextFirstName = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>ID</n><v criteria="startswith">answerSets0.answers</v><n>Name</n><v criteria="startswith">answerSets[0].answers[</v>)
			TextLastName = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>ID</n><v criteria="startswith">answerSets0.answers</v><n>Name</n><v criteria="startswith">answerSets[0].answers[</v>)
			TextMiddleName = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>ID</n><v criteria="startswith">answerSets0.answers</v><n>Name</n><v criteria="startswith">answerSets[0].answers[</v>)
			TextNewPersonJoinDate = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v>)
			RadioWhenThePersonReturnYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			RadioWhenThePersonReturnNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			TextPersonReturnDate = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>ID</n><v criteria="startswith">answerSets0.answers</v><n>Name</n><v criteria="startswith">answerSets[0].answers[</v><n>Title</n><v criteria="isequalto">mm/dd/yyyy</v>)
			ComboReasonForLeaving = (<instance>1|<tagname>SELECT</tagname>|)
			LinkPregnantorNewbornMedicallBill = (<instance>1|<tagname>LEGEND</tagname>|<n>TAGNAME</n><v criteria="isequalto">LEGEND</v><n>INNERTEXT</n><v criteria="startswith">If this person was pregnant or under age 1 in the last 3 calendar months, does this person need help paying medical bills from those months</v>)
			RadioPregnantNewbornMedicalBillYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">true</v>)
			RadioPregnantNewbornMedicalBillNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">false</v>)
			LinkSaveAndContinue = (<instance>1|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="contains">Save and Continue</v></findby>)
