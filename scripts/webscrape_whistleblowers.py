'''import requests
from bs4 import BeautifulSoup as bs4
from urllib.request import urlopen
#table class = 'wikitable sortable jquery-tablesorter>
URL = 'https://en.wikipedia.org/wiki/List_of_whistleblowers'
#page = requests.get(URL)
page = urlopen(URL)
html = page.read().decode('utf-8')
soup = bs4(html, "html.parser")
soup.find_all(True,{'class':"wikitable sortable query-tablesorter"})

rows =  []

for r in rows:
   year =  bs4.find().get_text()
   name = bs4.find().get_text()
   gender = bs4.find().get_text()
   action = bs4.find().get_text()


data = {
   
    "year": year,
    "name":name, 
    "gender":gender,
    "action":action
}



# Sample HTML
html = """
<tr>
<th scope="col" style="width:3em" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Year
</th>
<th scope="col" class="unsortable" style="width:5em">Image
</th>
<th scope="col" style="width:7em" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Name
</th>
<th scope="col" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Gender
</th>
<th scope="col" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Organization
</th>
<th scope="col" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Action
</th></tr>
"""
'''
#html_body = '''<tbody>
'''<tr>
<td>2000s
</td>
<td><span typeof="mw:File"><a href="/wiki/File:Karen_Kwiatkowski_on_the_farm.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Karen_Kwiatkowski_on_the_farm.jpg/75px-Karen_Kwiatkowski_on_the_farm.jpg" decoding="async" width="75" height="75" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Karen_Kwiatkowski_on_the_farm.jpg/113px-Karen_Kwiatkowski_on_the_farm.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Karen_Kwiatkowski_on_the_farm.jpg/150px-Karen_Kwiatkowski_on_the_farm.jpg 2x" data-file-width="176" data-file-height="176"></a></span>
</td>
<td><a href="/wiki/Karen_Kwiatkowski" title="Karen Kwiatkowski">Karen Kwiatkowski</a>
</td>
<td>Female
</td>
<td><a href="/wiki/United_States_Air_Force" title="United States Air Force">United States Air Force</a>
</td>
<td>Retired lieutenant colonel in the U.S. Air Force who worked as a desk officer in <a href="/wiki/The_Pentagon" title="The Pentagon">The Pentagon</a> and in a number of roles in the <a href="/wiki/National_Security_Agency" title="National Security Agency">National Security Agency</a>. She has written a number of essays on corrupting political influences of <a href="/wiki/Military_intelligence" title="Military intelligence">military intelligence</a> leading up to the <a href="/wiki/Invasion_of_Iraq" class="mw-redirect" title="Invasion of Iraq">invasion of Iraq</a> in 2003, and has said that she was the anonymous source for <a href="/wiki/Seymour_Hersh" title="Seymour Hersh">Seymour Hersh</a> and <a href="/wiki/Warren_Strobel" class="mw-redirect" title="Warren Strobel">Warren Strobel</a> on their exposés of pre-war intelligence.<sup id="cite_ref-133" class="reference"><a href="#cite_note-133"><span class="cite-bracket">[</span>133<span class="cite-bracket">]</span></a></sup>
</td></tr>
<tr>
<td>2000
</td>
<td><span typeof="mw:File"><a href="/wiki/File:Marsha_Coleman-Adebayo.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Marsha_Coleman-Adebayo.jpg/75px-Marsha_Coleman-Adebayo.jpg" decoding="async" width="75" height="105" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Marsha_Coleman-Adebayo.jpg/113px-Marsha_Coleman-Adebayo.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Marsha_Coleman-Adebayo.jpg/150px-Marsha_Coleman-Adebayo.jpg 2x" data-file-width="1500" data-file-height="2100"></a></span>
</td>
<td><a href="/wiki/Marsha_Coleman-Adebayo" title="Marsha Coleman-Adebayo">Marsha Coleman-Adebayo</a>
</td>
<td>Female
</td>
<td><a href="/wiki/United_States_Environmental_Protection_Agency" title="United States Environmental Protection Agency">United States Environmental Protection Agency</a>
</td>
<td><a href="/wiki/Marsha_Coleman-Adebayo" title="Marsha Coleman-Adebayo">Marsha Coleman-Adebayo</a> was a Senior Policy Analyst in the Office of the Administrator at the U.S. Environmental Protection Agency (EPA). She blew the whistle on the EPA for racial and gender discrimination in violation of <a href="/wiki/Civil_Rights_Act_of_1964" title="Civil Rights Act of 1964">Civil Rights Act of 1964</a> which began after she was removed from her position in South Africa where her "job was to essentially help the South African government to work on issues that impact public health".<sup id="cite_ref-Phipps_134-0" class="reference"><a href="#cite_note-Phipps-134"><span class="cite-bracket">[</span>134<span class="cite-bracket">]</span></a></sup> In South Africa she brought to the attention of the EPA the dangerous conditions an American company was exposing African workers who were mining to vanadium, a dangerous substance. Her case eventually led to the passing of the <a href="/wiki/No-FEAR_Act" title="No-FEAR Act">No-FEAR Act</a> in 2002 that makes federal agencies more accountable for employee complaints.<sup id="cite_ref-Phipps_134-1" class="reference"><a href="#cite_note-Phipps-134"><span class="cite-bracket">[</span>134<span class="cite-bracket">]</span></a></sup>
</td></tr>
<tr>
<td>2002
</td>
<td>
</td>
<td><a href="/wiki/Cynthia_Cooper_(accountant)" title="Cynthia Cooper (accountant)">Cynthia Cooper</a>
</td>
<td>Female
</td>
<td><a href="/wiki/MCI_Inc." title="MCI Inc.">Worldcom</a>
</td>
<td>Exposed <a href="/wiki/WorldCom_scandal" title="WorldCom scandal">corporate financial scandal</a>. Jointly named <i>Time'</i>s <a href="/wiki/Time_Magazine_Person_of_the_Year" class="mw-redirect" title="Time Magazine Person of the Year">People of the Year</a> in 2002.<sup id="cite_ref-:0_135-0" class="reference"><a href="#cite_note-:0-135"><span class="cite-bracket">[</span>135<span class="cite-bracket">]</span></a></sup>
</td></tr>
<tr>
<td>2002
</td>
<td><span typeof="mw:File"><a href="/wiki/File:34._ISC-Symposium-Sherron_S._Watkins-HSGN_028-01742.JPG" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/34._ISC-Symposium-Sherron_S._Watkins-HSGN_028-01742.JPG/75px-34._ISC-Symposium-Sherron_S._Watkins-HSGN_028-01742.JPG" decoding="async" width="75" height="49" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/34._ISC-Symposium-Sherron_S._Watkins-HSGN_028-01742.JPG/113px-34._ISC-Symposium-Sherron_S._Watkins-HSGN_028-01742.JPG 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0d/34._ISC-Symposium-Sherron_S._Watkins-HSGN_028-01742.JPG/150px-34._ISC-Symposium-Sherron_S._Watkins-HSGN_028-01742.JPG 2x" data-file-width="3008" data-file-height="1960"></a></span>
</td>
<td><a href="/wiki/Sherron_Watkins" title="Sherron Watkins">Sherron Watkins</a>
</td>
<td>Female
</td>
<td><a href="/wiki/Enron" title="Enron">Enron</a>
</td>
<td>Exposed corporate financial <a href="/wiki/Enron_scandal" title="Enron scandal">scandal</a> as <a href="/wiki/Enron" title="Enron">Enron</a> vice president in 2001. Watkins was named Time's People of the Year in 2002.<sup id="cite_ref-:0_135-1" class="reference"><a href="#cite_note-:0-135"><span class="cite-bracket">[</span>135<span class="cite-bracket">]</span></a></sup><sup id="cite_ref-136" class="reference"><a href="#cite_note-136"><span class="cite-bracket">[</span>136<span class="cite-bracket">]</span></a></sup>
</td></tr>
<tr>
<td>2002
</td>
<td><span typeof="mw:File"><a href="/wiki/File:Coleen_Rowley_17_Sep_2006.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Coleen_Rowley_17_Sep_2006.jpg/75px-Coleen_Rowley_17_Sep_2006.jpg" decoding="async" width="75" height="54" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Coleen_Rowley_17_Sep_2006.jpg/113px-Coleen_Rowley_17_Sep_2006.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Coleen_Rowley_17_Sep_2006.jpg/150px-Coleen_Rowley_17_Sep_2006.jpg 2x" data-file-width="659" data-file-height="477"></a></span>
</td>
<td><a href="/wiki/Coleen_Rowley" title="Coleen Rowley">Coleen Rowley</a>
</td>
<td>Female
</td>
<td><a href="/wiki/Federal_Bureau_of_Investigation" title="Federal Bureau of Investigation">Federal Bureau of Investigation</a>
</td>
<td>Outlined the FBI's slow action before the <a href="/wiki/September_11,_2001_attacks" class="mw-redirect" title="September 11, 2001 attacks">September 11, 2001 attacks</a>. Jointly named <i>Time'</i>s <a href="/wiki/Time_Magazine_Person_of_the_Year" class="mw-redirect" title="Time Magazine Person of the Year">People of the Year</a> in 2002.
</td></tr>
<tr>
<td>2002
</td>
<td><span typeof="mw:File"><a href="/wiki/File:William_Binney-IMG_9040.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b9/William_Binney-IMG_9040.jpg/75px-William_Binney-IMG_9040.jpg" decoding="async" width="75" height="113" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b9/William_Binney-IMG_9040.jpg/113px-William_Binney-IMG_9040.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b9/William_Binney-IMG_9040.jpg/150px-William_Binney-IMG_9040.jpg 2x" data-file-width="2923" data-file-height="4385"></a></span>
</td>
<td><a href="/wiki/William_Binney_(U.S._intelligence_official)" class="mw-redirect" title="William Binney (U.S. intelligence official)">William Binney</a><br><a href="/w/index.php?title=J._Kirke_Wiebe&amp;action=edit&amp;redlink=1" class="new" title="J. Kirke Wiebe (page does not exist)">J. Kirke Wiebe</a><br><a href="/w/index.php?title=Edward_Loomis&amp;action=edit&amp;redlink=1" class="new" title="Edward Loomis (page does not exist)">Edward Loomis</a>
</td>
<td>Male
</td>
<td><a href="/wiki/National_Security_Agency" title="National Security Agency">National Security Agency</a>
</td>
<td>NSA officials initially joined <a href="/wiki/United_States_House_Permanent_Select_Committee_on_Intelligence" title="United States House Permanent Select Committee on Intelligence">House Permanent Select Committee on Intelligence</a> staffer <a href="/wiki/Diane_Roark" title="Diane Roark">Diane Roark</a> in asking U.S. Department of Defense inspector general to investigate wasteful spending on the <a href="/wiki/Trailblazer_Project" title="Trailblazer Project">Trailblazer Project</a> and the NSA officials eventually went public when they were ignored and retaliated upon. They claim that <a href="/wiki/Thinthread" class="mw-redirect" title="Thinthread">Thinthread</a> was more focused thus more effective and lower cost than Trailblazer and subsequent programs, which automatically collected trillions of domestic communications of Americans in deliberate violation of the U.S. Constitution.
</td></tr>
<tr>
<td>2002
</td>
<td><span typeof="mw:File"><a href="/wiki/File:Sibel_edmonds_on_RT.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Sibel_edmonds_on_RT.png/75px-Sibel_edmonds_on_RT.png" decoding="async" width="75" height="53" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Sibel_edmonds_on_RT.png/113px-Sibel_edmonds_on_RT.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Sibel_edmonds_on_RT.png/150px-Sibel_edmonds_on_RT.png 2x" data-file-width="748" data-file-height="524"></a></span>
</td>
<td><a href="/wiki/Sibel_Edmonds" title="Sibel Edmonds">Sibel Edmonds</a>
</td>
<td>Female
</td>
<td><a href="/wiki/Federal_Bureau_of_Investigation" title="Federal Bureau of Investigation">Federal Bureau of Investigation</a>
</td>
<td>Former FBI translator naturalized <a href="/wiki/Turkish_American" class="mw-redirect" title="Turkish American">American citizen of Turkish descent</a> who was fired in 2002 by the FBI for attempting to report cover-ups of security issues, potential espionage, and incompetence.<sup id="cite_ref-137" class="reference"><a href="#cite_note-137"><span class="cite-bracket">[</span>137<span class="cite-bracket">]</span></a></sup><sup id="cite_ref-138" class="reference"><a href="#cite_note-138"><span class="cite-bracket">[</span>138<span class="cite-bracket">]</span></a></sup> She has been gagged by the <a href="/wiki/State_Secrets_Privilege" class="mw-redirect" title="State Secrets Privilege">State Secrets Privilege</a> in her efforts to go to court on these issues, including a rejection in 2005 by the <a href="/wiki/Supreme_Court_of_the_United_States" title="Supreme Court of the United States">Supreme Court of the United States</a> to hear her case without comment.<sup id="cite_ref-139" class="reference"><a href="#cite_note-139"><span class="cite-bracket">[</span>139<span class="cite-bracket">]</span></a></sup><sup id="cite_ref-140" class="reference"><a href="#cite_note-140"><span class="cite-bracket">[</span>140<span class="cite-bracket">]</span></a></sup> She is the founder of the <a href="/wiki/National_Security_Whistleblowers_Coalition" title="National Security Whistleblowers Coalition">National Security Whistleblowers Coalition</a> (NSWBC) that is looking to lobby congress and help other whistleblowers with legal and other forms of assistance.<sup id="cite_ref-141" class="reference"><a href="#cite_note-141"><span class="cite-bracket">[</span>141<span class="cite-bracket">]</span></a></sup>
</td></tr>
<tr>
<td>2002 &amp; 2004
</td>
<td><span typeof="mw:File"><a href="/wiki/File:Sterling_Photo.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Sterling_Photo.jpg/75px-Sterling_Photo.jpg" decoding="async" width="75" height="44" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Sterling_Photo.jpg/113px-Sterling_Photo.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Sterling_Photo.jpg/150px-Sterling_Photo.jpg 2x" data-file-width="3944" data-file-height="2317"></a></span>
</td>
<td><a href="/wiki/Jeffrey_Alexander_Sterling" title="Jeffrey Alexander Sterling">Jeffrey Alexander Sterling</a>
</td>
<td>Male
</td>
<td><a href="/wiki/Central_Intelligence_Agency" title="Central Intelligence Agency">Central Intelligence Agency</a>
</td>
<td>Sentenced to 3.5 years in prison for revealing details about <a href="/wiki/Operation_Merlin" title="Operation Merlin">Operation Merlin</a> (covert operation to supply Iran with flawed nuclear warhead blueprints) to journalist <a href="/wiki/James_Risen" title="James Risen">James Risen</a>.
</td></tr>
<tr>
<td>2003
</td>
<td>
</td>
<td><a href="/wiki/Katharine_Gun" title="Katharine Gun">Katharine Gun</a>
</td>
<td>Female
</td>
<td><a href="/wiki/Government_Communications_Headquarters" class="mw-redirect" title="Government Communications Headquarters">United Kingdom GCHQ</a>
</td>
<td>Leaked top-secret information to the press concerning alleged illegal activities by the United States and the United Kingdom in their push for the <a href="/wiki/2003_invasion_of_Iraq" title="2003 invasion of Iraq">2003 invasion of Iraq</a>.
</td></tr>
<tr>
<td>2003
</td>
<td>
</td>
<td><a href="/wiki/Joseph_C._Wilson" title="Joseph C. Wilson">Joseph Wilson</a>
</td>
<td>Male
</td>
<td><a href="/wiki/United_States_Government" class="mw-redirect" title="United States Government">United States Government</a>
</td>
<td>Former U.S. ambassador, whose editorial in <i><a href="/wiki/The_New_York_Times" title="The New York Times">The New York Times</a></i>, "What I Didn't Find in Africa",<sup id="cite_ref-142" class="reference"><a href="#cite_note-142"><span class="cite-bracket">[</span>142<span class="cite-bracket">]</span></a></sup> showed reasons for the <a href="/wiki/2003_invasion_of_Iraq" title="2003 invasion of Iraq">2003 invasion of Iraq</a>.
</td></tr>
<tr>
<td>2004
</td>
<td>
</td>
<td>Neil Patrick Carrick
</td>
<td>Male
</td>
<td><a href="/wiki/Greater_Grace_World_Outreach" title="Greater Grace World Outreach">Greater Grace World Outreach</a>
</td>
<td>A former member and staff member of Greater Grace World Outreach in Baltimore, Maryland U.S.A. who uncovered financial and sexual abuse by church leaders. Eventually, The Baltimore Sun would publish a front-page story uncovering a $500,000 payoff regarding a cover-up of an affair of a staff Pastor. Multiple articles across the United States and Internationally would follow. Following the split of the international organization hundreds of congregations, schools would change their affiliation with the organization. In the following years, several individuals would be convicted of sexual abuse related crimes including staff members from the Baltimore Church.
</td></tr>
<tr>
<td>2004
</td>
<td>
</td>
<td><a href="/wiki/Mukesh_Kapila" title="Mukesh Kapila">Mukesh Kapila</a>
</td>
<td>Male
</td>
<td><a href="/wiki/Darfur_genocide" title="Darfur genocide">Darfur genocide</a>
</td>
<td>In 2003–2004 Kapila was the <a href="/wiki/United_Nations" title="United Nations">United Nations</a> Resident and Humanitarian Coordinator, and the <a href="/wiki/United_Nations_Development_Programme" title="United Nations Development Programme">UN Development Program</a> Resident Representative for the <a href="/wiki/Sudan" title="Sudan">Sudan</a>. His reports about the <a href="/wiki/War_in_Darfur" title="War in Darfur">Darfur conflict</a> were at the time dismissed by the Government of Sudan as "a heap of lies", though they succeeded in bringing Darfur to the attention of the world's media for the first time. Kapila lost his job after becoming a <a href="/wiki/Whistleblower" class="mw-redirect" title="Whistleblower">whistleblower</a> regarding UN inaction in Darfur, and had to leave Sudan. He also received many death threats which continued for many years.<sup id="cite_ref-hmd_143-0" class="reference"><a href="#cite_note-hmd-143"><span class="cite-bracket">[</span>143<span class="cite-bracket">]</span></a></sup>
</td></tr>
<tr>
<td>2004
</td>
<td><span typeof="mw:File"><a href="/wiki/File:Sergeant_Provance.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sergeant_Provance.jpg/75px-Sergeant_Provance.jpg" decoding="async" width="75" height="81" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sergeant_Provance.jpg/113px-Sergeant_Provance.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sergeant_Provance.jpg/150px-Sergeant_Provance.jpg 2x" data-file-width="600" data-file-height="648"></a></span>
</td>
<td><a href="/wiki/Samuel_Provance" title="Samuel Provance">Samuel Provance</a>
<p><a href="/wiki/Joe_Darby" title="Joe Darby">Joe Darby</a>
</p>
</td>
<td>Male
</td>
<td><a href="/wiki/United_States_Army" title="United States Army">United States Army</a>
</td>
<td>Publicly revealed the role of <a href="/wiki/Interrogation" title="Interrogation">interrogators</a> in the abuses, as well the general effort to cover-up the <a href="/wiki/Abu_Ghraib_torture_and_prisoner_abuse" title="Abu Ghraib torture and prisoner abuse">Abu Ghraib prisoner abuse</a> itself.<sup id="cite_ref-144" class="reference"><a href="#cite_note-144"><span class="cite-bracket">[</span>144<span class="cite-bracket">]</span></a></sup> Darby received a <a href="/wiki/John_F._Kennedy_Profile_in_Courage_Award" class="mw-redirect" title="John F. Kennedy Profile in Courage Award">John F. Kennedy Profile in Courage Award</a>.<sup id="cite_ref-When_Joseph_Comes_Marching_Home_145-0" class="reference"><a href="#cite_note-When_Joseph_Comes_Marching_Home-145"><span class="cite-bracket">[</span>145<span class="cite-bracket">]</span></a></sup>
</td></tr>
<tr>
<td>2005
</td>
<td><span typeof="mw:File"><a href="/wiki/File:Russ_Tice_2009.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Russ_Tice_2009.jpg/75px-Russ_Tice_2009.jpg" decoding="async" width="75" height="97" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Russ_Tice_2009.jpg/113px-Russ_Tice_2009.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Russ_Tice_2009.jpg/150px-Russ_Tice_2009.jpg 2x" data-file-width="1140" data-file-height="1472"></a></span>
</td>
<td><a href="/wiki/Russ_Tice" title="Russ Tice">Russ Tice</a>
</td>
<td>Male
</td>
<td><a href="/wiki/United_States_Government" class="mw-redirect" title="United States Government">United States Government</a>
</td>
<td>Former intelligence analyst for the <a href="/wiki/National_Security_Agency" title="National Security Agency">National Security Agency</a> (NSA), the <a href="/wiki/U.S._Air_Force" class="mw-redirect" title="U.S. Air Force">U.S. Air Force</a>, the <a href="/wiki/Office_of_Naval_Intelligence" title="Office of Naval Intelligence">Office of Naval Intelligence</a>, and the <a href="/wiki/Defense_Intelligence_Agency" title="Defense Intelligence Agency">Defense Intelligence Agency</a>. Tice first approached Congress and eventually the media about the <a href="/wiki/NSA_warrantless_surveillance_(2001%E2%80%9307)" class="mw-redirect" title="NSA warrantless surveillance (2001–07)">warrantless surveillance</a> of the U.S. population by the NSA. Tice was a major source for the 2005 <i>New York Times</i> exposé and spoke out widely following subsequent disclosures by other NSA whistleblowers. He was the first to speak publicly and openly with allegations during the era beginning with the <a href="/wiki/Presidency_of_George_W._Bush" title="Presidency of George W. Bush">George W. Bush administration</a> (which continues into the <a href="/wiki/Presidency_of_Barack_Obama" title="Presidency of Barack Obama">Obama administration</a>). He had earlier been known for reporting suspicions that a DIA colleague of his might be a Chinese spy.<sup id="cite_ref-146" class="reference"><a href="#cite_note-146"><span class="cite-bracket">[</span>146<span class="cite-bracket">]</span></a></sup>
</td></tr>
<tr>
<td>2005/
<p>2011
</p>
</td>
<td>
</td>
<td><a href="/wiki/Thomas_Andrews_Drake" class="mw-redirect" title="Thomas Andrews Drake">Thomas Andrews Drake</a>
</td>
<td>Male
</td>
<td><a href="/wiki/National_Security_Agency" title="National Security Agency">National Security Agency</a>
</td>
<td>Thomas Drake worked at the NSA in various analyst and management positions.  He blew the whistle on the NSA's <a href="/wiki/Trailblazer_Project" title="Trailblazer Project">Trailblazer Project</a> that he felt was a violation of the <a href="/wiki/Fourth_Amendment_to_the_United_States_Constitution" title="Fourth Amendment to the United States Constitution">Fourth Amendment</a> and other laws and regulations.  He contacted <i><a href="/wiki/Baltimore_Sun" class="mw-redirect" title="Baltimore Sun">The Baltimore Sun</a></i> which published articles about waste, fraud, and abuse at the NSA, including stories about Trailblazer.  In April 2010, Drake was indicted by a grand jury on various charges, including obstructing justice and making false statements.  After the May 22, 2011 broadcast of a <i><a href="/wiki/60_Minutes" title="60 Minutes">60 Minutes</a></i> episode on the Drake case, the government dropped all of the charges against Drake and agreed not to seek any jail time in return for Drake's agreement to plead guilty to a misdemeanor of misusing the agency's computer system. Drake was sentenced to one year of probation and community service.<sup id="cite_ref-147" class="reference"><a href="#cite_note-147"><span class="cite-bracket">[</span>147<span class="cite-bracket">]</span></a></sup>
</td></tr>
<tr>
<td>2005
</td>
<td>
</td>
<td><a href="/wiki/Thomas_Tamm" title="Thomas Tamm">Thomas Tamm</a>
</td>
<td>Male
</td>
<td><a href="/wiki/United_States_Department_of_Justice" title="United States Department of Justice">United States Department of Justice</a>
</td>
<td>Attorney for the DOJ's <a href="/wiki/Office_of_Intelligence_Policy_and_Review" title="Office of Intelligence Policy and Review">Office of Intelligence Policy and Review</a> who initially informed <i>The New York Times</i> for the story that became a 2005 exposé on <a href="/wiki/Mass_surveillance_in_the_United_States" title="Mass surveillance in the United States">mass warrantless surveillance</a>. His home was raided in 2007 during FBI investigation of the leaks and he began to openly speak out publicly in 2008.
</td></tr>
<tr>
<td>2006
</td>
<td><span typeof="mw:File"><a href="/wiki/File:2008_IEEE-SSIT_Barus_Award_Presenation.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/3/35/2008_IEEE-SSIT_Barus_Award_Presenation.jpg/75px-2008_IEEE-SSIT_Barus_Award_Presenation.jpg" decoding="async" width="75" height="35" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/35/2008_IEEE-SSIT_Barus_Award_Presenation.jpg/113px-2008_IEEE-SSIT_Barus_Award_Presenation.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/35/2008_IEEE-SSIT_Barus_Award_Presenation.jpg/150px-2008_IEEE-SSIT_Barus_Award_Presenation.jpg 2x" data-file-width="330" data-file-height="153"></a></span>
</td>
<td><a href="/wiki/Michael_DeKort" title="Michael DeKort">Michael DeKort</a>
<p><a href="/w/index.php?title=Anthony_D%27Armiento&amp;action=edit&amp;redlink=1" class="new" title="Anthony D'Armiento (page does not exist)">Anthony D'Armiento</a>
</p>
</td>
<td>Male
</td>
<td><a href="/wiki/United_States_Department_of_Homeland_Security" title="United States Department of Homeland Security">United States Department of Homeland Security</a> – <a href="/wiki/United_States_Coast_Guard" title="United States Coast Guard">United States Coast Guard</a>
</td>
<td>Michael DeKort was an American <a href="/wiki/Systems_engineer" class="mw-redirect" title="Systems engineer">systems engineer</a> and <a href="/wiki/Project_manager" title="Project manager">project manager</a> at <a href="/wiki/Lockheed_Martin" title="Lockheed Martin">Lockheed Martin</a> who posted a whistleblowing video on <a href="/wiki/YouTube.com" class="mw-redirect" title="YouTube.com">YouTube.com</a> about the Lockheed <a href="/wiki/Integrated_Deepwater_System_Program" title="Integrated Deepwater System Program">Integrated Deepwater System Program</a>.<sup id="cite_ref-WaPo_148-0" class="reference"><a href="#cite_note-WaPo-148"><span class="cite-bracket">[</span>148<span class="cite-bracket">]</span></a></sup> In 2008, DeKort was awarded the Society on Social Implications of Technology's public service award.<sup id="cite_ref-149" class="reference"><a href="#cite_note-149"><span class="cite-bracket">[</span>149<span class="cite-bracket">]</span></a></sup> As well as the Barus Ethics Award from the <a href="/wiki/IEEE" class="mw-redirect" title="IEEE">IEEE</a> for his efforts to ensure accountability and <a href="/wiki/Whistleblowing" title="Whistleblowing">whistleblowing</a> video.<sup id="cite_ref-150" class="reference"><a href="#cite_note-150"><span class="cite-bracket">[</span>150<span class="cite-bracket">]</span></a></sup> D'Armiento claimed retaliation for reporting the issues.<sup id="cite_ref-151" class="reference"><a href="#cite_note-151"><span class="cite-bracket">[</span>151<span class="cite-bracket">]</span></a></sup>
</td></tr>
<tr>
<td>2006
</td>
<td><span typeof="mw:File"><a href="/wiki/File:Mark_Klein_AT%26T.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Mark_Klein_AT%26T.jpg/75px-Mark_Klein_AT%26T.jpg" decoding="async" width="75" height="71" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Mark_Klein_AT%26T.jpg/113px-Mark_Klein_AT%26T.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Mark_Klein_AT%26T.jpg/150px-Mark_Klein_AT%26T.jpg 2x" data-file-width="1944" data-file-height="1840"></a></span>
</td>
<td><a href="/wiki/Mark_Klein" title="Mark Klein">Mark Klein</a>
</td>
<td>Male
</td>
<td><a href="/wiki/AT%26T" title="AT&amp;T">AT&amp;T</a>, <a href="/wiki/National_Security_Agency" title="National Security Agency">National Security Agency</a>
</td>
<td>Retired communications technician for <a href="/wiki/AT%26T" title="AT&amp;T">AT&amp;T</a> who revealed the details of the secret 2003 construction of a monitoring facility in <a href="/wiki/Room_641A" title="Room 641A">Room 641A</a> of 611 Folsom Street in San Francisco, the site of a large SBC phone building, three floors of which are occupied by AT&amp;T. The facility is alleged to be one of several operated by the <a href="/wiki/National_Security_Agency" title="National Security Agency">National Security Agency</a> as part of the <a href="/wiki/NSA_warrantless_surveillance_controversy#Technical_and_operational_details" class="mw-redirect" title="NSA warrantless surveillance controversy">warrantless surveillance</a> undertaken by the Bush administration in the wake of the September 11, 2001 terrorist attacks.<sup id="cite_ref-152" class="reference"><a href="#cite_note-152"><span class="cite-bracket">[</span>152<span class="cite-bracket">]</span></a></sup>
</td></tr>
<tr>
<td>2006
</td>
<td>
</td>
<td><a href="/wiki/Cate_Jenkins" title="Cate Jenkins">Cate Jenkins</a>
</td>
<td>Female
</td>
<td><a href="/wiki/United_States_Environmental_Protection_Agency" title="United States Environmental Protection Agency">United States Environmental Protection Agency</a>
</td>
<td>Wrote memos to the <a href="/wiki/United_States_Environmental_Protection_Agency" title="United States Environmental Protection Agency">EPA</a> <a href="/wiki/Inspector_general" title="Inspector general">Inspector General</a>, <a href="/wiki/United_States_Congress" title="United States Congress">U.S. Congress</a>, and <a href="/wiki/Federal_Bureau_of_Investigation" title="Federal Bureau of Investigation">FBI</a> detailing the chemical composition of dust from the <a href="/wiki/September_11_attacks" title="September 11 attacks">September 11 attacks</a> and its hazards to responders.<sup id="cite_ref-153" class="reference"><a href="#cite_note-153"><span class="cite-bracket">[</span>153<span class="cite-bracket">]</span></a></sup> She alerted <i><a href="/wiki/The_New_York_Times" title="The New York Times">The New York Times</a></i> in 2006<sup id="cite_ref-154" class="reference"><a href="#cite_note-154"><span class="cite-bracket">[</span>154<span class="cite-bracket">]</span></a></sup> and said in a 2009 <a href="/wiki/CBS" title="CBS">CBS</a> interview<sup id="cite_ref-155" class="reference"><a href="#cite_note-155"><span class="cite-bracket">[</span>155<span class="cite-bracket">]</span></a></sup> that the <a href="/wiki/United_States_Environmental_Protection_Agency_September_11_attacks_pollution_controversy" title="United States Environmental Protection Agency September 11 attacks pollution controversy">EPA</a> explicitly lied about the <a href="/wiki/Health_effects_arising_from_the_September_11_attacks" title="Health effects arising from the September 11 attacks">danger of the dust</a> which caused chemical burns in the lungs of <a href="/wiki/Rescue_and_recovery_effort_after_the_September_11_attacks" class="mw-redirect" title="Rescue and recovery effort after the September 11 attacks">responders</a>, debilitating illnesses in many that included fatalities, and that it could have been prevented with proper safety equipment. Jenkins claims that the EPA has been misleading about evidence of debris inhalation hazards since the 1980s. She was fired and in 2012 successfully sued to be reinstated.<sup id="cite_ref-156" class="reference"><a href="#cite_note-156"><span class="cite-bracket">[</span>156<span class="cite-bracket">]</span></a></sup><sup id="cite_ref-157" class="reference"><a href="#cite_note-157"><span class="cite-bracket">[</span>157<span class="cite-bracket">]</span></a></sup>
</td></tr>
<tr>
<td>2007
</td>
<td>
</td>
<td><a href="/wiki/John_Kiriakou" title="John Kiriakou">John Kiriakou</a>
</td>
<td>Male
</td>
<td><a href="/wiki/Central_Intelligence_Agency" title="Central Intelligence Agency">Central Intelligence Agency</a>
</td>
<td>In an interview to ABC News on December 10, CIA officer Kiriakou disclosed that the agency <a href="/wiki/Waterboarding" title="Waterboarding">waterboarded detainees</a> and that this constituted torture. In the months following, Kiriakou passed the identity of a covert CIA operative to a reporter.  He was convicted of violating the <a href="/wiki/Intelligence_Identities_Protection_Act" title="Intelligence Identities Protection Act">Intelligence Identities Protection Act</a> and sentenced, on January 25, 2013, to 30 months imprisonment. Having served the first months of his service he wrote an open letter describing the inhuman circumstances at the correction facility.<sup id="cite_ref-158" class="reference"><a href="#cite_note-158"><span class="cite-bracket">[</span>158<span class="cite-bracket">]</span></a></sup>
</td></tr>
<tr>
<td>2008
</td>
<td><span typeof="mw:File"><a href="/wiki/File:Anat_Kamm_9.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Anat_Kamm_9.jpg/75px-Anat_Kamm_9.jpg" decoding="async" width="75" height="100" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Anat_Kamm_9.jpg/113px-Anat_Kamm_9.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Anat_Kamm_9.jpg/150px-Anat_Kamm_9.jpg 2x" data-file-width="2448" data-file-height="3264"></a></span>
</td>
<td><a href="/wiki/Anat_Kamm-Uri_Blau_affair" class="mw-redirect" title="Anat Kamm-Uri Blau affair">Anat Kamm</a>
</td>
<td>Female
</td>
<td><a href="/wiki/Israeli_Defense_Force" class="mw-redirect" title="Israeli Defense Force">Israeli Defense Force</a>
</td>
<td>Leaked documents to the media that revealed <a href="/wiki/Targeted_killing_by_Israel" title="Targeted killing by Israel">the IDF had been engaging in extrajudicial killings</a>.<sup id="cite_ref-159" class="reference"><a href="#cite_note-159"><span class="cite-bracket">[</span>159<span class="cite-bracket">]</span></a></sup> While serving as an assistant in the <a href="/wiki/Central_Command_(Israel)" title="Central Command (Israel)">Central Command</a> bureau, Kamm secretly copied classified documents that she leaked to the Israeli <i><a href="/wiki/Haaretz" title="Haaretz">Haaretz</a></i> journalist <a href="/wiki/Uri_Blau" title="Uri Blau">Uri Blau</a> after her military service was over. The leak suggested that the IDF had defied a court ruling against assassinating wanted militants in the <a href="/wiki/West_Bank" title="West Bank">West Bank</a> who could potentially be arrested safely.<sup id="cite_ref-160" class="reference"><a href="#cite_note-160"><span class="cite-bracket">[</span>160<span class="cite-bracket">]</span></a></sup><sup id="cite_ref-161" class="reference"><a href="#cite_note-161"><span class="cite-bracket">[</span>161<span class="cite-bracket">]</span></a></sup> Kamm was convicted of espionage and providing confidential information without authorization.
</td></tr>
<tr>
<td>2008
</td>
<td>
</td>
<td><a href="/wiki/Rudolf_Elmer" title="Rudolf Elmer">Rudolf Elmer</a>
</td>
<td>Male
</td>
<td><a href="/wiki/Julius_B%C3%A4r" class="mw-redirect" title="Julius Bär">Julius Bär</a>
</td>
<td>A long-term employee of the Swiss bank whose final position entailed overseeing its Caribbean operations until he was terminated in 2002, Elmer blew the whistle on Julius Bär in 2008 when he gave secret documents to <a href="/wiki/WikiLeaks" title="WikiLeaks">WikiLeaks</a>. The documents detailed Julius Bär's activities in the <a href="/wiki/Cayman_Islands" title="Cayman Islands">Cayman Islands</a> and alleged <a href="/wiki/Tax_evasion" title="Tax evasion">tax evasion</a>. Convicted in <a href="/wiki/Switzerland" title="Switzerland">Switzerland</a> in January 2011, he was rearrested immediately for having distributed illegally obtained data to WikiLeaks. Julius Bär alleges that Elmer has doctored evidence to suggest the tax evasion.<sup id="cite_ref-cnn_162-0" class="reference"><a href="#cite_note-cnn-162"><span class="cite-bracket">[</span>162<span class="cite-bracket">]</span></a></sup><sup id="cite_ref-NYT_163-0" class="reference"><a href="#cite_note-NYT-163"><span class="cite-bracket">[</span>163<span class="cite-bracket">]</span></a></sup><sup id="cite_ref-guardian16_164-0" class="reference"><a href="#cite_note-guardian16-164"><span class="cite-bracket">[</span>164<span class="cite-bracket">]</span></a></sup><sup id="cite_ref-guardian17_165-0" class="reference"><a href="#cite_note-guardian17-165"><span class="cite-bracket">[</span>165<span class="cite-bracket">]</span></a></sup><sup id="cite_ref-BBC_166-0" class="reference"><a href="#cite_note-BBC-166"><span class="cite-bracket">[</span>166<span class="cite-bracket">]</span></a></sup>
</td></tr></tbody>'''

