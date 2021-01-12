# Non-Functional Property Improving Commits

This is the repository containing a set of commits which improve the non-functional properties (NFPS) of android applications. These commits were elicited with keyword selection and manual analysis. Other commits were obtained through the use of an automatic classifier. The repositories Manually mined were:


|Name  | Repository |
|--|--|
|Aeons End|[https://github.com/JanSvoboda/aeonsend-randomizer](https://github.com/JanSvoboda/aeonsend-randomizer)|
|AFH Downloader|[https://github.com/daktak/afh_downloader](https://github.com/daktak/afh_downloader)|
|Android CUPS Print|[https://github.com/BenoitDuffez/AndroidCupsPrint/](https://github.com/BenoitDuffez/AndroidCupsPrint/)|
|ANNO 1404|[https://github.com/tran-khoa/ANNO1404-Warenrechner-App](https://github.com/tran-khoa/ANNO1404-Warenrechner-App)|
|Apple Flinger|[https://gitlab.com/ar-/apple-flinger](https://gitlab.com/ar-/apple-flinger)|
|Calculator|[https://github.com/Xlythe/Calculator](https://github.com/Xlythe/Calculator)|
|Call Recorder|[https://gitlab.com/axet/android-call-recorder](https://gitlab.com/axet/android-call-recorder)|
|DNS66|[https://github.com/julian-klode/dns66](https://github.com/julian-klode/dns66)|
|Editor|[https://github.com/billthefarmer/editor](https://github.com/billthefarmer/editor)|
|F-Droid|[https://gitlab.com/fdroid/fdroidclient](https://gitlab.com/fdroid/fdroidclient)|
|Firefox Klar|[https://github.com/mozilla-mobile/focus-android](https://github.com/mozilla-mobile/focus-android)|
|FOSS Browser|[https://github.com/scoute-dich/browser](https://github.com/scoute-dich/browser)|
|Frozen Bubble|[https://github.com/videogameboy76/frozenbubbleandroid](https://github.com/videogameboy76/frozenbubbleandroid)|
|G-Droid|[https://gitlab.com/gdroid/gdroidclient/](https://gitlab.com/gdroid/gdroidclient/)|
|Gadgetbridge|[https://codeberg.org/Freeyourgadget/Gadgetbridge](https://codeberg.org/Freeyourgadget/Gadgetbridge)|
|Gloomy Dungeons 2|[https://github.com/restorer/gloomy-dungeons-2](https://github.com/restorer/gloomy-dungeons-2)|
|MaterialOS|[https://github.com/materialos/android-icon-pack](https://github.com/materialos/android-icon-pack)|
|Mi Mangu Nu|[https://github.com/raulhaag/MiMangaNu](https://github.com/raulhaag/MiMangaNu)|
|Mighty Knight|[https://github.com/alketii/mighty-knight](https://github.com/alketii/mighty-knight)|
|NewPipe|[https://github.com/TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe)|


The automatically mined repositories in which at least one commit was found to improve a non-functional property can be found below:

|Name  | Repository |
|--|--|
|Koreader|https://github.com/koreader/koreader
|lnwallet|https://github.com/btcontract/lnwallet
|Calendar Notification|https://github.com/quarck/CalendarNotification
|rbb|https://github.com/btmura/rbb
|openmw|https://github.com/xyzz/openmw-android
|Port Authority|https://github.com/aaronjwood/PortAuthority
|Pixiv for Muzei|https://github.com/yellowbluesky/PixivforMuzei3
|openfoodfacts|https://github.com/openfoodfacts/openfoodfacts-androidapp
|AntennaPod|https://github.com/AntennaPod/AntennaPod
|Tower Collector|https://github.com/anthonycr/TowerCollector
|glt-companion|https://github.com/linuxtage/glt-companion
|avare|https://github.com/apps4av/avare
|TVH Guide|https://github.com/john-tornblom/TVHGuide
|Easy Token|https://github.com/cernekee/EasyToken
|ProExpense|https://github.com/arduia/ProExpense
|SMS Sync|https://github.com/ushahidi/SMSSync
|Kernel Adiutor|https://github.com/NHellFire/KernelAdiutor
|OpenBike Sharing|https://github.com/bparmentier/OpenBikeSharing
|GigaGet|https://github.com/PaperAirplane-Dev-Team/GigaGet
|LightningBrowser|https://github.com/anthonycr/Lightning-Browser




The repository is structured as follows:

**Commits**
>**Manual/Automaic/Both** : *All commits grouped by NFP and repository. Either only manually mined, automatically mined, or both* 
>>**ByRepo**: *Commits split by repository in whoich they were found*
>>>**Repository Name**: *Repository containing commits*
>>>>**executionTime.txt**: *Execution Time improving commits*

>>>>**memory.txt**: *Memory improving commits*

>>>>**bandwidth.txt**: *Bandwidth improving commit*

>>>>**frameRate.txt**: *Frame rate improving commits*

>>**Categories**: *Commits group by category of improvement*
>>>**executionTime**

>>>**memory**

>>>**bandwidth**

>>>**frameRate**

**Scripts**: *A repository cotaining python scripts used to mine commits.*
>**classifier** : *The automatic commit classifier*

**AllNFPCommits.pdf**: *Fully expanded commit table, including commits filtered with the automatic classifier*

**CMRepoProps.pdf**: *Properties of the repositories mined by the classifier, in which commits were found*

***NOTES***
*Empty files are present where no commits of that group were found.*