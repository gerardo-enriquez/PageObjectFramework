from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions



			LinkInbox = (<instance>1|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="isequalto"> Inbox</v>)
			LinkSentItems = (<instance>1|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="isequalto"> Sent Items</v>)
			LinkArchiveFolder = (<instance>1|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="isequalto"> Archive Folder</v>)
			LinkCompose = (<instance>1|<tagname>A</tagname>|<n>ID</n><v criteria="isequalto">compose</v>)
			LinkArchiveMessage = (<instance>1|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="isequalto">Archive</v>)
			LinkCloseMailbox = (<instance>1|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="isequalto">Close</v>)
			TableYourMailbox = (<instance>1|<tagname>TABLE</tagname>|<n>INNERTEXT</n><v criteria="startswith">*messageattachmentFromSubjectReceived</v><n>TAGNAME</n><v criteria="isequalto">TABLE</v></findby>)
			TableYourMailboxSentItems = (<instance>1|<tagname>TABLE</tagname>|<n>INNERTEXT</n><v criteria="startswith">*ToSubjectSent</v><n>TAGNAME</n><v criteria="isequalto">TABLE</v></findby>)
			TableYourMailboxArchivedFolder = (<instance>1|<tagname>TABLE</tagname>|<n>INNERTEXT</n><v criteria="startswith">*FromSubjectReceived</v><n>TAGNAME</n><v criteria="isequalto">TABLE</v></findby>)
			ComboMessageComposeTo = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">toCompose</v>)
			ComboMessageComposeSubject = (<instance>1|<tagname>SELECT</tagname>|<n>ID</n><v criteria="isequalto">subjectCompose</v>)
			TextComboMessageContent = (<instance>1|<tagname>TEXTAREA</tagname>|<n>ID</n><v criteria="isequalto">content</v><n>TYPE</n><v criteria="isequalto">textarea</v><n>CLASSNAME</n><v criteria="isequalto">messageTextArea</v>)
			LinkCancelMessage = (<instance>2|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="isequalto">Cancel</v>)
			LinkSendMessage = (<instance>1|<tagname>A</tagname>|<n>INNERTEXT</n><v criteria="isequalto">Send</v>)
