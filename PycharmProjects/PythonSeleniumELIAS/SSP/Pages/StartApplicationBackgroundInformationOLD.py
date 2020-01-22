from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			LabelQuestionTextForEditbox = (<instance>1|<tagname>LABEL</tagname>|<n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>innerTEXT</n><v criteria="doesnotcontain">DoesNotContainText</v><n>innerTEXT</n><v criteria="contains">StartAtText</v><n>for</n><v criteria="doesnotcontain">answerValue1</v><n>for</n><v criteria="doesnotcontain">answerValue2</v></findby>)
			ComboPreferredLanguage(1) = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers5.answerValue</v><n>CLASSNAME</n><v criteria="isequalto">hasScript</v>)
			RadioStateResidentYes(1) = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers1.answerValue2</v><n>TYPE</n><v criteria="isequalto">radio</v><n>CLASSNAME</n><v criteria="isequalto">hasScript</v>)
			RadioUSCitizenNationalNo(1) = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers1.answerValue1</v><n>TYPE</n><v criteria="isequalto">radio</v><n>CLASSNAME</n><v criteria="isequalto">hasScript</v>)
			Link_Yes = (<instance>1|<tagname>SPAN</tagname>|<n>INNERTEXT</n><v criteria="isequalto">No</v>)
			RadioI94Number = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">I-94 Number</v>)
			RadioAlienNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Alien Number</v>)
			ComboImmigrationStatus = (<instance>1|<tagname>SELECT</tagname>|)
			RadioLivedInUSSince1996Yes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			RadioLivedInUSSince1996No = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			INSI94Number = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v>)
			INSPassportNumber = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers92.answerValue</v>)
			INSSevisIDNumber = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers109.answerValue</v>)
			INSDocExpirationDate = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers127.answerValue</v><n>CLASSNAME</n><v criteria="isequalto">date-format-class hasDatepicker</v>)
			INSAlienNumber = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers76.answerValue</v>)
			INSIDNumber = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers66.answerValue</v>)
			INSCertificateOfCitizenshipNumber = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers119.answerValue</v>)
			INSCountryOfCitizenship = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers103.answerValue</v>)
			ComboCountryofCitizenship = (<instance>1|<tagname>SELECT</tagname>|<n>ClassName</n><v criteria="isequalto">hasScript</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v><n>name</n><v criteria="startswith">answerSets[0].answers[</v></findby>)
			TextCardNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextNaturalizedCertificationNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextAlienNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">ReplaceID</v></findby>)
			TextCertificationofCitizenshipNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextDocument/PassportExpirationDate = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v><n>name</n><v criteria="startswith">answerSets[0].answers[</v></findby>)
			TextSEVISID = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0</v></findby>)
			TextPassportNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v><n>NAME</n><v criteria="startswith">answerSets[0].answers[</v></findby>)
			TextVisaNumber = (<instance>1|<tagname>INPUT</tagname>|<n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextI94Number = (<instance>1|<tagname>INPUT</tagname>|<n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">ReplaceID</v></findby>)
			RadioActiveMilitaryMemberNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			RadioActiveMilitaryMemberYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			RadioSameNameOnDocumentNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>CLASSNAME</n><v criteria="isequalto">hasScript</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			RadioSameNameOnDocumentYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>CLASSNAME</n><v criteria="isequalto">hasScript</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			CheckRaceAmericanNative = (<instance>1|<tagname>input</tagname>|<n>type</n><v criteria="isequalto">checkbox</v><n>classname</n><v criteria="isequalto">hasScript</v><n>Value</n><v criteria="isequalto">American Indian or Alaskan Native</v></findby>)
			CheckRaceAsian = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>value</n><v criteria="isequalto">Asian</v></findby>)
			CheckRaceBlack = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>value</n><v criteria="isequalto">Black or African American</v></findby>)
			CheckRaceHispanic = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>value</n><v criteria="isequalto">Hispanic or Latino</v></findby>)
			CheckRaceNativeHawaiian = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>value</n><v criteria="isequalto">Native Hawaiian or Other Pacific Islander</v></findby>)
			CheckRaceUnknown = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>value</n><v criteria="isequalto">Unknown</v></findby>)
			CheckRaceWhite = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>value</n><v criteria="isequalto">White</v></findby>)
			ComboCitizenshipStatus = (<instance>1|<tagname>SELECT</tagname>|)
			ComboDocumentType = (<instance>1|<tagname>SELECT</tagname>|<n>ClassName</n><v criteria="isequalto">hasScript</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			ComboPreferredLanguage = (<instance>1|<tagname>SELECT</tagname>|<n>ClassName</n><v criteria="startswith">hasScript</v><n>innerText</n><v criteria="contains">Select One EnglishAfghaniAmerican</v></findby>)
			RadioBornInUsNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioBornInUsYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			RadioChildSupportNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers10.answerValue2</v></findby>)
			RadioChildSupportYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers10.answerValue1</v></findby>)
			RadioActiveMilitaryMemberYesOld = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			RadioActiveMilitaryMemberNoOld = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioEligibleImmigrationNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers19.answerValue2</v></findby>)
			RadioEligibleImmigrationYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers19.answerValue1</v></findby>)
			RadioLanguageAssistanceNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers6.answerValue2</v></findby>)
			RadioLanguageAssistanceYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers6.answerValue1</v></findby>)
			RadioFosterCareNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers7.answerValue2</v></findby>)
			RadioFosterCareYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers7.answerValue1</v></findby>)
			RadioHaveInsuranceNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers12.answerValue2</v></findby>)
			RadioHaveInsuranceYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers12.answerValue1</v></findby>)
			RadioLivedInUSSince1996NoOld = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioLivedInUSSince1996YesOld = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			RadioSameNameOnDocumentNoOld = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioSameNameOnDocumentYesOld = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			RadioParentLivingOutsideNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers11.answerValue2</v></findby>)
			RadioParentLivingOutsideYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers11.answerValue1</v></findby>)
			RadioStateResidentNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>ID</n><v criteria="isequalto">answerSets0.answers1.answerValue2</v></findby>)
			RadioStateResidentYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>ID</n><v criteria="isequalto">answerSets0.answers1.answerValue1</v></findby>)
			TextDateOfEntry = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>Title</n><v criteria="isequalto">mm/dd/yyyy</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextFirstName = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextIDNumber = (<instance>1|<tagname>INPUT</tagname>|<n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextInsuranceEndDate = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers13.answerValue</v></findby>)
			TextInsuranceEndReason = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers14.answerValue</v></findby>)
			TextLastName = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextMiddleName = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextOtherEthnicGroup = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v>)
			TextResidentSince = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v>)
			ComboSectionCode = (<instance>1|<tagname>SELECT</tagname>|<n>ClassName</n><v criteria="isequalto">hasScript</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>innerHTML</n><v criteria="contains"><option value="">Select One</option></v><n>id</n><v criteria="startswith">answerSets0.answers</v><n>name</n><v criteria="startswith">answerSets[0].answers[</v><n>innertext</n><v criteria="contains">ReplaceInnerText</v></findby>)
			ComboEthnicGroupAsian = (<instance>1|<tagname>SELECT</tagname>|<n>INNERTEXT</n><v criteria="contains">Asian Indian</v>)
			ComboEthnicGroupMexican = (<instance>1|<tagname>SELECT</tagname>|<n>INNERTEXT</n><v criteria="contains">Mexican American</v>)
			ComboEthnicGroupHawaiian = (<instance>1|<tagname>SELECT</tagname>|<n>INNERTEXT</n><v criteria="contains">Guamanian</v>  )
			RadioUSCitizenNationalYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			RadioUSCitizenNationalNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioNaturalizedCitizenNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers16.answerValue2</v></findby>)
			RadioNaturalizedCitizenYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers15.answerValue2</v></findby>)