import RallyContext
import RallyAnalysis
import JasonSendMail






#MAIN

#Pull Orcavengers data from Rally using Rally API key
print "Get Rally Project Info"
r = RallyContext.RallyContext('_aC8FkwE1SCmlL8RMoOLCZmWZ5WQlkAppUwu5mDMDZM')



#Analyse Rally data
print "Analyse"
analyses = [RallyAnalysis.rally_analysis_grooming_health(),
            RallyAnalysis.rally_analysis_wip()]

body = ''
for analysis in analyses:
    analysis.analyse(r)
    advice = analysis.print_advice()
    print advice
    body += advice + '\n'





#Send Results
#print "Send Results"
#smtp = JasonSendMail.SendMail('d2l\jason', 'JasonD2L', 'ssrs.reachmail.net', 587)
#smtp = JasonSendMail.SendMail('', '', '192.168.10.11 ', 587)
#smtp.sendmail('jason.wood@d2l.com', 'jason.wood@d2l.com', "Daily Rally Health", body)
