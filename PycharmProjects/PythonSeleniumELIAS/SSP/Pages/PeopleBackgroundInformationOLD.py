from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			RadioAlienNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Alien Number</v>)
			RadioActiveDutyNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			RadioActiveDutyYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			ComboCountryofCitizenship = (<instance>1|<tagname>SELECT</tagname>|<n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v><n>name</n><v criteria="startswith">answerSets[0].answers[</v></findby>)
			TextCardNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextNaturalizedCertificationNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextAlienNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">REPLACEID</v></findby>)
			TextCertificationofCitizenshipNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextDocument/PassportExpirationDate = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v><n>NAME</n><v criteria="startswith">answerSets[0].answers[</v></findby>)
			TextSEVISID = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">REPLACEID</v></findby>)
			TextPassportNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v><n>name</n><v criteria="startswith">answerSets[0].answers[</v></findby>)
			TextVisaNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextI94Number = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">REPLACEID</v><n>name</n><v criteria="startswith">answerSets[0].answers[</v></findby>)
			ComboImmigrationStatus = (<instance>1|<tagname>SELECT</tagname>|)
			CheckRaceAmericanNativeE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">textMessage</v><n>TYPE</n><v criteria="isequalto">checkbox</v>)
			CheckRaceAsianE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">textMessage</v><n>TYPE</n><v criteria="isequalto">checkbox</v>)
			CheckRaceBlackE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">textMessage</v><n>TYPE</n><v criteria="isequalto">checkbox</v>)
			CheckRaceHispanicE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">textMessage</v><n>TYPE</n><v criteria="isequalto">checkbox</v>)
			CheckRaceNativeHawaiianE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">textMessage</v><n>TYPE</n><v criteria="isequalto">checkbox</v>)
			CheckRaceUnknownE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">textMessage</v><n>TYPE</n><v criteria="isequalto">checkbox</v>)
			CheckRaceWhiteE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">textMessage</v><n>TYPE</n><v criteria="isequalto">checkbox</v>)
			ComboEthnicGroupAsianE12 = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers137.answerValue</v>)
			ComboEthnicGroupHawaiianE12 = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers135.answerValue</v>)
			ComboEthnicGroupHispanicE12 = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers136.answerValue</v>)
			ComboImmigrationStatusE12 = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers19.answerValue</v>)
			ComboPreferredLanguageE12 = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers5.answerValue</v>)
			RadioChildSupportNoE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers10.answerValue2</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioChildSupportYesE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers10.answerValue1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioEligibleImmigrationNoE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers18.answerValue2</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioEligibleImmigrationYesE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers18.answerValue1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioFosterCareNoE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers7.answerValue2</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioFosterCareYesE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers7.answerValue1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioHaveInsuranceNoE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers12.answerValue2</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioHaveInsuranceYesE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers12.answerValue1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioLanguageAssistanceNoE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers6.answerValue2</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioLanguageAssistanceYesE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers6.answerValue1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioLivedInUSSince1996NoE12 = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioLivedInUSSince1996YesE12 = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			RadioNaturalizedCitizenNoE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers16.answerValue2</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioNaturalizedCitizenYesE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers16.answerValue1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioParentLivingOutsideNoE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers11.answerValue2</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioParentLivingOutsideYesE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers11.answerValue1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioStateResidentNoE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers1.answerValue2</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioStateResidentYesE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers1.answerValue1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			ComboDocumentTypeE12 = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers22.answerValue</v>)
			RadioSameNameOnDocumentNoE12 = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioSameNameOnDocumentYesE12 = (<instance>1|<tagname>INPUT</tagname>|<n>ID</n><v criteria="isequalto">answerSets0.answers112.answerValue1</v><n>TYPE</n><v criteria="isequalto">radio</v>)
			RadioLivedInUSSince1996NoOLD = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioLivedInUSSince1996YesOLD = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			RadioSameNameOnDocumentNoOLD = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioSameNameOnDocumentYesOLD = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			CheckRaceAmericanNative = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>value</n><v criteria="isequalto">American Indian or Alaskan Native</v></findby>)
			CheckRaceAsian = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>value</n><v criteria="isequalto">Asian</v></findby>)
			CheckRaceBlack = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>value</n><v criteria="isequalto">Black or African American</v></findby>)
			CheckRaceHispanic = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>value</n><v criteria="isequalto">Hispanic or Latino</v></findby>)
			CheckRaceNativeHawaiian = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>value</n><v criteria="isequalto">Native Hawaiian or Other Pacific Islander</v></findby>)
			CheckRaceUnknown = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>value</n><v criteria="isequalto">Unknown</v></findby>)
			CheckRaceWhite = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">checkbox</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>value</n><v criteria="isequalto">White</v></findby>)
			ComboCitizenshipStatus = (<instance>1|<tagname>SELECT</tagname>|)
			ComboDocumentType = (<instance>1|<tagname>SELECT</tagname>|<n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			ComboEthnicGroupAsian = (<instance>1|<tagname>SELECT</tagname>|<n>INNERTEXT</n><v criteria="contains">Asian Indian</v>)
			ComboEthnicGroupHawaiian = (<instance>1|<tagname>SELECT</tagname>|<n>INNERTEXT</n><v criteria="contains">Guamanian</v>)
			ComboEthnicGroupHispanic = (<instance>1|<tagname>SELECT</tagname>|<n>INNERTEXT</n><v criteria="contains">Mexican</v>)
			ComboPreferredLanguage = (<instance>1|<tagname>SELECT</tagname>|<n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>className</n><v criteria="isequalto">hasScript</v><n>id</n><v criteria="contains">answerSets</v><n>name</n><v criteria="contains">answerSets</v><n>type</n><v criteria="isequalto">select-one</v><n>id</n><v criteria="isequalto">answerSets0.answers5.answerValue</v></findby>)
			ComboSectionCode = (<instance>1|<tagname>SELECT</tagname>|<n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>INNERTEXT</n><v criteria="contains">REPLACEME</v></findby>)
			RadioBornInUsNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioBornInUsYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			RadioChildSupportNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>className</n><v criteria="isequalto">hasScript</v><n>id</n><v criteria="isequalto">answerSets0.answers10.answerValue2</v><n>name</n><v criteria="contains">answerSets</v></findby>)
			RadioChildSupportYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>className</n><v criteria="isequalto">hasScript</v><n>id</n><v criteria="isequalto">answerSets0.answers10.answerValue1</v><n>name</n><v criteria="contains">answerSets</v></findby>)
			RadioEligibleImmigrationNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers19.answerValue2</v></findby>)
			RadioEligibleImmigrationYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers19.answerValue1</v></findby>)
			RadioFosterCareNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>className</n><v criteria="isequalto">hasScript</v><n>id</n><v criteria="isequalto">answerSets0.answers7.answerValue2</v><n>name</n><v criteria="contains">answerSets</v></findby>)
			RadioFosterCareYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>className</n><v criteria="isequalto">hasScript</v><n>id</n><v criteria="isequalto">answerSets0.answers7.answerValue1</v><n>name</n><v criteria="contains">answerSets</v></findby>)
			RadioHaveInsuranceNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>className</n><v criteria="isequalto">hasScript</v><n>id</n><v criteria="isequalto">answerSets0.answers12.answerValue2</v><n>name</n><v criteria="contains">answerSets</v></findby>)
			RadioHaveInsuranceYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>className</n><v criteria="isequalto">hasScript</v><n>id</n><v criteria="isequalto">answerSets0.answers12.answerValue1</v><n>name</n><v criteria="contains">answerSets</v></findby>)
			RadioLanguageAssistanceNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>className</n><v criteria="isequalto">hasScript</v><n>id</n><v criteria="isnotequalto">answerSets0.answers6.answerValue2</v><n>name</n><v criteria="contains">answerSets</v></findby>)
			RadioLanguageAssistanceYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>className</n><v criteria="isequalto">hasScript</v><n>id</n><v criteria="contains">answerSets</v><n>name</n><v criteria="contains">answerSets</v><n>id</n><v criteria="isequalto">answerSets0.answers6.answerValue1</v></findby>)
			RadioLivedInUSSince1996No = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			RadioLivedInUSSince1996Yes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			RadioNaturalizedCitizenNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioNaturalizedCitizenYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			RadioParentLivingOutsideNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioParentLivingOutsideYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			RadioSameNameOnDocumentNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			RadioSameNameOnDocumentYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			RadioStateResidentNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>ID</n><v criteria="isequalto">answerSets0.answers1.answerValue2</v></findby>)
			RadioStateResidentYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>ID</n><v criteria="isequalto">answerSets0.answers1.answerValue1</v></findby>)
			RadioUSCitizenNationalNo = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">No</v>)
			RadioUSCitizenNationalYes = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">radio</v><n>VALUE</n><v criteria="isequalto">Yes</v>)
			TextDateOfEntry = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers191.answerValue</v></findby>)
			TextFirstName = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextIDNumber = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextInsuranceEndDate = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers13.answerValue</v></findby>)
			TextInsuranceEndReason = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="isequalto">answerSets0.answers14.answerValue</v></findby>)
			TextLastName = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextMiddleName = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v><n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>id</n><v criteria="startswith">answerSets0.answers</v></findby>)
			TextOtherEthnicGroup = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v>)
			TextResidentSince = (<instance>1|<tagname>INPUT</tagname>|<n>TYPE</n><v criteria="isequalto">text</v>)
			LabelQuestionTextForEditbox = (<instance>1|<tagname>LABEL</tagname>|<n>IsHidden</n><v criteria="isequalto">False</v><n>IsVisible</n><v criteria="isequalto">True</v><n>innerTEXT</n><v criteria="doesnotcontain">DoesNotContainText</v><n>innerTEXT</n><v criteria="contains">StartAtText</v><n>for</n><v criteria="doesnotcontain">answerValue1</v><n>for</n><v criteria="doesnotcontain">answerValue2</v></findby>)