'''
soup = bs4(html, 'html.parser')

header_row = soup.find('tr')

headers = [th.get_text(strip=True) for th in header_row.find_all('th')]


=print(headers)


soup = bs4(html, parser='lxml')

htmltable = soup.find('table', { 'class' : 'wikitable sortable query-tablesorter' })
# where the dictionary specify unique attributes for the 'table' tag

def tableDataText(table):    
    """Parses a html segment started with tag <table> followed 
    by multiple <tr> (table rows) and inner <td> (table data) tags. 
    It returns a list of rows with inner columns. 
    Accepts only one <th> (table header/data) in the first row.
    """
    def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]  
    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append(rowgetDataText(tr, 'td') ) # data row       
    return rows

list_table = tableDataText(html_body)
list_table[:2]
'''

import pandas as pd
from bs4 import BeautifulSoup as bs4
import requests

url = 'https://en.wikipedia.org/wiki/List_of_whistleblowers'
page = requests.get(url)
soup = bs4(page.text, 'html.parser')
dfs = pd.read_html(page.text)
tables = soup.find_all("table", class_='wikitable sortable jquery-tablesorter')

for index, table in enumerate(tables):
    for row in table.find_all('tr'):
        cells = row.find_all(['th', 'td'])
        cell_data = [cell.get_text(strip=True) for cell in cells]
        if cell_data:
            print(cell_data)

dataframes = pd.read_html(page.text)

for df_index, df in enumerate(dataframes):
    csv_file_name = f'whistleblowers_table_{df_index + 1}.csv'  # Create a unique filename
    df.to_csv(csv_file_name, index=False)  # Save DataFrame to CSV without the index
    print(f'Saved {csv_file_name}')

#for json files!! 
    '''for df_index, df in enumerate(dataframes):
    json_file_name = f'whistleblowers_table_{df_index + 1}.json'  # Create a unique filename
    df.to_json(orient="split")  # Save DataFrame to CSV without the index
    print(f'Saved {json_file_name}')'''